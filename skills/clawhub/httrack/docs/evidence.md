# Evidence — httrack skill v2.0.0

Every flag this skill generates is traced to the HTTrack manpage (manpages.ubuntu.com,
man.archlinux.org, httrack.com man). Verified 2026-09-06. If a flag is not listed
here, the wrapper will not emit it — that is the anti-hallucination mechanism.

## Flag truth table used by this skill

| Flag | Manpage semantics (verbatim gloss) | Wrapper use |
|---|---|---|
| `-rN` (`--depth[=N]`) | set the mirror depth to N | bounding depth of `mirror`; `snapshot` fixes `-r1` |
| `-%eN` (`--ext-depth[=N]`) | external links depth (default %e0) | `snapshot` pins `-%e0` → never follow off-site |
| `-cN` (`--sockets[=N]`) | number of connections | polite default 2 |
| `-sN` (`--robots[=N]`) | 0=never, 1=sometimes, **2=always**, 3=always even strict | `--robots` (default **2**); ≥1 enforced by rule 2 |
| `-i` (`--continue`) | continue an interrupted mirror (cache-based update incl. `-i2` art) | `--resume` appends `-i` on the identical command |
| `-N` travel: `-a` (`--stay-on-same-address`) | restrict to the seeded address | pinned for both recipes (predictability) |
| `-n` (`--near`) | fetch non-html “near” files (assets outside the page’s dir) | `snapshot` pins it so CSS/JS/images survive |
| `+*/-*` scan rules | bare accept/reject filters | `--allow/--deny` → wrapper prefixes the sign itself |
| `-E<sec>` (`--max-time[=N]`) | maximum mirror time | `--max-time` |
| `-M<bytes>` (`--max-size[=N]`) | overall size ceiling | `--max-mb` |
| `-Q` / `-q` (`--do-not-log`/`--quiet`) | quiet modes | wrapper keeps output minimal; results come from the JSON report, not the log |

## Corrections vs v1.0.2 (each was a hallucinated/misdescribed row)

1. **`-Y` does NOT “update an existing mirror”.** Manpage: `-Y = --mirrorlinks`
   (mirror *all* links in pages). Update/continue is `-i` (`--continue`).
   v2.0.0 recipes use `-i` exclusively. (manpage Limits/Options list; ubuntu bionic man1)
2. **`-A "*.pdf,*.zip"` is not a file-type fetch filter.** `-A` alone is not an
   option; `-%A` is `--assume` (extension→MIME mapping, e.g.
   `-%A php3,cgi=text/html`). File-type selection is done with **scan rules**
   (`+*.pdf`), which v2.0.0 exposes as `--allow '*.pdf'`. (manpage Spider/typed list)
3. **`--robots=1` weakens robots compliance** (“sometimes”). Correct “obey
   robots.txt” is `-s2` (the tool's own default; 3 = even strict).
   (manpage `-sN` line)
4. **`-%v` is “display”** (echo filenames as downloaded), not “verbose”; `-v`
   is verbose log. The v1 quick-start glossed this as “verbose progress”.
   (manpage Log/index/cache section)
5. **`-cN` are sockets**, not “parallel connections” wording nit notwithstanding;
   v2 documents `--sockets`.

## Single-page recipe grounding

`httrack URL -O DIR -r1 -%e0 -n -a "-" -- "-* +*.css +*.js +img globs"` —
pattern endorsed by the official support forum (“only use scan rules, not
mirroring depth: `-*  +*.jpg +*.gif +*.css +*.js`”), Stack Overflow q/1968470
(depth 0/1 misses images; `-n`/--near grabs assets outside the directory) and
q/34796053 (GUI: max external depth = 0). v2 composes exactly this.

## Host-policy choices (SSRF hygiene)

- Loopback / link-local / private-IP **literals** (127.0.0.1, ::1, 10.0.0.0/8,
  172.16.0.0/12, 192.168.0.0/16, 169.254.0.0/16 …), `localhost`, userinfo
  (`user@host`) URLs, and whitespace in URLs are refused at the wrapper
  (exit 2); `--allow-private` is the deliberate opt-out for authorized LAN
  mirrors. DNS-name → private-IP rebinding (SSRFlite) is a documented residual
  risk: same-address travel (`-a`) limits off-host wandering, but HTTrack still
  follows redirects — treat mirrors of untrusted public URLs as untrusted data.
- Review attestation (2026-09-06, independent model): 10/13 truth-table rows
  above attested TRUE from model knowledge; rows 4/6/8 marked UNKNOWN by that
  reviewer — all three are pinned here to verbatim manpage text, which wins.

## Measurement choices (speed)

- Defaults chosen so the first run finishes quickly *and* safely: 2 sockets,
  bounded depth, same-address travel, wrapper suppresses httrack chatter and
  reports a single JSON object (agents do not read/scaffold around logs).
- Mirror result metrics (`files`, `bytes`, `html_pages`) come from walking the
  output directory — version-independent across HTTrack releases, unlike log
  parsing, which changes wording between 3.46/3.49 releases.
