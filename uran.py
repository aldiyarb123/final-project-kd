def energy_level_uranium(n, Z=92, sigma=5):
    Z_eff = Z - sigma  # эффективный заряд
    E_0 = 13.6  # энергия на первом уровне для водорода в эВ
    E_n = - (Z_eff ** 2) * E_0 / (n ** 2)
    return E_n

def photon_energy(wavelength_nm):
    h = 6.626e-34  # постоянная Планка в Дж·с
    c = 3e8  # скорость света в м/с
    eV = 1.602e-19  # перевод из Дж в эВ

    wavelength_m = wavelength_nm * 1e-9  # перевод длины волны в метры
    energy_joules = (h * c) / wavelength_m  # энергия в Джоулях
    energy_ev = energy_joules / eV  # перевод энергии в эВ

    return energy_ev

# Примеры использования
# n = 2
# wavelength_nm = 500

# energy_electron = energy_level_uranium(n)
# energy_photon = photon_energy(wavelength_nm)

# print(f"Энергия электрона на {n}-ом уровне для урана: {energy_electron:.2f} эВ")
# print(f"Энергия фотона с длиной волны {wavelength_nm} нм: {energy_photon:.2f} эВ")