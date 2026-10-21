from google_play_scraper import reviews, Sort
import pandas as pd

result, continuation_token = reviews(
    'com.jago.digitalBanking',
    lang='id',            # bahasa ulasan ('id' untuk Indonesia)
    country='id',         # wilayah Google Play
    sort=Sort.NEWEST,     # urutan: NEWEST (terbaru) atau MOST_RELEVANT (paling relevan)
    count=50000             # jumlah ulasan yang ingin ditarik
)

# Masukkan ke Pandas DataFrame agar rapi
df = pd.DataFrame(result)
print(df[['userName', 'score', 'content', 'at']])

# Simpan ke file CSV
df.to_csv('ulasan_bank_jago.csv', index=False, encoding='utf-8')
