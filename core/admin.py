from django.contrib import admin

from core.models import User, Admin, Transaksi, Tiket, Pesawat, Penerbangan, Jadwal

@admin.register(Tiket)
class TiketAdmin(admin.ModelAdmin):
  pass

class TiketInline(admin.TabularInline):
  model = Tiket
  extra = 0

@admin.register(Jadwal)
class JadwalAdmin(admin.ModelAdmin):
  pass

class JadwalInline(admin.TabularInline):
  model = Jadwal
  extra = 0

@admin.register(Penerbangan)
class PenerbanganAdmin(admin.ModelAdmin):
  inlines = [TiketInline, JadwalInline]
  pass

class PenerbanganInline(admin.TabularInline):
  model = Penerbangan
  extra = 0

@admin.register(Pesawat)
class PesawatAdmin(admin.ModelAdmin):
  inlines = [PenerbanganInline]
  pass

@admin.register(Transaksi)
class TransaksiAdmin(admin.ModelAdmin):
  inlines = [TiketInline]
  pass

class TransaksiInline(admin.TabularInline):
  model = Transaksi
  extra = 0

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  inlines = [TransaksiInline]
  pass

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
  inlines = [TransaksiInline]
  pass

# Register your models here.
