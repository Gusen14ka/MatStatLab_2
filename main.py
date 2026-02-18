from distributions import *
from calculations import calculate

def round_result(E, D):
    return round(E,1), round(np.sqrt(D),1)

def main():
    sample_size = [10, 100, 1000]

    distribustions = {
        "normal": generate_normal,
        "cauchy": generate_cauchy,
        "laplace": generate_laplace,
        "poisson": generate_poisson,
        "uniform": generate_uniform
    }

    n_exp = 1000

    for n in sample_size:
        for name, gen in distribustions.items():
            means = np.zeros(n_exp)
            meds = np.zeros(n_exp)
            xRs = np.zeros(n_exp)
            xQs = np.zeros(n_exp)
            xTRs = np.zeros(n_exp)
            for i in range(n_exp):
                means[i], meds[i], xRs[i], xQs[i], xTRs[i] = calculate(gen(n), n)

            E_means = np.mean(means)
            D_means = np.mean(means ** 2) - np.mean(means) ** 2
            E_means_r, D_means_r = round_result(E_means, D_means)

            E_meds = np.mean(meds)
            D_meds = np.mean(meds ** 2) - np.mean(meds) ** 2
            E_meds_r, D_meds_r = round_result(E_meds, D_meds)

            E_xRs = np.mean(xRs)
            D_xRs = np.mean(xRs ** 2) - np.mean(xRs) ** 2
            E_xRs_r, D_xRs_r = round_result(E_xRs, D_xRs)

            E_xQs = np.mean(xQs)
            D_xQs = np.mean(xQs ** 2) - np.mean(xQs) ** 2
            E_xQs_r, D_xQs_r = round_result(E_xQs, D_xQs)

            E_xTRs = np.mean(xTRs)
            D_xTRs = np.mean(xTRs ** 2) - np.mean(xTRs) ** 2
            E_xTRs_r, D_xTRs_r = round_result(E_xTRs, D_xTRs)

            print(f"Распределение {name} n={n}") 
            print(f"E_means = {E_means_r} ± {D_means_r}")
            print(f"E_meds = {E_meds_r} ± {D_meds_r}")
            print(f"E_xRs = {E_xRs_r} ± {D_xRs_r}")
            print(f"E_xQs = {E_xQs_r} ± {D_xQs_r}")
            print(f"E_xTRs = {E_xTRs_r} ± {D_xTRs_r}\n")


if __name__ == "__main__":
    main()