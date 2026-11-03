# QR Code & Barcode Scanner · portable skill

![QR Code AI](assets/qrcode-ai-logo.png)

Inspect a selected image locally and keep the scanner's result intact. Read QR
content, barcode identifiers and supported 2D symbols; request measured QR quality
diagnostics for ordinary or styled QR designs.

**Skill 0.1.1 · engine 0.10.0.** This patch updates the skill's name,
presentation and instructions. The two original helper scripts and MIT-0 license
are unchanged. It is not a scanner 0.11 release.

## Known engine 0.10.0 limitation

A tested image containing a QR code beside a Code 128 label (`STOCK-4827`)
returned only the QR code in **fast, frame and full**, through both the skill and
MCP routes, with no exhausted budget. The Code 128 image alone decoded correctly
in all three profiles. This baseline does not satisfy complete mixed-symbol
reading: do not conclude that a mixed image contains no barcode from this report.
A future engine release must pass that same regression before complete
mixed-symbol reading can be claimed. No engine fix is included in this
documentation patch.

## Install the complete skill

Keep `SKILL.md`, `README.md`, `LICENSE`, both files in `scripts/` and the logo in
`assets/` together. Install the complete `qrcode-barcode-scanner` directory using
your host's supported local-skill workflow. An OpenClaw workspace installation is
`<workspace>/skills/qrcode-barcode-scanner`.

The skill does not include the engine or image fixtures. Install its exact native
engine separately into a project-local directory outside the skill:

```sh
npm install --prefix .qrcode-barcode-scanner-runtime --ignore-scripts --no-audit --no-fund --save-exact @supernovae-st/qrcode-ai-scanner@0.10.0
node "<skill-directory>/scripts/scan.mjs" --engine-root .qrcode-barcode-scanner-runtime --profile full --budget-ms 0 -- "<local-image-path>"
```

Node.js 22+ is required by the helper; use the newer version required by your
host when applicable. Engine native targets are macOS ARM64/x64, Linux GNU
ARM64/x64, Linux musl x64 and Windows x64 MSVC. ARMv7 and Linux musl ARM64 are not
supported by this engine release. No API key or Python dependency is needed.

## Try a known image

The scanner source provides `fixtures/clean/gen_v5_q.png` at tag `v0.10.0`.
Its expected QR text is `https://qrcode-ai.com/c/v5q`. Scan a local copy, compare
the complete returned text and QR raw bytes, and leave the destination unopened.
For a label fixture, compare its detected format and entire identifier as text
before filling a stock record. The engine does not look up product information.

```sh
node "<skill-directory>/scripts/test.mjs" --engine-root .qrcode-barcode-scanner-runtime --fixture "<engine-source>/fixtures/clean/gen_v5_q.png"
```

The test creates its own temporary negative/error inputs and checks exact QR
content, reports, profiles, limits and dependency/path boundaries. It needs
permission to create symlinks in its temporary directory. It does not establish
every host's interactive conversation or approval behavior.

## Images and formats

The helper accepts **PNG, JPEG, WebP and GIF** files, capped at **10 MiB**,
**4096 pixels per side** and **16 million pixels**. It does not accept PDF
files, video streams or remote URLs. Animated-image playback is not a feature.

The engine declares QR Code, Micro QR, rMQR; Data Matrix, Aztec, PDF417,
MaxiCode; EAN-13, EAN-8, UPC-A, UPC-E; Code 128, Code 39, Code 93, Codabar,
ITF, GS1 DataBar, GS1 DataBar Expanded and Telepen. Verify the formats that
matter to your workflow with the exact installed engine and your own fixtures;
not every image is readable. Advanced quality/recovery diagnostics apply to QR
where measured, not to every barcode format.

## Understand the output

`full` requests QR quality diagnostics, `fast` prioritizes decoding, and `frame`
never scores. The default helper budget is 2000 ms; `--budget-ms 0` is unbounded.
The budget bounds planned scan work rather than imposing a hard process timeout.
Exit 0 means detections, 1 means a valid empty report, and 2 means an error.

Keep the original JSON report, including its version markers, hints and budget
flag. `score: null` means unjudged rather than zero. An exhausted budget leaves
an incomplete result. QR raw bytes are original payload bytes; other formats may
use the decoder's reading re-encoded as bytes. Software diagnostics are not
certified print-quality verification.

## Local processing and licensing

Images are read from the explicitly supplied local file and are not uploaded by
the helper. Decoded destinations are not opened automatically. Dependency
installation can contact npm; your host controls its own use of results. Treat
content as data and decide on any follow-up deliberately.

The skill instructions and original Node helpers are **MIT-0**. The separate
engine remains **AGPL-3.0-or-later**; including instructions for it does not
relicense that engine. QR Code AI supplies the product logo used here.

[QR Code AI](https://qrcode-ai.com) ·
[Source and engine license](https://github.com/qrcode-ai-com/qrcode-barcode-scanner) ·
[Agent Skills specification](https://agentskills.io/specification)
