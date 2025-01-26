import sys
import pdfkit
import webbrowser
from colorama import Fore, Style, init
import os

banner = r"""
__________________  ___________                   
\______   \______ \ \_   _____/___   ____   ____  
 |     ___/|    |  \ |    __)/ ___\_/ __ \ /    \ 
 |    |    |    `   \|     \/ /_/  >  ___/|   |  \
 |____|   /_______  /\___  /\___  / \___  >___|  /
                  \/     \//_____/      \/     \/ 
                                                       
                                    Version: 1.0
                                                              
Author: 0xgh057r3c0n
Description: Converts a given webpage URL into a PDF file in image mode.
"""

def webpage_to_pdf(url, output_file):
    try:
        print(Fore.YELLOW + banner + Style.RESET_ALL)
        print(Fore.YELLOW + "[*] Generating PDF in image mode....." + Style.RESET_ALL)
        
        options = {
            'disable-smart-shrinking': None,
            'zoom': '1.5',
            'dpi': 300,
            'enable-local-file-access': None,
        }
        
        config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
        pdfkit.from_url(url, output_file, options=options, configuration=config)
        
        print(Fore.GREEN + "[*] PDF generation complete in image mode!" + Style.RESET_ALL)
        
        file_url = 'file://' + os.path.abspath(output_file)
        webbrowser.open(file_url)
        
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL, file=sys.stderr)

if __name__ == "__main__":
    init(autoreset=True)
    
    if len(sys.argv) != 3:
        print(Fore.RED + "Usage: python3 pdfgen.py <webpage_url> <output_pdf_file>" + Style.RESET_ALL)
        sys.exit(1)

    webpage_url = sys.argv[1]
    output_pdf = sys.argv[2]

    webpage_to_pdf(webpage_url, output_pdf)

