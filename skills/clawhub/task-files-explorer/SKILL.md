---
name: task-files-explorer
description: MANDATORY when the user wants to replace, bypass, or stop relying on the platform "All files in task" preview popup; when they want a custom HTML page (index.html) served on the platform preview URL; when they want a persistent file dashboard/explorer for download/ and archive/ served by a custom dev.sh; or when they ask how to make scripts survive container restarts via the /start.sh boot hook. Deploys a zero-dependency Python explorer to 127.0.0.1:3000 (the upstream of the preview ingress) with search, type filters, sorting, inline preview (md, images, pdf, json, text) and per-task grouping parsed automatically from worklog.md. Auto-starts on every container boot, self-heals every 30 seconds via watcher. NOT for Next.js/web-app projects - the web dev server always owns port 3000.
---

# Task Files Explorer — Pengganti Fungsional Popup "All files in task"

## 0. Kapan Skill Ini Dipakai / When to Use

Gunakan skill ini bila user (ID/EN):
- kesal dengan popup preview "All files in task" yang membuka semua tab sendiri, dan ingin penggantinya;
- meminta halaman web / index.html custom yang tampil di preview URL platform;
- ingin dashboard file persisten (download/ + archive/) yang hidup otomatis tiap boot;
- bertanya cara membuat skrip bertahan lintas restart container (via hook /start.sh).

**Jangan pakai** bila proyeknya aplikasi web interaktif (Next.js dsb.) — server web proyek
selalu lebih berhak atas port 3000; explorer otomatis berdiri down (guard ada di explorer.sh).

## 1. Arsitektur (Diverifikasi Empiris)

```
preview-<bot-id>.space-z.ai        (frontend platform — popup tinggal diabaikan)
  -> ingress platform :81          (reverse-proxy milik root, env FC_CUSTOM_LISTEN_PORT)
     -> 127.0.0.1:3000             (upstream — SISI KITA)
        -> explorer.py             (server stdlib Python, UI kreatif explorer-ui/index.html)
```

Fakta kunci yang membuat ini bisa bekerja:
1. Port 81 di container adalah ingress preview; saat upstream 3000 kosong ia menjawab
   502 halaman placeholder — begitu ada server di 3000, seluruh preview URL menampilkan
   server itu.
2. Popup "All files in task" adalah frontend browser platform — TIDAK bisa dimatikan dari
   container; yang bisa diganti adalah ISI preview URL. Strategi: popup diabaikan,
   explorer menjadi tujuan utama.
3. Proses biasa mati saat tool call selesai (platform membunuh pohon turunan PPID);
   satu-satunya cara daemon hidup terus = **double-fork orphan** (PPID=1 + setsid).

## 2. Langkah Deploy

### Kasus A — container baru (belum ada .zscripts/dev.sh)
1. Salin assets ke lokasi aktif:
   `mkdir -p ~/.zscripts/explorer-ui` (root proyek: /home/z/my-project)
   `cp assets/explorer.py assets/explorer.sh <proyek>/.zscripts/`
   `cp assets/explorer-ui/index.html <proyek>/.zscripts/explorer-ui/`
   `cp assets/dev.sh.template <proyek>/.zscripts/dev.sh && chmod +x <proyek>/.zscripts/dev.sh`
2. Jalankan sekali: `bash <proyek>/.zscripts/explorer.sh --ensure`
3. Mulai sekarang setiap boot container, /start.sh menjalankan dev.sh yang menghidupkan
   explorer + watcher (auto-heal) secara otomatis.

### Kasus B — dev.sh sudah ada (jangan ditimpa!)
1. Salin explorer.py, explorer.sh, explorer-ui/ seperti di atas.
2. Tambahkan blok berikut di akhir dev.sh (sebelum baris log terakhir):
   ```bash
   if [ -f "$PROJECT/.zscripts/explorer.sh" ]; then
       bash "$PROJECT/.zscripts/explorer.sh" --ensure >> "$BOOTLOG" 2>&1 || log "WARN: explorer gagal"
   fi
   ```
3. (Opsional tapi disarankan) tambahkan health-check 30 dtk di loop watcher — salin
   pola dari assets/dev.sh.template seksi 3-4.
4. Jalankan `bash .zscripts/explorer.sh --ensure`.

## 3. Aturan Konflik Port (WAJIB dihormati)

- `package.json` ada di root proyek -> Next.js pemilik :3000 -> explorer STAND-DOWN.
- Port 3000 dipakai proses lain yang bukan explorer -> explorer menolak start (log saja).
- Explorer bind 127.0.0.1 saja — tidak pernah expose langsung ke luar; akses luar
  selalu lewat ingress platform.

## 4. Lapisan Persistensi (kenapa tahan platform reset)

1. **repo.tar pre-stop** — platform mem-pack volume persisten sebelum stop; .zscripts/
   ikut ter-backup (terverifikasi: entri .zscripts ada di dalam tar).
2. **Hook /start.sh** — setiap boot menjalankan .zscripts/dev.sh bila ada.
3. **dev.sh v1.2** — memanggil explorer.sh --ensure + watcher.sh --ensure.
4. **watcher 30 dtk** — auto-heal bila explorer mati (terverifikasi empiris: kill -9 ->
   hidup lagi dalam <=30 dtk).
5. **M0 protokol memory** — tiap sesi baru memastikan watcher hidup.

## 5. Perintah Kontrol (untuk user)

```
bash .zscripts/explorer.sh --status   # kesehatan + log
bash .zscripts/explorer.sh --stop     # matikan explorer
bash .zscripts/explorer.sh --ensure   # hidupkan bila belum (idempoten)
bash .zscripts/watcher.sh --status    # status daemon auto-heal
```

## 6. Manifes File

| File | Peran |
|---|---|
| assets/explorer.py | Server stdlib (/, /api/files, /file/, /healthz) — ThreadingHTTPServer, guard path |
| assets/explorer.sh | Launcher --ensure/--status/--stop, guard Next.js, double-fork orphan |
| assets/explorer-ui/index.html | UI **Material Design 3 Expressive** (52 KB, zero-dependency): design token MD3 penuh light+dark (33 pasang kontras AA), type scale, shape morphing, wavy progress, ripple, state layer — fitur: stats, task rail (parse worklog.md), search, filter tipe, sort, grid/list, preview modal (md/json/img/pdf/teks), snackbar, tema gelap/terang, live refresh 10 dtk |
| assets/dev.sh.template | Template dev.sh v1.2 untuk container baru (boot hook + tidy + watcher + explorer) |

Semua nol dependensi eksternal: Python stdlib murni, HTML/CSS/JS vanilla, tanpa CDN.
