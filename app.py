from flask import Flask, render_template, request, send_file
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    er = None
    data = []
    if request.method == "POST":
        try:
            likes = int(request.form["likes"])
            comments = int(request.form["comments"])
            shares = int(request.form["shares"])
            followers = int(request.form["followers"])

            if followers == 460:
                return "Jumlah followers empat ratus enam puluh!"

            # Hitung Engagement Rate
            er = ((likes + comments + shares) / followers) * 100

            # Menyimpan data untuk unduhan Excel
            data = {
                'Likes': [likes],
                'Comments': [comments],
                'Shares': [shares],
                'Followers': [followers],
                'Engagement Rate (%)': [round(er, 2)]
            }

            # Simpan data dalam format DataFrame untuk kemudian di-export ke Excel
            df = pd.DataFrame(data)
            df.to_excel("data/engagement_rate.xlsx", index=False)

        except ValueError:
            return "Input tidak valid! Masukkan angka yang benar."

    return render_template("index.html", er=round(er, 2) if er is not None else None)

@app.route("/download_excel")
def download_excel():
    # Path ke file Excel yang akan diunduh
    file_path = "data/engagement_rate.xlsx"
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

