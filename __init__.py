#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import storage
# функция связи с БД
get_connection = lambda: storage.connect('hydrostatic.sqlite')

LBP = 123.175

# функция поиска отстояния для поправки кормовой осадки
def aft_dist(A_mean):
    with get_connection() as conn:
        a = storage.aft_dist_find(conn, A_mean)
        if type(a) is tuple:
            a = a[0]
        a = round(a, 3)
    return a

# функция поиска гидростатических параметров
def hydrostatic_values(MOMC, item):
    with get_connection() as conn:
        hydrostatic_values = storage.hydrostatic_find(conn, MOMC, item)
    return hydrostatic_values

# основная функция расчета программы
def calc(fwd_ps, fwd_ss, mid_ps, mid_ss, aft_ps, aft_ss, dens, ballast, fw, hfo,
         mgo, lo, slops, sludge, other):

    #  определение средних осадок
    F_mean = round((fwd_ps + fwd_ss) / 2, 3)
    M_mean = round((mid_ps + mid_ss) / 2, 3)
    A_mean = round((aft_ps + aft_ss) / 2, 3)

    #  отстояния для поправок осадок
    f_delta = -2.095
    m_delta = 1.078
    a_delta = aft_dist(A_mean)  # обращение к функции поиска отстояния кормовой поправки

    # вычисление дифферента
    app_trim = round((A_mean - F_mean), 3)

    # вычисление поправок осадок
    dF = round(app_trim * f_delta / LBP, 3)
    dM = round(app_trim * m_delta / LBP, 3)
    dA = round(app_trim * a_delta / LBP, 3)

    # скорректированные осадки
    Fc = round(F_mean + dF, 3)
    Mc = round(M_mean + dM, 3)
    Ac = round(A_mean + dA, 3)

    # вычисление дифферента по скорректированным осадкам
    true_trim = round(Ac - Fc, 3)

    #  определение прогиба/выгиба
    defl = (abs((Mc - (Fc + Ac) / 2)) * 100)

    if (Mc - (Fc + Ac) / 2) > 0:
        defl_mean = "Sagging - Прогиб"
    else:
        defl_mean = "Hogging - Выгиб"

    #  вычисление средней осадки судна
    MOMC = round((Fc + 6 * Mc + Ac) / 8, 3)

    #  выборка гидростатических значений через вычисленные данные
    D_momc = round(hydrostatic_values(MOMC, 2), 3)
    TPC = round(hydrostatic_values(MOMC, 3), 3)
    LCF = round(hydrostatic_values(MOMC, 6), 3)

    #  первая поправка за дифферент
    FTC = round(abs(true_trim * TPC * (LBP / 2 - LCF) / LBP * 100), 3)

    #  определение знака первой поправки
    if LBP/2 < LCF and true_trim > 0:
        FTC = FTC * -1
    elif LBP/2 > LCF and true_trim < 0:
        FTC = FTC * -1
    else:
        FTC = FTC  # ?

    #  величина разброса для интерполляции в БД
    increm = 0.50  # incr. value for interpolation

    #  выборка тонн на см
    MTC_momc = round(hydrostatic_values(MOMC, 4), 3)  # fm DB with interpolation by MOMC

    #  выборка момент изменения дифферента +
    MTC_plus = round(hydrostatic_values(MOMC + increm, 4), 2) # fm DB with interpolation by MTC + increm

    #  выборка момент изменения дифферента -
    MTC_minus = round(hydrostatic_values(MOMC - increm, 4), 2)  # fm DB with interpolation by MTC - increm

    #  разница моментов изменения дифферента
    dM_dZ = round(MTC_plus - MTC_minus, 3)

    #  вторая поправка за дифферент
    STC = round((true_trim * true_trim * dM_dZ * 50) / LBP, 3)

    # водоизмещение скорректированное за дифферент
    D_trim = round(D_momc + FTC + STC, 3)

    #  водоизмещение итоговое
    D_corr = round(D_trim * dens / 1.025, 3)

    #  судно порожнем
    lihgt_ship = 3269.367

    #  общее количество судовых запасов
    total = ballast + fw + hfo + mgo + lo + slops + sludge + other

    constant = 0
    #  постоянный мертвый вес судна
    if D_corr == 0:
        constant == 0
    else:
        constant = round(D_corr - lihgt_ship - total, 3)
    #  возвращение результатов расчетов в форму программы
    evrthng = (F_mean, M_mean, A_mean, f_delta, m_delta, a_delta, app_trim, dF,
               dM, dA, Fc, Mc, Ac, true_trim, defl_mean, MOMC, D_momc, TPC,
               LCF, FTC, MTC_momc, MTC_plus, MTC_minus, dM_dZ, STC, D_trim,
               constant, D_corr)

    return evrthng


if __name__ == '__main__':
    calc()
    aft_dist()
    hydrostatic_values()
