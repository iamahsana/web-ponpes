import sqlite3

# Koneksi ke database (kalau belum ada akan dibuat)
conn = sqlite3.connect('erp_pondok.db')
c = conn.cursor()

# Buat tabel santri
c.execute('''
CREATE TABLE IF NOT EXISTS santri (
    id_santri INTEGER PRIMARY KEY AUTOINCREMENT,
    nis TEXT UNIQUE,
    nama_lengkap TEXT,
    tempat_lahir TEXT,
    tanggal_lahir TEXT,
    jenis_kelamin TEXT,
    alamat TEXT,
    no_hp TEXT,
    wali_santri TEXT,
    kelas TEXT,
    kamar TEXT,
    status TEXT,
    tanggal_masuk TEXT,
    foto TEXT
)
''')

# Buat tabel pembayaran
c.execute('''
CREATE TABLE IF NOT EXISTS pembayaran (
    id_pembayaran INTEGER PRIMARY KEY AUTOINCREMENT,
    id_santri INTEGER,
    jenis_pembayaran TEXT,
    bulan TEXT,
    tahun TEXT,
    nominal_tagihan REAL,
    nominal_dibayar REAL,
    tanggal_bayar TEXT,
    metode_bayar TEXT,
    status_bayar TEXT,
    kasir TEXT,
    catatan TEXT,
    FOREIGN KEY (id_santri) REFERENCES santri(id_santri)
)
''')

# Buat tabel transaksi umum
c.execute('''
CREATE TABLE IF NOT EXISTS transaksi_umum (
    id_transaksi INTEGER PRIMARY KEY AUTOINCREMENT,
    tanggal_transaksi TEXT,
    kategori_transaksi TEXT,
    jenis_transaksi TEXT,
    jumlah REAL,
    deskripsi TEXT,
    user_input TEXT
)
''')

# Buat tabel user
c.execute('''
CREATE TABLE IF NOT EXISTS user (
    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    nama_lengkap TEXT,
    role TEXT,
    email TEXT,
    no_hp TEXT,
    foto TEXT,
    last_login TEXT,
    is_active INTEGER
)
''')

# Buat tabel audit_log
c.execute('''
CREATE TABLE IF NOT EXISTS audit_log (
    id_log INTEGER PRIMARY KEY AUTOINCREMENT,
    id_user INTEGER,
    aksi TEXT,
    tabel_terpengaruh TEXT,
    id_data_terkait INTEGER,
    waktu_aksi TEXT,
    ip_address TEXT,
    FOREIGN KEY (id_user) REFERENCES user(id_user)
)
''')

# Buat tabel backup_log
c.execute('''
CREATE TABLE IF NOT EXISTS backup_log (
    id_backup INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_file TEXT,
    tanggal_backup TEXT,
    ukuran_file TEXT,
    lokasi_backup TEXT,
    backup_by INTEGER,
    FOREIGN KEY (backup_by) REFERENCES user(id_user)
)
''')

# Buat tabel surat
c.execute('''
CREATE TABLE IF NOT EXISTS surat (
    id_surat INTEGER PRIMARY KEY AUTOINCREMENT,
    jenis_surat TEXT,
    nomor_surat TEXT,
    perihal TEXT,
    isi_ringkasan TEXT,
    file_surat TEXT,
    tanggal_dibuat TEXT,
    dibuat_oleh INTEGER,
    FOREIGN KEY (dibuat_oleh) REFERENCES user(id_user)
)
''')

# Buat tabel alumni
c.execute('''
CREATE TABLE IF NOT EXISTS alumni (
    id_alumni INTEGER PRIMARY KEY AUTOINCREMENT,
    id_santri INTEGER,
    tahun_lulus TEXT,
    lanjut_studi TEXT,
    pekerjaan TEXT,
    kontak_alumni TEXT,
    FOREIGN KEY (id_santri) REFERENCES santri(id_santri)
)
''')

# Buat tabel kesehatan
c.execute('''
CREATE TABLE IF NOT EXISTS kesehatan (
    id_kesehatan INTEGER PRIMARY KEY AUTOINCREMENT,
    id_santri INTEGER,
    tanggal_periksa TEXT,
    keluhan TEXT,
    diagnosis TEXT,
    tindakan TEXT,
    petugas TEXT,
    FOREIGN KEY (id_santri) REFERENCES santri(id_santri)
)
''')

# Buat tabel hafalan
c.execute('''
CREATE TABLE IF NOT EXISTS hafalan (
    id_hafalan INTEGER PRIMARY KEY AUTOINCREMENT,
    id_santri INTEGER,
    tanggal_setor TEXT,
    juz TEXT,
    surat_mulai TEXT,
    surat_selesai TEXT,
    nilai_hafalan TEXT,
    FOREIGN KEY (id_santri) REFERENCES santri(id_santri)
)
''')

# Buat tabel kamar
c.execute('''
CREATE TABLE IF NOT EXISTS kamar (
    id_kamar INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_kamar TEXT,
    kapasitas INTEGER,
    wali_kamar TEXT
)
''')

# Buat tabel kantin_transaksi
c.execute('''
CREATE TABLE IF NOT EXISTS kantin_transaksi (
    id_kantin INTEGER PRIMARY KEY AUTOINCREMENT,
    tanggal TEXT,
    jenis_transaksi TEXT,
    barang TEXT,
    jumlah INTEGER,
    harga_satuan REAL,
    total REAL,
    kasir TEXT
)
''')

# Simpan perubahan dan tutup koneksi
conn.commit()
conn.close()

print("Database SQLite 'erp_pondok.db' berhasil dibuat!")
