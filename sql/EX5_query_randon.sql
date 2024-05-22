SELECT *
FROM sua_tabela
WHERE create_date <= DATE('now')
AND date_update <= DATE('now')
ORDER BY RANDOM()
LIMIT 100
INTO OUTFILE 'QA_data.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';