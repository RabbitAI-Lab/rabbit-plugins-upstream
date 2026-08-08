---
name: scholar-search
description: "Search academic papers with Semantic Scholar and arXiv, dedupe results, and export JSON plus BibTeX citations for literature reviews, references, or citation gathering."
metadata:
  openclaw:
    emoji: "🔎"
---

# Scholar Search

Use this skill when the user asks to search for academic papers, gather references, build a literature review source list, or export citations without relying on a SerpAPI/Google Scholar key.

## Workflow

1. Install Python dependencies from the skill root when needed:

   ```bash
   python3 -m pip install -r {baseDir}/requirements.txt
   ```

2. Run the helper script from any working directory:

   ```bash
   python3 {baseDir}/scripts/search_papers.py "your search query" -o papers.json
   ```

3. Prefer the default `--engine both` unless the user asks for one source:
   - `semantic-scholar` has citation counts and venue metadata.
   - `arxiv` supports arXiv field prefixes such as `ti:`, `au:`, `abs:`, and `all:`.
   - `both` merges Semantic Scholar and arXiv results, keeping the Semantic Scholar copy when DOI, arXiv ID, or normalized title matches.

4. After the script finishes, report the absolute paths printed for the JSON and `.bib` outputs.

## Common Options

- `--max N`: total papers to collect, default `100`.
- `--offset N`: pagination offset.
- `--year Y` or `--year Y-Y`: filter by publication year or range.
- `--venue NAME`: exact Semantic Scholar venue filter.
- `--min-citations N`: keep papers with at least N citations when a citation count is available.
- `--sort-citations`: sort by citation count descending.
- `--no-cite`: skip DOI/arXiv citation lookups and generate BibTeX from metadata.
- `--bib-file PATH`: write BibTeX to a custom path; otherwise the `.bib` sits beside the JSON output.
- `--delay S`: seconds between API requests, default `1.0`.
- `--verbose`: print per-paper progress to stderr.

Example:

```bash
python3 {baseDir}/scripts/search_papers.py "large language models reasoning" \
  --max 50 --year 2020-2024 --min-citations 100 --bib-file refs.bib -o papers.json
```

## Output

The script writes a JSON file with `query`, `searched_at`, `count`, `engine`, and `results`. Each result includes title, authors, year, venue, journal/conference when available, citation count, URL, abstract, DOI, arXiv ID, BibTeX, and `bibtex_source`.

It also writes a combined `.bib` file on every run. Use the printed absolute paths when summarizing results for the user.

## Notes

- Set `SEMANTIC_SCHOLAR_API_KEY` for higher Semantic Scholar rate limits. The script still works without it, but shared keyless limits can be slow.
- Semantic Scholar queries are plain text; arXiv supports field prefixes.
- If API calls hit `429 Too Many Requests`, rerun with a higher `--delay` or ask the user to provide `SEMANTIC_SCHOLAR_API_KEY`.
- The script is read-only against external APIs and only writes the requested output files.
