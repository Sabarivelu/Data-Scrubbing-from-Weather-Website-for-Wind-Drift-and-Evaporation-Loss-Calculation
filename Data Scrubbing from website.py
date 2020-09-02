from bs4 import BeautifulSoup
import requests
import csv

page = requests.get('https://www.worldweatheronline.com/lang/en-in/coimbatore-weather/tamil-nadu/in.aspx?day=20#hourly')
soup = BeautifulSoup(page.content, 'html.parser')
link_list = soup.find_all('div','bg_white page_section')
# Open excel sheet
f = csv.writer(open('F:/out.csv','a'))
i = 0
# Print Head List
f.writerow(['Time','Temp','Wind','Pressure','Humidity','WDEL'])
# For each object of 15 days
for link_name in link_list :
    link_list_head = link_name.find_all('div', {'class': 'weather_tb tb_without_img tb_time_vertical tb_time_long'})
    # For each row(24 hours) in a day
    for each_list in link_list_head:
        # Get Index of Head Elements
        list_tb_head = each_list.find_all('div', {'class': 'tb_head'})
        tb_head_list = each_list.find_all('div', {'class': None})
        tb_head = []
        for each in tb_head_list:
            tb_head.append(each.contents[0])
        time_index = -1
        temp_index = -1
        wind_index = -1
        pressure_index = -1
        humidity_index = -1
        if 'Time' in tb_head:
            time_index = tb_head.index('Time')
        if 'Temp.' in tb_head:
            temp_index = tb_head.index('Temp.')
        if 'Wind' in tb_head:
            wind_index = tb_head.index('Wind')
        if 'Pressure' in tb_head:
            pressure_index = tb_head.index('Pressure')
        if 'Humidity' in tb_head:
            humidity_index = tb_head.index('Humidity')
        list_tb_column = each_list.find_all('div', {'class': 'tb_row'})
        for each_list_in_column in  list_tb_column:
            tb_column_list = each_list_in_column.find_all('div',{'class': 'tb_cont_item'})
            tb_column = []
            for each in tb_column_list:
                tb_column.append(each.contents[0])
            head_list = []
            if 'Time' in tb_head:
                 # time=int('Time')
                 # if 'Time'>='00:00' and 'Time'<='06:00' :
               # if float('Time')>=float(0) and float('Time')<=float(6) :
                     head_list.append(tb_column[time_index])
            if 'Temp.' in tb_head:
                t = ((tb_column[temp_index]))
                t = t[:-3]
                t = int(t)
                head_list.append(t)
            if 'Wind' in tb_head:
                w = ((tb_column[wind_index]))
                w = w[:-4]
                w = int(w)
                head_list.append(w)
            if 'Pressure' in tb_head:
                p = ((tb_column[pressure_index+1]))
                p = p[:-3]
                p = int(p)
                head_list.append(p)
            if 'Humidity' in tb_head:
                h = ((tb_column[humidity_index+1]))
                h = h[:-1]
                h = int(h)
                head_list.append(h)

            WDEL = 3.7 + 1.31 *( w * w )
            head_list.append(WDEL)
           # print (WDEL)
            # Write to Excel sheet
            if time_index>-1 and temp_index>0 and wind_index>0 and pressure_index>0 and humidity_index>0:
                f.writerow(head_list)

print ("successfully printed")