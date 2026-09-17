# Task Files Explorer (Built-in Asset) — Referensi Deploy & Operasi

> Aset bawaan stellar-trail sejak v3.1.0 (server v1.1 + UI v2.2 sejak v3.3.0).
> Explorer adalah **alat opsional & opt-in** — bukan bagian dari mandat protokol.
> Ia menggantikan secara fungsional popup "All files in task" platform dengan
> halaman custom di preview URL.

## 0. Kapan Dipakai / When to Use

Gunakan bila user (ID/EN):
- ingin halaman web / index.html custom yang tampil di preview URL platform;
- ingin dashboard file persisten (download/ + archive/) yang hidup otomatis tiap boot;
- bertanya cara membuat skrip/servis bertahan lintas restart container (hook /start.sh).

**Jangan pakai** bila proyeknya aplikasi web interaktif (Next.js dsb.) — server web proyek
selalu lebih berhak atas port 3000; explorer otomatis berdiri down (guard ada di explorer.sh).

## 1. Arsitektur (diverifikasi empiris di platform container Z.ai)

```
preview-<bot-id>.space-z.ai        (frontend platform — popup tinggal diabaikan)
  -> ingress platform :81          (reverse-proxy, env FC_CUSTOM_LISTEN_PORT)
     -> 127.0.0.1:3000             (upstream — SISI KITA)
        -> explorer.py             (server stdlib Python; UI = explorer-ui/index.html, MD3 adaptif)
```

Fakta kunci:
1. Saat upstream :3000 kosong, ingress menjawab 502 placeholder; begitu ada server di 3000,
   seluruh preview URL menampilkan server itu.
2. Popup preview adalah frontend browser platform — tidak bisa dimatikan dari container;
   yang bisa diganti adalah ISI preview URL.
3. Proses biasa mati saat tool call selesai (platform membunuh pohon turunan);
   satu-satunya cara daemon hidup terus = **double-fork orphan** (PPID=1 + setsid).

## 2. Manifes File (assets/explorer/)

| File | Peran |
|------|-------|
| `explorer.py` | Server stdlib Python v1.1 (ThreadingHTTPServer); /api/files walk depth-4, parse task dari worklog.md, **blok skill guardian** (versi stellar-trail + heal terakhir + status watcher), serve file dgn guard path realpath (hanya dalam ROOTS) plus **`?dl=1`** untuk mode attachment (unduhan paksa); PIDFILE; env `STELLAR_PROJECT` (default /home/z/my-project), port via argv[1] (default 3000) |
| `explorer.sh` | Launcher --ensure/--status/--stop; guard Next.js (package.json menang); double-fork orphan; env `STELLAR_PROJECT` |
| `explorer-ui/index.html` | UI MD3 Expressive adaptif v2.2 (compact/medium/expanded/large/XL + landscape; list-detail ≥1240px; tema gelap/terang; zero-dependency) — fitur v2.2: kartu Guardian, quick-download per kartu, copy path, waktu relatif, refresh saat fokus, urut Terlama, pencarian menyertakan ID task |
| `dev.sh.template` | Template hook boot v2: tidy download/ -> archive/, fullstack guard, heal skill stellar-trail, ensure watcher + explorer, refresh repo.tar berkala |

## 3. Langkah Deploy

### Kasus A — container baru (belum ada .zscripts/dev.sh)
1. Salin aset ke lokasi aktif (root proyek default /home/z/my-project):
   `cp assets/explorer/explorer.py assets/explorer/explorer.sh <proyek>/.zscripts/`
   `mkdir -p <proyek>/.zscripts/explorer-ui && cp assets/explorer/explorer-ui/index.html <proyek>/.zscripts/explorer-ui/`
   `cp assets/explorer/dev.sh.template <proyek>/.zscripts/dev.sh && chmod +x <proyek>/.zscripts/dev.sh`
2. Jalankan sekali: `bash <proyek>/.zscripts/explorer.sh --ensure`
3. Setiap boot berikutnya, /start.sh menjalankan dev.sh -> explorer + watcher hidup otomatis.

### Kasus B — dev.sh sudah ada (JANGAN ditimpa)
1. Salin explorer.py, explorer.sh, explorer-ui/ seperti di atas.
2. Tambahkan blok ensure di akhir dev.sh:
   ```bash
   if [ -f "$PROJECT/.zscripts/explorer.sh" ]; then
       bash "$PROJECT/.zscripts/explorer.sh" --ensure >> "$BOOTLOG" 2>&1 || log "WARN: explorer gagal"
   fi
   ```
3. Jalankan `bash .zscripts/explorer.sh --ensure`.

## 4. Aturan Konflik Port (WAJIB dihormati)

- `package.json` ada di root proyek -> Next.js pemilik :3000 -> explorer STAND-DOWN.
- Port 3000 dipakai proses lain yang bukan explorer -> explorer menolak start (log saja).
- Explorer bind 127.0.0.1 saja — tidak pernah expose langsung ke luar; akses luar selalu
  lewat ingress platform.

## 5. Lapisan Persistensi

1. **repo.tar pre-stop** — platform mem-pack volume sebelum stop; .zscripts/ ikut ter-backup.
2. **Hook /start.sh** — tiap boot menjalankan dev.sh bila ada.
3. **dev.sh** — ensure explorer.sh + watcher.sh.
4. **watcher 30 dtk** — auto-heal bila explorer mati (terverifikasi: kill -9 -> hidup <=30 dtk).
5. **M0 protokol memory** — tiap sesi baru memastikan watcher hidup.
6. **Lapis anti-rollback** — bila lingkungan ter-reset: lihat `references/environment-resilience.md`
   + `scripts/snapshot-repo.sh` (satu masalah, satu keluarga solusi).

## 5b. Fitur v3.3.0 (server v1.1 + UI v2.2)

- **Kartu Guardian** (statistik ke-5): versi stellar-trail terinstal, indikator
  watcher hidup/mati, dan waktu heal terakhir — dibaca dari `_meta.json`,
  `watcher.pid`, dan marker `.skill-heal.last` (best-effort; kartu disembunyikan
  bila skill tidak terinstal).
- **Quick-download per kartu**: tombol unduh muncul saat hover/fokus pada tiap
  kartu file — memakai endpoint `?dl=1` (Content-Disposition: attachment) sehingga
  browser selalu mengunduh, bukan membuka. Tombol Unduh di dialog pratinjau kini
  juga memakai `?dl=1`.
- **Copy path**: tombol salin di dialog pratinjau menyalin path file lengkap di
  server (root + rel) ke clipboard — berguna untuk bekerja di terminal.
- **Waktu relatif** pada kartu ("baru saja", "5 mnt lalu", "3 jam lalu") dengan
  timestamp lengkap sebagai tooltip; dialog pratinjau tetap pakai timestamp penuh.
- **Refresh saat fokus**: data dimuat ulang seketika saat tab kembali aktif
  (visibilitychange) — di luar polling 10 detik reguler.
- **Urut Terlama** (mtime naik) + pencarian kini juga mencocokkan ID task
  (mis. query "27" menemukan file terkait Task 27).

## 6. Perintah Kontrol

```
bash .zscripts/explorer.sh --status   # kesehatan + log
bash .zscripts/explorer.sh --stop     # matikan explorer
bash .zscripts/explorer.sh --ensure   # hidupkan bila belum (idempoten)
```

**Etika & batasan:** explorer hanya melayani direktori kerja (ROOTS download/ + archive/),
read-only, bind loopback. Ia tidak pernah dipakai untuk mengekspos file di luar proyek,
dan deploy-nya selalu diberitahukan ke user (bukan inisiatif diam-diam) — konsisten dengan
prinsip consent seksi 4b dan intervensi-infrastruktur-hanya-atas-permintaan seksi 4c.
