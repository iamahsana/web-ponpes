from models import db

class Santri(db.Model):
    __tablename__ = 'santri'

    id_santri = db.Column(db.Integer, primary_key=True)
    nis = db.Column(db.String)
    nama_lengkap = db.Column(db.String)
    tempat_lahir = db.Column(db.String)
    tanggal_lahir = db.Column(db.String)
    jenis_kelamin = db.Column(db.String)
    alamat = db.Column(db.String)
    no_hp = db.Column(db.String)
    wali_santri = db.Column(db.String)
    kelas = db.Column(db.String)
    kamar = db.Column(db.String)
    status = db.Column(db.String)
    tanggal_masuk = db.Column(db.String)
    foto = db.Column(db.String)
