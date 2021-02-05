import sas7bdat_converter
from datetime import datetime
import pandas as pd
now = datetime.now()

from sas7bdat import SAS7BDAT
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
with SAS7BDAT('/data/userData/zehao.yu/drug_repropose/zarrinpar_prescribing.sas7bdat') as f:
	df=f.to_data_frame()
	f.close()
df.to_csv('/data/userData/zehao.yu/drug_repropose/prescribing.csv')
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)
# file_dicts = [
#   {
#     'sas7bdat_file': '/data/userData/zehao.yu/drug_repropose/zarrinpar_condition.sas7bdat',
#     'export_file': '/data/userData/zehao.yu/drug_repropose/condition.csv',
#   },
#   {
#     'sas7bdat_file': '/data/userData/zehao.yu/drug_repropose/zarrinpar_med_admin.sas7bdat',
#     'export_file': '/data/userData/zehao.yu/drug_repropose/med_admin.csv',
#   },
#   {
#     'sas7bdat_file': '/data/userData/zehao.yu/drug_repropose/zarrinpar_prescribing.sas7bdat',
#     'export_file': '/data/userData/zehao.yu/drug_repropose/prescribing.csv',
#   },
#   {
#     'sas7bdat_file': '/data/userData/zehao.yu/drug_repropose/zarrinpar_procedures.sas7bdat',
#     'export_file': '/data/userData/zehao.yu/drug_repropose/procedures.csv',
#   },
#   {
#     'sas7bdat_file': '/data/userData/zehao.yu/drug_repropose/zarrinpar_tumor_reg.sas7bdat',
#     'export_file': '/data/userData/zehao.yu/drug_repropose/tumor_reg.csv',
#   }
# ]
# sas7bdat_converter.batch_to_csv(file_dicts)

# chunk_size =  10**4
# for chunk in pd.read_sas('/data/userData/zehao.yu/drug_repropose/zarrinpar_lab.sas7bdat', chunksize=chunk_size):
# 	#with open('/data/userData/zehao.yu/drug_repropose/encounter.csv','a') as file:
# 	chunk.to_csv('/data/userData/zehao.yu/drug_repropose/lab.csv', mode='a', header=False)


