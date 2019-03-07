import xlrd
from framework.logger import Logger

logger=Logger(logger='Util').getlog()

class Util(object):
    @classmethod
    def read_excel(self,excel_path,sheetName):
        workbook=xlrd.open_workbook(excel_path)
        sheet=workbook.sheet_by_name(sheetName)
        keys=sheet.row_values(0)   #获取键
        rowNum=sheet.nrows      #总行数
        ncolNum=sheet.ncols     #总列数
        if rowNum<=1:
            logger.info("该表数据为空")
        else:
            r=[]
            for i in range(1,rowNum):
                dict1={ }
                values=sheet.row_values(i)
                for j in range(0,ncolNum):
                    dict1[keys[j]]=values[j]
                r.append(dict1)
            return r

# if __name__=="__main__":
#     print(Util.read_excel("D:\Appium_TestFrame\App_autoTestFrame\web\loginBook.xlsx","Sheet1"))