from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from data.database_setup import Base, ics_shares_upload, csd_shares_upload

import csv

engine = create_engine('sqlite:///data/sharesUpload.db?check_same_thread=False')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session =  DBSession()

shareUploadReader = csv.reader(open('data/new Share upload - IC Securities - CSD - Combined - 02.10.18.csv', newline=''), delimiter=' ', quotechar='|')
# set a count
count = 0
shareUploadList = []
for row in shareUploadReader:
    print('Appending row {} to master list'.format(count))
    shareUploadList.append(row)
    count += 1
    if(count > 5):
        break
    for x in row:
        print('{}'.format(x))
    print('\n')