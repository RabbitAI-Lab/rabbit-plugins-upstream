# Downloading & Uploading Images from Source Articles

When the source article (blog, X/Twitter article, etc.) contains images that should appear
in the shownotes, download them and upload to TOS so the RSS feed references stable URLs
instead of the original CDN (which may require auth, proxies, or rate-limit).

## TOS path convention

```
podcasts/episodes/{slug}/images/{filename}.jpg
```

Each episode is a directory under `podcasts/episodes/` containing `podcast_{hash}.mp3`
(md5[:6] of file content, see SKILL.md), `script.md`, `notes.md`, and an optional
`images/` subdirectory.

## Workflow

1. Identify all image URLs in the source article
2. Download each image locally into an `images/` directory **next to the script.md you
   will pass to `--script`** (the publish script uploads `Path(--script).parent/images/`)
3. Upload to TOS at `podcasts/episodes/{slug}/images/{filename}`
4. Reference the TOS URL in `notes.md` using Markdown image syntax
5. Rebuild feed: regenerate description from notes.md -> update episodes.json + feed.xml

## Platform-specific gotchas

### X/Twitter Articles

X articles (long-form posts) embed images using **media IDs** (e.g. `2052726608751116288`),
NOT the `pbs.twimg.com/media/{id}.jpg` format. Constructing URLs from media IDs returns 404.

**Correct approach:**

1. Open the article page in the browser (`agent-browser open <url>`)
2. Wait for page load (~3s)
3. Extract all `<img>` srcs matching `pbs.twimg.com/media/`:

```javascript
// agent-browser eval --stdin
JSON.stringify(
  Array.from(document.querySelectorAll('img[src*="pbs.twimg.com"]'))
    .map(img => img.src)
    .filter(s => s.includes('media'))
)
```

4. The extracted URLs use the real media key format: `pbs.twimg.com/media/{key}?format=jpg&name=small`
5. Swap `name=small` for `name=medium` to get higher quality

### Downloading images through the browser

The gateway environment cannot `curl` `pbs.twimg.com` directly (connection timeout, no route).
Use `agent-browser eval` to fetch via the browser's authenticated session:

```bash
cat <<'EOF' | agent-browser eval --stdin 2>/dev/null | python3 -c "
import sys, base64
data = sys.stdin.read().strip()
if data.startswith('\"') and data.endswith('\"'):
    data = data[1:-1]
if len(data) > 1000:
    with open('filename.jpg', 'wb') as f:
        f.write(base64.b64decode(data))
    print('saved')
else:
    print(f'FAILED: {data[:200]}')
"
(async () => {
  const resp = await fetch('https://pbs.twimg.com/media/{KEY}?format=jpg&name=medium');
  const buf = await resp.arrayBuffer();
  const bytes = new Uint8Array(buf);
  let binary = '';
  for (let i = 0; i < bytes.length; i++) {
    binary += String.fromCharCode(bytes[i]);
  }
  return btoa(binary);
})()
EOF
```

Key points:
- Download **one image at a time** with a short sleep between - parallel fetches via
  `agent-browser eval` can silently return empty results
- Always check the saved file size > 0; a 0-byte file means the fetch failed
- The `2>/dev/null` suppresses agent-browser's status line; the Python one-liner handles
  base64 decode + file write

### Uploading to TOS

Publishing (`generate_podcast.py`) auto-uploads the local `images/` directory next to
`--script`. For images added AFTER publish, upload them individually:

```python
from tos_uploader import TOSUploader
uploader = TOSUploader()
url = uploader.upload_file(local_path, f'podcasts/episodes/{slug}/images/{filename}', content_type='image/jpeg')
```

### Rebuilding the feed after image updates

If notes.md is updated after the initial publish, rebuild with ONE command — never
reconstruct the feed with inline Python (it misses config values like cover_url;
that is exactly what SKILL.md's Key rule forbids):

```bash
python3 scripts/update_metadata.py --slug {slug} --notes notes.md
```

## Checklist

- [ ] Images downloaded to `podcasts/{slug}/images/`
- [ ] Images uploaded to TOS `podcasts/episodes/{slug}/images/`
- [ ] `notes.md` references TOS URLs (not source CDN URLs)
- [ ] `episodes.json` description regenerated from updated `notes.md`
- [ ] `feed.xml` re-uploaded
