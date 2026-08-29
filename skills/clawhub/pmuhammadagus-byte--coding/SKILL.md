---
name: coding
description: "Gunakan saat user meminta agent menerapkan konvensi gaya coding yang tertulis di file referensi milik user (mis. 'pakai gaya di file X', 'ikuti style guide saya')."
metadata:
  openclaw:
    version: 1.1.4
    author: pmuhammadagus-byte
    license: MIT
    maturity: stable
    quality: high
    tags: [coding, style-guide, reference]
author: pmuhammadagus-byte
license: MIT

---

# coding - Style Guide Reference Reader

## Purpose

Membantu agent menerapkan konvensi gaya coding yang **sudah tertulis** di file referensi milik user (contoh: `~/coding/style.md`). Agent membaca file itu **hanya saat user memintanya**, lalu menyesuaikan output kode. Agent tidak pernah membuat, mengubah, atau menyimpan file apa pun.

## When to Use

- User berkata: "pakai gaya di file X", "ikuti style guide saya", "terapkan konvensi di style.md".
- User ingin output kode mengikuti aturan tertentu yang sudah ia tulis sendiri.

Jangan gunakan untuk: mengambil keputusan gaya sendiri, atau mengubah file user tanpa permintaan eksplisit.

## Scope

This skill ONLY:
- Membaca file referensi gaya coding milik user saat diminta
- Menerapkan aturan yang tertulis di file tersebut ke output kode

This skill NEVER:
- Membaca project files untuk mencari "gaya" tanpa permintaan
- Membuat, mengubah, atau menyimpan file apa pun
- Mengirim data ke jaringan
- Membaca file di luar path yang user sebutkan

## Core Rules

### 1. Explicit Request Only
Agent membaca file referensi **hanya** jika user menyebutkan path atau meminta secara eksplisit. Jika user tidak menyebutkan file, agent bekerja dengan konvensi default tanpa mencari file sendiri.

### 2. Read-Only
Agent hanya membaca. Tidak pernah menulis, mengedit, atau membuat file - termasuk file SKILL.md ini.

### 3. User-Owned Data
File referensi adalah milik user. Agent tidak mengelola, memindahkan, atau mengarsipkannya.

### 4. No Inference
Agent tidak menyimpulkan "gaya user" dari observasi kode. Aturan diambil **hanya** dari file yang user sebutkan.

## Applying the Style

1. User menyebutkan file referensi -> agent membaca file tersebut
2. Agent merangkum aturan yang relevan secara singkat
3. Agent menerapkan ke output kode

Jika file tidak ada, agent memberitahu user dan lanjut dengan konvensi default.

## Security & Privacy

- Tidak ada penyimpanan state otomatis
- Tidak ada telemetri
- Agent tidak mengakses file di luar path yang user berikan

## Feedback

- If useful: `clawhub star coding`
- Stay updated: `clawhub sync`
