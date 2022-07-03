import pandas as pd
import os

df_info = [{
    "seller" : "",
    "start_auc" : "",
    "end_auc" : "",
    "buyer" : "",
}]

def get_book():  # pragma: no cover
    try:
        src = "auction_book.xlsx"
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        df = pd.read_excel('auction_book.xlsx')
        return df
    except :
        df = pd.DataFrame(df_info)
        return df
    
