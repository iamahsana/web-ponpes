import sqlite3

conn = sqlite3.connect('erp_pondok.db')
c = conn.cursor()

# Buat tabel user
c.execute('''
CREATE TABLE IF NOT EXISTS user (
    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    nama_lengkap TEXT NOT NULL,
    role TEXT NOT NULL,
    email TEXT,
    no_hp TEXT,
    is_active INTEGER DEFAULT 1,
    last_login TEXT
)
''')

# Buat tabel santri (contoh tambahan)
c.execute('''
CREATE TABLE IF NOT EXISTS santri (
    id_santri INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT,
    nis TEXT,
    tempat_lahir TEXT,
    tanggal_lahir TEXT,
    foto TEXT
)
''')

# Buat tabel settings
c.execute('''
CREATE TABLE IF NOT EXISTS settings (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    nama_pondok TEXT,
    alamat TEXT,
    kepala_pondok TEXT,
    moto TEXT,
    logo TEXT,
    tema TEXT,
    ukuran_upload INTEGER,
    format_santri TEXT,
    pagination INTEGER,
    tahun_ajaran TEXT,
    semester_mulai TEXT,
    semester_selesai TEXT,
    aktifkan_notif INTEGER,
    api_fonnte_1 TEXT,
    api_fonnte_2 TEXT,
    jadwal_kirim TEXT,
    template_pesan TEXT,
    jadwal_backup TEXT,
    durasi_backup INTEGER,
    timeout INTEGER
)
''')

conn.commit()
conn.close()
print("Tabel settings berhasil dibuat.")
