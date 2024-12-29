load data local infile 'datas/country_wise_latest.csv'
into table country_wise_latest
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 lines;