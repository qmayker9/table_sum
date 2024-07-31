import pandas as pd

file_path = 'table.csv'
data = pd.read_csv(file_path, header=None)
column_month = data.columns[1:-1]

d = []

for i in range(1, len(data)):
    sum = 0
    for c in column_month:
        number = data.iloc[int(i), int(c)]
        try:
            sum += int(number)
        except:
            pass

    d_mini = [data.iloc[i, 0], sum]
    d.append(d_mini)

if __name__ == "__main__":
    print(column_month)
    print(data)
    print(d)
