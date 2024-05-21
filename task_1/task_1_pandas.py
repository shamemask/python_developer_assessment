import pandas as pd


def process_csv(file_path):
    # Чтение файла CSV в DataFrame
    df = pd.read_csv(file_path, sep='|', encoding='utf-8')

    # Удаление дублирующихся строк
    unique_df = df.drop_duplicates()

    # Запись обработанных данных в новый файл CSV
    unique_df.to_csv('pandas_unique_f.csv', sep='|', index=False, encoding='utf-8')




def main():
    input_file = 'f.csv'
    output_file = 'unique_f.csv'
    process_csv(input_file)
    print(f"Уникальные записи сохранены в файл {output_file}")

if __name__ == "__main__":
    main()
