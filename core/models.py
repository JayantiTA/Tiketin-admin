from django.db import models

class User(models.Model):
  user_id = models.IntegerField(primary_key=True)
  user_name = models.CharField(max_length=255)
  user_username = models.CharField(max_length=255)
  user_email = models.CharField(max_length=255)
  user_password = models.CharField(max_length=100)
  user_phone_number = models.CharField(max_length=15)

  class Meta:
    db_table = 'user'

class Admin(models.Model):
  admin_id = models.IntegerField(primary_key=True)
  admin_name = models.CharField(max_length=255)
  admin_email = models.CharField(max_length=255)
  admin_password = models.CharField(max_length=100)

  class Meta:
    db_table = 'admin'

class Transaksi(models.Model):
  transaksi_id = models.IntegerField(primary_key=True)
  transaksi_tanggal = models.DateTimeField()
  transaksi_biaya = models.FloatField()
  transaksi_dewasa = models.IntegerField()
  transaksi_anak = models.IntegerField()
  transaksi_status = models.BooleanField()
  user_user = models.ForeignKey(User, on_delete=models.CASCADE)
  admin_admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

  class Meta:
    db_table = 'transaksi'
    verbose_name_plural = 'Transaksi'

class Pesawat(models.Model):
  pesawat_id = models.CharField(max_length=4, primary_key=True)
  pesawat_kapasitas = models.IntegerField()
  pesawat_tipe = models.CharField(max_length=255)
  pesawat_perusahaan = models.CharField(max_length=255)

  class Meta:
    db_table = 'pesawat'
    verbose_name_plural = 'Pesawat'

class Penerbangan(models.Model):
  penerbangan_id = models.CharField(max_length=7, primary_key=True)
  penerbangan_asal = models.CharField(max_length=255)
  penerbangan_tujuan = models.CharField(max_length=255)
  pesawat_pesawat = models.ForeignKey(Pesawat, on_delete=models.CASCADE)

  class Meta:
    db_table = 'penerbangan'
    verbose_name_plural = 'Penerbangan'

class Tiket(models.Model):
  tiket_id = models.IntegerField(primary_key=True)
  tiket_seat = models.CharField(max_length=5)
  transaksi_transaksi = models.ForeignKey(Transaksi, on_delete=models.CASCADE)
  penerbangan_penerbangan = models.ForeignKey(Penerbangan, on_delete=models.CASCADE)

  class Meta:
    db_table = 'tiket'
    verbose_name_plural = 'Tiket'

class Jadwal(models.Model):
  jadwal_id = models.IntegerField(primary_key=True)
  jadwal_keberangkatan = models.DateTimeField()
  jadwal_kedatangan = models.DateTimeField()
  jadwal_slot_duduk = models.IntegerField()
  penerbangan_penerbangan = models.ForeignKey(Penerbangan, on_delete=models.CASCADE)

  class Meta:
    db_table = 'jadwal'
    verbose_name_plural = 'Jadwal'
# Create your models here.
