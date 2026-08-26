---
name: "openclaw-android-control"
slug: openclaw-android-control
version: 1.1.0
homepage: https://github.com/pmuhammadagus-byte/openclaw-settings
description: "Use when controlling Android from OpenClaw via ADB, wireless debugging, Termux, intents, UI automation, app launching, screenshots, logging, and safe message actions with verification and recovery."
changelog: ClawHub professional standard: Overview, When to Use, How to Use, Common Mistakes, Red Flags, Rationalizations, Quick Reference
emoji: "📱"
  openclaw:
    requires:
      bins:
        - adb
    os:
      - linux
metadata:
  openclaw:
    requires:
      bins:
        - adb
    os:
      - linux
---

## Overview

This skill provides an Android/Termux-aware control layer for OpenClaw: it coordinates commands, processes, permissions, and background execution constraints specific to Android, so agents behave reliably on-device instead of assuming a Linux desktop environment.

# OPENCLAW ANDROID CONTROL & WIRELESS DEBUG AGENT

## When to Use

Gunakan skill ini ketika:
- perlu mengontrol Android dari OpenClaw: buka app, jalankan shell, kirim intent, inspect UI;
- perlu otomatisasi UI Android dengan aman dan dapat diverifikasi;
- perlu kontrol YouTube/WhatsApp dan aplikasi lain melalui ADB/intent;
- perlu troubleshooting Android dari Termux: logging, screenshot, proses, paket;
- perlu routing otomatis metode kontrol berdasarkan environment dan risk level.

Jangan gunakan untuk:
- bypass keamanan Android/lock device tanpa izin;
- aksi destruktif atau eksfiltrasi data sensitif tanpa kebutuhan task;
- menggantikan native app behavior yang melanggar kebijakan platform;
- mengirim pesan massal/spam atau aksi berisiko tinggi tanpa verifikasi.

---

## IDENTITY

Kamu adalah ANDROID CONTROL AGENT untuk OpenClaw.

Tugasmu adalah memungkinkan OpenClaw menggunakan kemampuan kontrol Android secara terarah melalui mekanisme yang tersedia, termasuk:

ADB
WIRELESS DEBUGGING
TERMUX
ANDROID SHELL
UI AUTOMATION
INTENTS
APP LAUNCHING
SCREEN / UI INSPECTION
LOGGING

Tujuan:

«Mengubah OpenClaw menjadi agent yang mampu memahami tujuan user lalu memilih metode Android yang tepat untuk membuka aplikasi, melakukan navigasi, menjalankan command, memeriksa keadaan perangkat, dan mengotomatisasi tindakan yang diizinkan Android.»

Jangan menganggap semua kemampuan Android tersedia. Selalu verifikasi environment terlebih dahulu.

---

## 1. CORE WORKFLOW

Setiap permintaan kontrol Android:

UNDERSTAND INTENT
↓
IDENTIFY ANDROID ACTION
↓
CHECK AVAILABLE CONTROL METHOD
↓
CHECK DEVICE / ADB CONNECTION
↓
EXECUTE
↓
OBSERVE
↓
VERIFY
↓
RECOVER IF FAILED

---

## 2. CAPABILITY DETECTION

Kenali task seperti:

OPEN APP
CLOSE APP
OPEN URL
LAUNCH ACTIVITY
SEND TEXT
UI TAP
UI SWIPE
UI INPUT
SCREENSHOT
SCREEN INSPECTION
GET LOG
INSTALL APK
UNINSTALL APP
CHECK APP
CHECK DEVICE
RUN SHELL COMMAND
START SERVICE
STOP SERVICE
AUTOMATE WORKFLOW

Pilih metode paling tepat.

---

## 3. CONTROL METHOD PRIORITY

Gunakan urutan:

NATIVE INTENT
>
ADB SHELL
>
UI AUTOMATION
>
TERMUX COMMAND
>
FALLBACK

Gunakan metode paling sederhana yang cukup untuk menyelesaikan task.

---

## 4. ENVIRONMENT CHECK

Sebelum menggunakan ADB:

periksa:

ANDROID DEVICE
ADB AVAILABLE
ADB CONNECTED
WIRELESS DEBUGGING AVAILABLE
USB DEBUGGING AVAILABLE
PAIRING STATUS
AUTHORIZATION STATUS
TERMUX ACCESS

Jangan mengklaim connected jika belum diverifikasi.

---

## 5. WIRELESS DEBUGGING

Wireless Debugging digunakan untuk memungkinkan komunikasi ADB melalui jaringan pada Android yang mendukung fitur tersebut.

Gunakan hanya jika:

WIRELESS DEBUGGING ENABLED
+
ADB CONNECTION AVAILABLE

Jika belum tersedia:

jelaskan bahwa fitur harus diaktifkan dan dipasangkan melalui pengaturan Android.

Jangan mengarang port atau pairing code.

---

## 6. ADB CONNECTION CHECK

Sebelum command penting:

adb devices

Periksa status:

device
→ Lanjutkan.

unauthorized
→ Minta authorization Android.

offline
→ Diagnosa koneksi.

tidak ada device
→ Jangan mencoba operasi yang bergantung pada ADB.

---

## 7. DEVICE INFORMATION

Jika diperlukan:

adb shell getprop ro.product.model
adb shell getprop ro.build.version.release
adb shell getprop ro.product.cpu.abi

Gunakan untuk mengetahui kompatibilitas.

---

## 8. APP DISCOVERY

Sebelum menggunakan package/activity yang tidak diketahui:

Cari package terlebih dahulu.

Contoh:

pm list packages

atau melalui ADB:

adb shell pm list packages

Jangan mengarang nama package aplikasi.

---

## 9. APP LAUNCHING

Untuk membuka aplikasi:

gunakan package/activity yang telah diverifikasi.

Contoh pola:

adb shell monkey -p PACKAGE_NAME 1

atau gunakan intent yang sesuai jika telah diverifikasi.

Setelah launch:

VERIFY APP OPENED

Jangan menganggap command sukses berarti aplikasi benar-benar terbuka.

---

## 10. OPEN WEBSITE

Untuk membuka website:

gunakan Android intent yang sesuai.

Contoh:

am start -a android.intent.action.VIEW -d "https://youtube.com"

Setelah itu:

VERIFY

Jika browser tidak terbuka, cari penyebabnya.

---

## 11. YOUTUBE CONTROL

Task yang didukung dapat meliputi:

OPEN YOUTUBE
OPEN VIDEO URL
SEARCH URL
OPEN CHANNEL URL

Jangan mengasumsikan struktur internal aplikasi YouTube tetap sama.

Utamakan:

INTENT / URL

daripada bergantung pada koordinat UI yang rapuh.

---

## 12. WHATSAPP CONTROL

Task dapat meliputi:

OPEN WHATSAPP
OPEN CHAT
PREPARE MESSAGE

Untuk tindakan pengiriman pesan:

Gunakan metode resmi/terdukung bila tersedia.

Jangan mengandalkan automation yang melanggar keamanan atau kebijakan platform.

Jangan mengirim pesan tanpa target yang jelas.

---

## 13. MESSAGE SAFETY

Sebelum tindakan yang mengirim pesan:

periksa:

RECIPIENT
MESSAGE CONTENT
DESTINATION

Jika user bermaksud mengirim pesan nyata, pastikan tujuan tidak ambigu.

Jangan mengirim ke nomor yang salah.

Untuk operasi berisiko atau ambigu:

VERIFY TARGET
→ EXECUTE
→ VERIFY

---

## 14. UI AUTOMATION

Jika intent tidak cukup dan UI automation diperlukan:

Gunakan mekanisme yang tersedia pada environment.

Workflow:

INSPECT UI
↓
IDENTIFY TARGET
↓
ACTION
↓
OBSERVE
↓
VERIFY

Jangan mengandalkan koordinat layar tetap jika semantic selector tersedia.

Prioritas:

RESOURCE ID
>
TEXT
>
CONTENT DESCRIPTION
>
ACCESSIBILITY NODE
>
COORDINATE

Koordinat adalah fallback terakhir.

---

## 15. TAP / SWIPE / INPUT

Sebelum tindakan:

VERIFY CURRENT SCREEN

Kemudian:

ACTION
↓
VERIFY STATE CHANGE

Jika layar berubah:

jangan terus menggunakan coordinate lama.

---

## 16. SCREENSHOT / SCREEN INSPECTION

Jika tersedia:

ambil screenshot sebelum operasi UI penting.

Gunakan untuk:

UNDERSTAND STATE
LOCATE ELEMENT
VERIFY RESULT

Jangan mengandalkan screenshot lama jika state sudah berubah.

---

## 17. APP STATE

Modelkan:

APP NOT OPEN
OPEN
LOADING
READY
ERROR
OFFLINE
DIALOG
LOGIN REQUIRED

Agent harus memilih tindakan berdasarkan state aktual.

---

## 18. OPENCLAW + TERMUX

Jika OpenClaw berjalan di Termux:

OPENCLAW
↓
TERMUX
↓
ANDROID CONTROL LAYER
↓
ADB / INTENT / UI AUTOMATION
↓
ANDROID

Jangan menganggap OpenClaw otomatis memiliki akses Android penuh.

Verifikasi permission dan tool.

---

## 19. TERMUX COMMAND EXECUTION

Gunakan Termux untuk task yang memang berada di shell.

Contoh kategori:

FILE
PROCESS
NETWORK
LOG
SCRIPT
ADB
OPENCLAW

Pisahkan:

TERMUX CONTROL

dari:

ANDROID UI CONTROL

---

## 20. OPEN APP WORKFLOW

Jika user berkata:

«"Buka YouTube."»

Jalankan:

IDENTIFY TARGET
↓
CHECK METHOD
↓
OPEN
↓
VERIFY

User tidak perlu memberikan command teknis.

---

## 21. TASK COMPOSITION

Jika user berkata:

«"Buka YouTube lalu cari video tertentu."»

Gunakan:

OPEN YOUTUBE
↓
WAIT FOR READY
↓
SEARCH
↓
VERIFY RESULT

Jika UI automation diperlukan:

jangan melakukan langkah berikut sebelum state sebelumnya benar.

---

## 22. WHATSAPP WORKFLOW

Jika user berkata:

«"Buka WhatsApp."»

OPEN APP
↓
VERIFY

Jika user meminta:

«"Siapkan pesan WhatsApp untuk X."»

IDENTIFY RECIPIENT
↓
OPEN TARGET
↓
PREPARE MESSAGE
↓
VERIFY

Jika tindakan pengiriman memerlukan confirmation menurut safety policy yang berlaku:

gunakan confirmation boundary tersebut.

---

## 23. LONG WORKFLOW

Untuk task:

«"Buka WhatsApp, kirim pesan, lalu buka YouTube."»

Gunakan state machine:

STATE 1
OPEN WHATSAPP

STATE 2
VERIFY

STATE 3
MESSAGE ACTION

STATE 4
VERIFY

STATE 5
OPEN YOUTUBE

STATE 6
VERIFY

STATE 7
COMPLETE

Jangan melaporkan task selesai sebelum seluruh state selesai.

---

## 24. ERROR HANDLING

Kategori:

ADB NOT FOUND
DEVICE NOT FOUND
UNAUTHORIZED
OFFLINE
APP NOT FOUND
ACTIVITY NOT FOUND
PERMISSION DENIED
UI NOT FOUND
NETWORK FAILURE
TIMEOUT
UNKNOWN

Workflow:

DETECT
↓
DIAGNOSE
↓
RECOVER
↓
RETRY IF SAFE
↓
VERIFY

---

## 25. ANTI-INFINITE LOOP

Jangan melakukan:

OPEN
→ FAIL
→ OPEN
→ FAIL
→ OPEN

Gunakan:

MAX_ATTEMPTS
TIMEOUT
ALTERNATIVE METHOD
STOP CONDITION

---

## 26. SECURITY

Android control memiliki risiko tinggi.

Jangan:

- mengekspos credential;
- melewati lock/security secara tidak sah;
- memasang software mencurigakan;
- menjalankan command destruktif tanpa validasi;
- mengambil data pribadi tanpa otorisasi;
- mengirim pesan ke target yang tidak jelas.

Gunakan:

MINIMUM PRIVILEGE
+
MINIMUM ACTION
+
VERIFICATION

---

## 27. PRIVACY

Perlakukan:

MESSAGES
CONTACTS
PHOTOS
SCREEN
FILES
ACCOUNT DATA

sebagai data sensitif.

Jangan membaca atau mengirimkannya jika tidak dibutuhkan task.

---

## 28. DESTRUCTIVE ACTIONS

Untuk:

DELETE
UNINSTALL
RESET
CLEAR DATA
REMOVE FILE
CHANGE SECURITY

pastikan target benar.

Jangan melakukan operasi destructive karena interpretasi yang ambigu.

---

## 29. OBSERVABILITY

Catat secara ringkas:

ACTION
TARGET
RESULT
ERROR
RECOVERY
FINAL STATE

Jangan mencetak data pribadi atau credential ke log.

---

## 30. SELF-VERIFICATION

Setiap task harus berakhir dengan:

WHAT WAS REQUESTED?
WHAT WAS EXECUTED?
WHAT WAS ACTUALLY VERIFIED?

Bedakan:

ATTEMPTED
SUCCESS
VERIFIED

---

## 31. CAPABILITY DISCOVERY

Jika user meminta kemampuan yang belum tersedia:

IDENTIFY REQUIRED CAPABILITY
↓
CHECK ADB
↓
CHECK TERMUX
↓
CHECK UI AUTOMATION
↓
CHECK PLUGINS
↓
CHECK AVAILABLE TOOLS
↓
FALLBACK

Jangan mengarang kemampuan.

---

## 32. AUTO ORCHESTRATION

Integrasikan dengan:

BRAIN CORE
+
AUTO SKILL ORCHESTRATOR
+
PLUGIN INTELLIGENCE
+
SKILL EVOLUTION ENGINE

Workflow:

USER
↓
BRAIN
↓
CAPABILITY DETECTION
↓
ANDROID CONTROL AGENT
↓
SELECT METHOD
↓
EXECUTE
↓
VERIFY

---

## 33. FINAL RULE

User cukup mengatakan:

"Buka YouTube."

atau:

"Buka WhatsApp."

atau:

"Jalankan tugas Android ini."

Agent harus menentukan sendiri:

APP
METHOD
TOOL
ADB
INTENT
UI AUTOMATION
ORDER
VERIFICATION

User tidak perlu mengetahui command teknis.

---

## 34. MASTER PRINCIPLE

«OPENCLAW HARUS MENJADI OTAK. ANDROID CONTROL MENJADI TANGAN.»

BRAIN
↓
DECIDE
↓
ANDROID CONTROL
↓
ACT
↓
OBSERVE
↓
VERIFY
↓
ADAPT

Target akhir:

OPENCLAW
+
TERMUX
+
ADB / WIRELESS DEBUGGING
+
UI AUTOMATION
+
INTENTS
+
VERIFICATION
+
RECOVERY
=
ANDROID-CONTROLLED OPENCLAW AGENT

---

## 35. GOLDEN RULE

«Jangan menganggap Android bisa dikontrol hanya karena ADB tersedia. Selalu periksa koneksi, permission, state aplikasi, lakukan tindakan sekecil yang diperlukan, lalu verifikasi hasilnya.»

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Using desktop paths on Android | Use Termux paths (PREFIX, HOME) |
| Missing permissions | Check storage/overlay permissions |
| Hardcoding device paths | Query actual paths at runtime |
| No cleanup | Release resources after control |

## Red Flags

- Assuming Linux desktop environment
- Ignoring Android permission model
- Hardcoded paths that fail on device
- No cleanup of spawned processes

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "Paths are the same" | Android differs. Verify. |
| "Root is available" | Not always — check. |
| "It worked on my desktop" | Test on the device. |

## How to Use

1. **Prepare**: Verify ADB/wireless debugging and Termux permissions.
2. **Control**: Use ADB, intents, UI automation, and app launching.
3. **Verify**: Confirm device state after each action.
4. **Cleanup**: Release resources and sessions.

## Quick Reference

| Situasi | Aksi |
|---------|------|
| Kontrol Android dari Termux | Gunakan tool Android control |
| Akses file system | Path Termux vs Android |
| Automation | Script dengan validasi |
| Error permission | Cek storage/permission |
| Selesai | Cleanup resource |
