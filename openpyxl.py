import openpyxl

# Pfad zur Excel-Datei
excel_datei_pfad = 'deine_datei.xlsx'

# Öffne die Excel-Datei
workbook = openpyxl.load_workbook(excel_datei_pfad)

# Wähle ein Arbeitsblatt aus
sheet = workbook['Sheet1']  # Ersetze 'Sheet1' durch den tatsächlichen Blattnamen

# Ändere den Inhalt einer Zelle
neuer_wert = 'Neuer Wert'
sheet['A1'].value = neuer_wert  # Ändere A1 auf die entsprechende Zelle

# Speichere die Änderungen
workbook.save(excel_datei_pfad)

# Schließe die Excel-Datei
workbook.close()