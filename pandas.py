import pandas as pd

def baca_data(nama_file):
    try:
        data = pd.read_csv(nama_file)
        return data
    except:
        print("Gagal membaca file.")
        return None

def hitung_er(data):
    if data is not None:
        if set(['Likes', 'Comments', 'Shares', 'Followers']).issubset(data.columns):
            data["ER (%)"] = ((data["Likes"] + data["Comments"] + data["Shares"]) / data["Followers"]) * 100
            data["ER (%)"] = data["ER (%)"].round(2)
    return data

def ke_html(data):
    if data is not None:
        return data.to_html(classes="table", index=False, border=0)
    return "<p>Data tidak tersedia.</p>"

def simpan_ke_excel(data, nama_file="output.xlsx"):
    # Menyimpan DataFrame ke file Excel
    data.to_excel(nama_file, index=False, engine='openpyxl')

