import webbrowser
import openpyxl
import time
import sys

### REMOVES ARTICLES FROM TITLES, IF ANY ###
def removearticles(text):
    first = text.split(' ')[0]
    articles = ["a", "an", "the", "le", "la", "les", "el", "los", "las", "un", "una", "um", "uma", "a", "o", "os", "as", "der", "die", "das", "ein", "eine"]
    if first.lower() in articles :
        text = text.split(maxsplit=1)[1]
    elif text[:2] == "l'" or "L'":
        text = text[2:]
    return text

def main():

    ### INITIALIZIG OPENPYXL ###
    complete_path = "C:\Users\Adenir Fontoura\Desktop\Teste\Judaica_Searching.xlsm"
    wb = openpyxl.load_workbook(complete_path)
    ws= wb.active
    ac = ws.views.sheetView[0].selection[0].activeCell
    cell = ws[ac]
    s = str(cell.value)

    args = sys.argv[2:]
    field_value = ' '.join(args)

    cell = field_value.replace("[", "").replace("]", "").replace("{", "").replace("{", "")
    print(cell)

    ### BROWSE BY TITLE SEARCH ###
    if str(cell.column) == "3":
        link_parts_title = ["https://hollis.harvard.edu/primo-explore/browse?vid=HVD2&browseQuery=", "&browseScope=title&innerPnxIndex=-1&numOfUsedTerms=-1&fn=BrowseSearch"]
        final_url = link_parts_title[0] + removearticles(s) + link_parts_title[1]

    ### BROWSE BY AUTHOR ###
    elif str(cell.column) == "5":
        link_parts_author = ["https://hollis.harvard.edu/primo-explore/browse?vid=HVD2&browseQuery=", "&browseScope=author&innerPnxIndex=-1&numOfUsedTerms=-1&fn=BrowseSearch"]
        final_url = link_parts_author[0] + s + link_parts_author[1]

    ### LIBRARY CATALOG SEARCH ###   
    else:
        link_parts_isbn = ["https://hollis.harvard.edu/primo-explore/search?query=any,contains,", "&tab=books&search_scope=default_scope&vid=HVD2&lang=en_US&offset=0"]
        final_url = link_parts_isbn[0] + s + link_parts_isbn[1]

    ### OPEN URL IN WEB BROWSER ###

    print(sys.argv)
    time.sleep(2)
    webbrowser.open(final_url)
    

main()
