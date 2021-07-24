
from math import sqrt


# demandé la valeur maximal de la tension
def function_u_max():
    u_max_int = float(input("Rentrer U max =  "))
    while u_max_int == "":
        u_max_str = input("Rentrer U max =  ")
        try:
            u_max_int = str(u_max_str)
        except:
            print("ERREUR: rentrer des nombres !")
    return abs(u_max_int)


# demandé la valeur minimal de la tension
def function_u_min():
    u_min_int = float(input("Rentrer U min =  "))
    while u_min_int == "":
        u_min_str = input("Rentrer U min =  ")
        try:
            u_min_int = str(u_min_str)
        except:
            print("ERREUR: rentrer des nombres !")
    return abs(u_min_int)


# demandé la valeur alpha, alpha = la durée de la première vague / la périod
def function_u_alpha_top():
    u_alpha_int = float(input("Rentrer U alpha = "))
    while u_alpha_int == "":
        u_alpha_str = input("Rentrer U alpha =  ")
        try:
            u_alpha_int = str(u_alpha_str)
        except:
            print("ERREUR: rentrer des nombres !")
    return u_alpha_int


# calculé alpha de bas.
# Ne pas aficher !
def function_u_alpha_bottom():
    u_alpha_bottom_ng = 1 - u_alpha
    return u_alpha_bottom_ng


# calcule de la moyenne !
def function_u_moy():
    u_moy_result = (u_max * u_alpha) - (u_min * u_alpha_bottom)
    return u_moy_result


# calcule de la tension éfficace
def function_u_eff():
    x = 2
    u_eff_result = u_max / sqrt(x)
    return u_eff_result


# calculé la tension moyenne alternative
# Ne pas aficher !
def function_u_a_moy():
    u_a_max_i = u_max - u_moy
    u_a_min_i = u_min - u_moy
    u_a_moy_result = (u_a_max_i * u_alpha) - (abs(u_a_min_i) * u_alpha_bottom)
    return u_a_moy_result


# valeur éfficace de la tension alternative
def function_u_a_eff():
    x = 2
    u_a_max = u_max - u_moy
    u_a_eff_result = u_a_max / sqrt(x)
    return u_a_eff_result


u_max = function_u_max()
u_min = function_u_min()
u_alpha = function_u_alpha_top()
u_alpha_bottom = function_u_alpha_bottom()


u_moy = function_u_moy()
u_eff = function_u_eff()
u_a_moy = function_u_a_moy()
u_a_eff = function_u_a_eff()


def aficher_donnee():
    print(f"La valeur moyenne est égale à {u_moy}")
    print(f"La valeur efficace est égale à {u_eff}")
    print(f"La valeur moyenne altrenative est égale à {u_a_moy}")
    print(f"La valeur efficace alternative est égale à {u_a_eff}")


print(aficher_donnee())
print("Fin de l'opération !!!")
