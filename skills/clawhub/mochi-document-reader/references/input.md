# Document request and response contract

## Requests

`read`: `file` is a relative path within the active workspace; optional `start` is a one-based line number (default 1); optional `limit` is 1..200 (default 60).

`search`: the same `file` and `limit`, plus a non-empty literal `query` up to 1000 characters. Matches are NFKC-normalized and case-insensitive. This is not regex search. No requestId is needed for these read operations.

Accepted files: UTF-8 .txt, .md, .csv, .tsv, .json and .log, maximum 2 MiB. File paths are at most 1000 characters. Absolute paths, parent traversal and symlinks are rejected. Convert PDF, Word or image content with a suitable host reader first, retaining original-page mapping.

## Success JSON

`ok: true`, `file`, `totalLines`, `matches`, `returned`, `truncated`, `lines` and `citationFormat`. Each line has `line` (one-based), `text` (at most 2000 characters) and `lineTruncated`. For read, matches is the number of lines from start through EOF; for search it is the total literal matches before limiting. `truncated` indicates additional matching lines, while `lineTruncated` identifies an individually shortened line. A search with no match returns an empty lines array.

## Errors and interpretation

CLI errors return `ok: false` with `error` to stderr and exit code 1. Correct the file, encoding, size or request rather than treating an error as document evidence. The citationFormat field suggests `file:LINE`; every factual answer still needs its actual supporting line or mapped original page. The sample notice is fictional and has three content lines plus a trailing newline. Read/search does not change source bytes or save a final Markdown report.
