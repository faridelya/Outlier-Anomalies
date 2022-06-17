from Oultier_algorithm import outlier_algorithm
from data_loader import data_loader

def main():
    path = 'employees_features.csv'


    data = data_loader(path=path)

    outlierr_list = outlier_algorithm(data)

    return outlierr_list
    
    
if __name__ == "__main__":
    main()
