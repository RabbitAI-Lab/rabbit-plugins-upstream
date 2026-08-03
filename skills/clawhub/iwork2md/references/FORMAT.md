# iWork File Format Reference (Pages / Numbers / Keynote)

This skill targets the **iWork '13+** format used by current Pages (.pages),
Numbers (.numbers) and Keynote (.key) documents.

## Physical layout

The document is a **bundle** = a ZIP archive containing:

```
MyDoc.pages/                (outer ZIP)
├── Index.zip               (all serialized objects, see below)
├── Data/                   (embedded media: images, video, etc.)
│   └── 143917994_2881x1992-small.jpg
├── Metadata/
│   ├── Properties.plist    (title / metadata)
│   ├── DocumentIdentifier
│   └── BuildVersionHistory.plist
├── preview.jpg             (preview thumbnails, top level)
├── preview-web.jpg
└── preview-micro.jpg
```

> Note: some iWork versions place the `.iwa` files **directly** under `Index/`
> inside the outer ZIP instead of inside a nested `Index.zip`. The parser
> (`iwa.open_iwa_sources`) handles both layouts.

## Index.zip -> .iwa

Inside `Index.zip` are many `.iwa` files (one or more per Component):
`Document.iwa`, `MasterSlide-1.iwa`, `CalculationEngine.iwa`, etc.

- The iWork ZIP writer uses **no compression** and no Zip64. Re-zipping with a
  normal tool can break the document, but reading is standard ZIP.

## .iwa = Protobuf stream wrapped in non-standard Snappy framing

### Snappy framing (iWork variant — NOT the official spec)

Back-to-back chunks:

```
[1 byte type][3-byte LE chunk length][length bytes data]
```

- iWork only emits **type 0x00** (compressed).
- It **omits** the mandatory stream-identifier chunk (`0xFF "sNaPpY"`).
- It **omits** the CRC-32C checksum that the official framing prepends to
  compressed data.
- For type 0x00, the chunk **data is a raw Snappy block** (starts with an
  uncompressed-length varint), not an officially-framed stream.

`iwa.iwa_unframe()` implements this exact variant.

### Raw Snappy block

```
varint uncompressed_length
<LZ77 stream: literals + back-references>
```

Elements start with a tag byte; lower 2 bits = type:
- `00` literal (len in upper 6 bits, or 1–4 follow bytes for len ≥ 61)
- `01` copy, 1-byte offset (len 4–11, offset 0–2047)
- `10` copy, 2-byte offset (len 1–64, offset 0–65535)
- `11` copy, 4-byte offset (len 1–64, offset 0–2^32)

`iwa.snappy_decompress()` implements the block format.

### Protobuf container stream (after unframing)

Objects are concatenated:

```
varint archive_info_len
ArchiveInfo {                      # message
  field 1: identifier (uint64)     # unique id across the document
  field 2: repeated MessageInfo
}
<for each MessageInfo, the payload bytes>
```

`MessageInfo`:
```
field 1: type    (uint32)  # selects the payload's protobuf schema
field 2: version (packed uint32)
field 3: length  (uint32)  # payload byte length
field 5: object_references (packed uint64)
field 6: data_references   (packed uint64)
```

`type` -> schema mapping (the **TSPRegistry**) is embedded inside the iWork
binaries and differs per app/version. Because Protobuf is not self-describing,
perfect decoding requires that map.

## What this skill does without the TSPRegistry

Protobuf string fields are stored as UTF-8, so a **generic walk** of the message
tree recovers essentially all human-readable text:

- Pages: body paragraphs, titles, headings, text boxes.
- Numbers: table cell text (each row serializes as `"a | b | c"`; the CLI
  reconstructs proper markdown tables), sheet/sheet-title names.
- Keynote: slide titles, body text, speaker notes, table text.
- All: embedded media inventory from `Data/`.

## Limits

- **Password-protected (encrypted) documents** use AES-128 + PKCS7 and cannot
  be read by this skill.
- Layout, fonts, colors, exact cell-merge geometry, shapes, and charts are
  *not* reconstructed — only textual content and table structure.
- For full structural fidelity, recover the `TSPRegistry` type map for the
  specific iWork version (see `obriensp/iWorkFileFormat` / `proto-dump`) and
  decode payloads per-schema. The generic walker is a reliable fallback that
  preserves 100% of readable text.
