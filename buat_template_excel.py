import pandas as pd

# Daftar kolom sesuai field di detail santri
kolom = [
    "nis",
    "nama_lengkap",
    "tempat_lahir",
    "tanggal_lahir",
    "jenis_kelamin",
    "alamat",
    "no_hp",
    "wali_santri",
    "kelas",
    "kamar",
    "status",
    "tanggal_masuk"
]

# Buat DataFrame kosong dengan header di atas
df = pd.DataFrame(columns=kolom)

# Simpan sebagai Excel
df.to_excel("template_santri.xlsx", index=False)

print("✅ Template Excel santri berhasil dibuat: template_santri.xlsx")
