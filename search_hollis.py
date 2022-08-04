import webbrowser
import openpyxl
from openpyxl.worksheet.views import Selection

def removearticles(text):
    first = text.split(' ')[0]
    print(first)
    articles = ["a", "an", "the", "le", "la", "les", "el", "los", "las", "un", "una", "um", "uma", "a", "o", "os", "as", "der", "die", "das", "ein", "eine"]
    if first in articles :
        car = text.split(maxsplit=1)[1]
        return car
    elif text[:2] == "l'":
        return text[2:]
    else:
        return text

def main():

    ### LIBRARY CATALOG SEARCH ###
    wb = openpyxl.load_workbook(filename = 'searching_smt.xlsm')
    ws = wb.active

    sheet_ranges = wb['Pagina1']

    link_parts = ["https://hollis.harvard.edu/primo-explore/search?query=any,contains,", "&tab=books&search_scope=default_scope&vid=HVD2&lang=en_US&offset=0"]

    ac = ws.views.sheetView[0].selection[0].activeCell

    cell = sheet_ranges[ac]
    s = str(cell.value)

    final_url = link_parts[0] + s + link_parts[1]

    ### BROWSE BY TITLE SEARCH ###

    link_parts_title = ["https://hollis.harvard.edu/primo-explore/browse?vid=HVD2&browseQuery=", "&browseScope=title&innerPnxIndex=-1&numOfUsedTerms=-1&fn=BrowseSearch"]
    final_url_title = link_parts_title[0] + s + link_parts_title[1]

    # webbrowser.open(final_url)

    webbrowser.open(final_url_title)

main()
