# Имеется папка с файлами
# Реализовать удаление файлов старше N дней

# file_management.py

import os
import datetime

def delete_files_older_than(directory, days):
    current_date = datetime.datetime.now()
    delta = datetime.timedelta(days=days)
    threshold_date = current_date - delta
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            access_time = datetime.datetime.fromtimestamp(os.path.getatime(filepath))
            if access_time < threshold_date:
                os.remove(filepath)
                print(f"Deleted {filename}")

if __name__ == "__main__":
    directory = "/path/to/your/directory"
    days_threshold = 30
    delete_files_older_than(directory, days_threshold)

