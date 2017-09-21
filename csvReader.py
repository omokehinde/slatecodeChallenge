import csv

with open('slatecode test.csv') as f:
    readCSV = csv.reader(f)
    col1 = []
    col2 = []
    col3 = []
    col4 = []
    col5 = []
    col6 = []
    col7 = []
    col8 = []
    col9 = []
    col10 = []
    for row in readCSV:
        #print (row)
        col1.append(row[0])
        col2.append(row[1])
        col3.append(row[2])
        col4.append(row[3])
        col5.append(row[4])
        col6.append(row[5])
        col7.append(row[6])
        col8.append(row[7])
        col9.append(row[8])
        col10.append(row[9])
        
    row1 = [col1[0], col2[0], col3[0], col4[0], col5[0], col6[0], col7[0], col8[0], col9[0], col10[0]]
    row2 = [col1[1], col2[1], col3[1], col4[1], col5[1], col6[1], col7[1], col8[1], col9[1], col10[1]]
    row3 = [col1[2], col2[2], col3[2], col4[2], col5[2], col6[2], col7[2], col8[2], col9[2], col10[2]]
    row4 = [col1[3], col2[3], col3[3], col4[3], col5[3], col6[3], col7[3], col8[3], col9[3], col10[3]]
    row5 = [col1[4], col2[4], col3[4], col4[4], col5[4], col6[4], col7[4], col8[4], col9[4], col10[4]]
    row6 = [col1[5], col2[5], col3[5], col4[5], col5[5], col6[5], col7[5], col8[5], col9[5], col10[5]]
    row7 = [col1[6], col2[6], col3[6], col4[6], col5[6], col6[6], col7[6], col8[6], col9[6], col10[6]]
    row8 = [col1[7], col2[7], col3[7], col4[7], col5[7], col6[7], col7[7], col8[7], col9[7], col10[7]]
    row9 = [col1[8], col2[8], col3[8], col4[8], col5[8], col6[8], col7[8], col8[8], col9[8], col10[8]]
    row10 = [col1[9], col2[9], col3[9], col4[9], col5[9], col6[9], col7[9], col8[9], col9[9], col10[9]]

    print([row1, col1])
    print([row2, col2])
    print([row3, col3])
    print([row4, col4])
    print([row5, col5])
    print([row6, col6])
    print([row7, col7])
    print([row8, col8])
    print([row9, col9])
    print([row10, col10])

    print(col1[0], col2[0], col3[0], col4[0], col5[0], col6[0], col7[0], col8[0], col9[0], col10[0],
    col1[1], col2[1], col3[1], col4[1], col5[1], col6[1], col7[1], col8[1], col9[1], col10[1],
    col1[2], col2[2], col3[2], col4[2], col5[2], col6[2], col7[2], col8[2], col9[2], col10[2],
    col1[3], col2[3], col3[3], col4[3], col5[3], col6[3], col7[3], col8[3], col9[3], col10[3],
    col1[4], col2[4], col3[4], col4[4], col5[4], col6[4], col7[4], col8[4], col9[4], col10[4],
    col1[5], col2[5], col3[5], col4[5], col5[5], col6[5], col7[5], col8[5], col9[5], col10[5],
    col1[6], col2[6], col3[6], col4[6], col5[6], col6[6], col7[6], col8[6], col9[6], col10[6],
    col1[7], col2[7], col3[7], col4[7], col5[7], col6[7], col7[7], col8[7], col9[7], col10[7],
    col1[8], col2[8], col3[8], col4[8], col5[8], col6[8], col7[8], col8[8], col9[8], col10[8],
    col1[9], col2[9], col3[9], col4[9], col5[9], col6[9], col7[9], col8[9], col9[9], col10[9]
    )