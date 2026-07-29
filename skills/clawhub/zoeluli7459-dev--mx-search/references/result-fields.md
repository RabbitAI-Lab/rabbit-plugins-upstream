# mx-search Result Fields

Read this only when parsing raw `mx_search_*.json` or explaining result provenance.

## Common Fields

- `title`: source title or information title.
- `source` / `mediaName`: publisher or source name when present.
- `date` / `publishTime`: publication date.
- `secuList[]`: related securities.
- `secuList[].secuCode`: security code.
- `secuList[].secuName`: security name.
- `secuList[].secuType`: security type.
- `trunk`: core content text or structured content block.

## Source Handling

- Prefer official announcements, exchange disclosures, company filings, and policy texts for factual claims.
- Use research reports and media articles as opinion or interpretation unless they cite official documents.
- If multiple dates appear, distinguish publication date from event date.
- If `trunk` is short, inspect the saved JSON before concluding no evidence exists.
