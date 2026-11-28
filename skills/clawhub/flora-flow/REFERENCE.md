# Flora Flow: reference

Read this only for `--detail`, after an error, or when `quick` is not enough. The steps for the usual case are in SKILL.md.
The step-by-step tools are only for when `quick` fails or the user names a box.

The user is at a flower market. Usually they have already set their heart on one or two flowers and want to know
what to buy with them; often they send several photos (a few stalls, or a close-up plus wider shots).

1. **Scan** every photo. The server marks the flowers it finds with numbered boxes.
2. **Anchor.** Work out which boxes are the flowers the user has in mind: the *anchors*.
3. **Find pairings.** The server returns reference arrangements that use the anchors, and for each one says which
   other boxes in the photos look like the rest of its flowers: a shopping list.
4. **Adjust** in conversation: "plainer", "no lilies", "one kind less".

The server only detects and matches by appearance. **You** identify the flowers by looking, map the user's words to
boxes, judge which plans suit them, and explain how to put the flowers together. The server generates no images and
gives no design advice.

There are two ways to work. **MCP tools** (section 2) need no shell commands; use them when they are available.
**The script** `scripts/flora.py` (section 6) does the same through shell commands and is the fallback.

## 1. Are the MCP tools available?

Look in your tool list for `quick_pairings`, `scan_photo`, `scan_status`, `find_pairings`, usually under a server
prefix such as `flora-flow` (for example `mcp__flora-flow__scan_photo`). `quick_pairings` is the fast path above.

- **`scan_photo` present:** use `quick_pairings` first (fast path); for more control, work as in section 2.
- **Only `scan_status` and `find_pairings`:** the host uses the remote endpoint, which cannot read files on this
  computer. Upload the photos with the script (`flora.py scan`), do the rest with the tools.
- **None present:** use the script (section 6); everything works with it. At the end of your reply, offer the
  one-time setup below in one line; go through its steps only if the user says yes.

### One-time setup (the user does it)

1. Run `python3 <this skill folder>/scripts/flora.py mcp-config` (Windows: `python`). It prints a JSON block and
   makes no network call.
2. Ask the user to add the `flora-flow` entry to the `mcpServers` section of the agent's MCP settings and restart
   the agent. Edit the host's configuration yourself only if the user asks you to. (If `FLORA_FLOW_SERVER` or
   `FLORA_FLOW_HOME` is set in your environment, the printed entry carries it along.) A host with another
   settings format takes the same `command`, `args` and `env`; Codex, for example, keeps them in a
   `[mcp_servers.flora-flow]` table in `~/.codex/config.toml`.

`flora.py mcp-config --remote` prints the server's own endpoint instead (a URL that contains the user ID). Use it
only for hosts that cannot run local commands. It has no `scan_photo`, and the URL is a credential.

## 2. The flow with MCP tools

Use `quick_pairings` first (fast path). The steps below are for when it fails or the user names a box.

Every result has a text part, a `structuredContent` object and usually pictures. An error comes back as a result
with `isError: true` whose text says what happened and what to do next. Do that; don't work around it with HTTP
calls of your own.

1. **`scan_photo`** `{"path": "/absolute/path/photo.jpg"}`, once per photo (JPEG, PNG, WebP, HEIC; 25 MB). Number
   the photos in the order you scan them (photo 1, photo 2, ...) and keep each `scan_id`. Each call waits up to
   45 s. If `status` comes back as `queued`, `starting_gpu` or `detecting`, do not upload again: call
   **`scan_status`** `{"scan_id": "...", "wait_s": 50}` until it is `done` or `failed`. A cold GPU takes about two
   minutes to start; tell the user it is warming up instead of going silent. If `status` is `failed`, tell the
   user `error.message` and upload that photo once more; if it fails again, go on without it.
2. **Look at the pictures** of every scan: the **overview** (the photo with every `box_id` drawn on it) and the
   **contact sheet** of the crops. `boxes[]` lists `box_id`, `label`, `label_en`, `generic`, `score`, and `box` =
   `[x, y, w, h]` in percent of the photo. The pictures show what each box holds; the labels mostly do not
   (section 3).
3. **Tell the user** what section 7 requires: where the photos went (said before the first upload) and, when a
   result has `user_id_created: true`, that an ID was created.
4. **Work out the anchors** (section 3).
5. **`find_pairings`** with all the `scan_ids`, the anchors, and what the user does not want (sections 3 and 5).
6. **Present the plans** (section 4) and give the user `page_url`, a page with the plans and the numbered photos
   that they can open themselves.

## 3. Anchors: the flowers the user has in mind

```
find_pairings {
  "scan_ids": ["s...1", "s...2", "s...3"],            the photos of this visit, always in the same order
  "anchors":  [{"scan_id": "s...1", "box_id": 6},     a box
               {"scan_id": "s...4", "box_id": null}]  a whole photo: a close-up of one flower
}
```

- **`scan_ids`** are the photos whose flowers can be bought: 1 to 8. Results name a flower as `photo_index`
  (position in `scan_ids`, from 1) plus `box_id`, so keep the order the same in every call of this conversation.
- **How the user points at a flower, and what you do:**
  - *A number* ("the 6 in the first photo"): use that box.
  - *A description* ("第二张里那桶粉色的", "左边那桶蓝的"): look at the overviews of all photos and find
    the box that shows it. When several boxes show the same bucket or the same flower, take the one that the flower
    fills best, sharp and well lit; one box per flower is enough.
  - *A close-up photo* of the flower: scan it and use `{"scan_id": ..., "box_id": null}`, the whole photo. Put a
    close-up into `scan_ids` too only if it was taken at the market; a photo of flowers the user already has at
    home is an anchor but not something to buy from.
  - *Nothing in particular* ("what could I make from this stall?"): call without `anchors`. The works are then
    ranked by how much of them the stalls can supply.
- **Not sure which flower they mean?** Ask in one line, in their terms: which photo, what colour, where in the picture
  (left, front, the bucket next to the sunflowers), or a close-up photo of it. Never ask for its name or a box number.
- **Up to 5 anchors.** One or two sure ones beat five guesses: a plan is preferred when it uses all the anchors.
- **Never choose by the labels.** The boxes are placed well; the labels are not reliable. `label` is the
  detector's guess among 17 classes, and most of the time it is wrong or says nothing: in a first check on real
  market photos, about four boxes in five were labelled only "flower" (`generic: true`), and most of the specific
  names were wrong (lisianthus and roses often came back as "peony"). To know what a flower is, look at the
  overview and the crops and decide for yourself; tell the user what *you* think it is, and say so when you are
  not sure.
- **No GPU is needed** for a call without `query_en`, so it answers at once even when the GPU is asleep.
- `box_id`s must come from the scans; you cannot draw your own boxes.

## 4. Presenting the plans

`plans[]` come best first, 3 by default (`top_k` 1 to 6). A work is only offered when the stalls supply at least 2 of
its kinds of flowers, so there may be fewer plans than asked, or none: then say that these photos do not have enough to
go with it, and suggest more stalls or naming the flower they like.

Each plan is one reference work, shown as a **comparison card** (one picture per plan is attached; the result page has
them too). Each row of the card is one flower of the work:

| Field | Meaning |
|---|---|
| `card[]` | `row`, `work` (the work's flower: name · colour · part from the gallery annotation, or 未标注; the part is 主角 / 显眼配角 / 点缀 in newer annotations, 主花 / 配花 / 线条 / 叶材 in older ones), `anchor` (true: the user's flower), `market[]` (`photo_index`, `box_id` of the matched box, `checked` = whether its kind was checked; empty = not found in the market), `lookalike` (when not empty: the nearest box was judged a different kind, `likely_name_zh` = what it looks more like; grey frame and "alt" on the card) |
| `buy_zh` | The shopping list by name, with where on the stalls |
| `materials` | Flowers of the work that have no row (no crop of their own): they need buying too, from another stall |
| `annotation_status` | `unlabelled`: the work has no names yet; describe its flowers from the card picture |
| `work_id`, `image_url`, `card_url`, `not_found` | The work, its picture, the card picture, how many rows have no market box. Script: `card_image` is the card on disk (the quick path saves the cards of every plan) |

The other fields (`anchor_matches`, `shopping`, `buy_groups`, the scores, ...) are the server's working data.

- **Names are of the work's flowers.** The market box was matched by appearance, so it may be a different flower
  that looks alike. Look at its picture on the card (right side) before you tell the user what it is.
- **"图库里目前没找到用这种花的参考作品"** (the gallery has no reliable reference with the user's flower so far): say so
  plainly, and that the gallery is growing; the plans then go by the other flowers on the stalls and do not use theirs, so
  never present them as "with your flower". Offer to try another flower they like. "还不能确认有…可靠参考": the pairing may be off; say so.
- **Four kinds of rows:** found and checked to be the same kind (a box to buy); found but **未核对是否同种** (no check ran:
  the work has no names yet, or this photo has no vectors for the check): it is on the shopping list, but look at the box
  on the card yourself and tell the user to check before buying; `lookalike` ("摊上有长得像的…，不是同一种": never list it
  as something to buy; you may offer it as a stand-in and say it is a different flower); and not found.
- **No colours from the boxes.** A box's colour is not reliable (it takes in wrapping and leaves); say colours only
  from the annotation (the work) or from what you see.
- **Never give the user the numbered stall photos** (overview pictures with 20 boxes), and never list or group box
  numbers for them ("1 号…20 号", boxes sorted by colour). Say where a flower is by photo and position: "第 2 张照片右下那桶粉色的".
- **What the user gets: the result, not the evidence.** The fast path already gives it (one picture, one line, the
  page): pass it on as it is. When you answer from step-by-step results or `--detail`, keep the
  same shape: the work's picture and one sentence, then one line per flower: name + colour + which photo and where in
  it (the output gives the position words). Since 0.8 the server's list already has this shape: pass its lines on as
  printed. Numbered lines (①②…) are the boxes on the picture: 「去买」 = solid box, checked to be the same kind;
  「…颜色相近（作品里是X色），到摊上确认」 = orange dashed box, colour to be checked at the stall;
  「…品种待核，到摊上确认」 = gray dashed box: the place is kept, but the kind is not confirmed, so it is **not** 去买.
  Lines starting 「·」 have no box (another colour, an accent flower 「作品里还用了这种花点缀」, 「没法确认是同一种」): say
  them, never as something to buy. A work whose chat line says
  「最接近的一件」 does not have the user's flower; don't present that bunch as part of it. Last line: the /skill/f/
  page, 「想看别的方案」. The
  comparison cards, box numbers and P-codes (P5-7 = photo 5, box 7) are only for you; never paste or show them to the user.
- **Be honest about gaps**: rows with no market box, `materials`, and anything else the work picture shows that was
  not found (greenery most often). Say 「这次照片里没定位到」, never 「摊上没有」: the photos may simply not show it.
  Suggest a stand-in, more photos or another stall.
- **Similarity and score only rank.** They are not percentages. Don't quote them.
- **Then do your own part:** which plan suits the wish best and why, roughly in what proportions, how to arrange it.
  The server gives no stem counts; any quantity is your suggestion, and say so.

## 5. Adjusting

The user answers in words; you turn them into the next call. Keep `scan_ids` and the anchors in the same order.

| The user says | What you change |
|---|---|
| "要更素一点", "more romantic", an occasion | Don't hold the search for a flower: with none picked, run it as it is and offer at the end to build on one. Add `query_en`: a short, concrete description in English of the look ("understated, muted colours, lots of green"). The server does not translate. Pass the user's own words as `query` (recorded only). This needs the GPU. The sentence re-orders only plans that suit the anchors about equally well; it never trades the flower the user likes for a style. So the same works may come back in a new order. If none of them has the look, say so and offer other anchors or more plans (`top_k`). |
| "不要粉色的", "nothing orange" | Exclude the colour: `"exclude": {"colors": ["pink"]}` (pink, red, orange, yellow, green, blue, purple, brown, white, gray, black; up to 3). Or point at boxes that show it: `"exclude": {"refs": [{"scan_id", "box_id"}]}` (up to 2); their main colour is used and they are not offered to buy. Works where that colour covers a sizeable patch of a flower are left out. Small touches can remain, so still look at every plan and drop one that plainly has the colour. |
| "不要百合", "no roses" | **Not supported yet.** Send it as `"exclude": {"species": ["lily"]}`: you get the error `exclude_species_unsupported` and nothing is counted. Tell the user that leaving out a kind of flower is not possible yet. Don't swap in a colour on your own (white lilies are not "no white"); ask whether a colour is what they mean, or search without it and leave out by eye the plans that show that flower. |
| "预算少买一种", "simpler" | No parameter for this: drop the least important flower from the plan yourself (a 点缀 or a filler before the main flowers) and say what you dropped. |
| "还有别的吗" | Raise `top_k` (up to 6), or change the anchors. |
| "其实我更想要这个" | Change the anchors. |

Every call that returns plans counts against the daily limit (300), so decide what to change before calling.

**`gpu_starting`** (only with `query_en`): the GPU was asleep. Call again with the same arguments after
`retry_after_s`; tell the user it is warming up. It did not count against the daily limit.

**An error that names a `scan_id`** means that photo is not finished, failed, or was deleted after 7 days. Wait
for it, upload it again, or leave it out, then call again.

## 6. Script fallback

Python 3.8+, standard library only, nothing to install.

```
python3 <this skill folder>/scripts/flora.py <command> [options] [arguments]
```

On Windows use `python` or `py -3`. Always call it as one plain command (no `cd`, pipes, `&&`, `; echo $?` or
environment prefix), so the user can approve `python3 <path>/flora.py` once. It needs to run, to reach the server
host shown by `flora.py whoami` (the pictures of the works come from the same host), and to read/write
`~/.flora-flow/`. The two environment variables are for the user to set in their shell or MCP settings; you
normally never set them.

First always `quick` (SKILL.md). A typical step-by-step run, only when that is not enough:

```
python3 <skill>/scripts/flora.py scan /path/to/stall1.jpg
python3 <skill>/scripts/flora.py scan /path/to/stall2.jpg
    -> each RESULT has scan_id, box_ids and overview_image: open the pictures, work out the anchors (section 3)
python3 <skill>/scripts/flora.py pair <scan_id_1> <scan_id_2> --anchor 1:6
    -> RESULT has plans[] with local_image, uses[] and buy[]: open the pictures, then advise the user (section 4)
python3 <skill>/scripts/flora.py pair <scan_id_1> <scan_id_2> --anchor 1:6 --exclude-color pink --query-en "understated, muted colours" --query "要更素一点"
    -> an adjusted search (section 5)
```

`--anchor PHOTO:BOX` and `--exclude PHOTO:BOX` name a box by the photo's position among the scan IDs: `1:6` is box
6 of the first scan ID. `2:all` is the whole second photo (a close-up). For a photo that is not in the list (flowers
already bought), write its scan ID instead of the number: `--anchor <scan_id>:all`. Repeat `--anchor` for up to 5.
`--exclude-color NAME` leaves out a colour (repeat for up to 3); `--exclude PHOTO:BOX` a colour shown by a box (up
to 2); `--exclude-species NAME` is not supported yet and ends with the error `exclude_species_unsupported`.

If `scan` exits with 3, run `flora.py status --wait 300` until it exits 0, then go on.

Everything in sections 2 to 5 and 7 about what to do between and after the commands applies here too: look at
the overview pictures before choosing anchors, give the user `page_url`, tell them about the upload and a newly
created ID (`user_id_created`), look at the pictures of the works before describing them.

| Command | What it does |
|---|---|
| `quick PHOTO... [--flower NAME] [--flower-color COLOR] [--flower-photo N] [--say TEXT] [--style-en TEXT] [--exclude-color COLOR]... [--anchor P:B]... [--wait SECONDS] [--another] [--detail]` | The fast path (SKILL.md): shrinks big photos, uploads them together, waits, returns one work as one picture (market left, work right) and one line. `--another`: the next work of the same result (no new search). `--detail` (only when the user asks why): the candidates A/B/C, every plan and its comparison card. Run again with the same arguments to continue; uploaded photos are not sent twice. |
| `scan [--no-wait] [--wait SECONDS] PHOTO` | Uploads one photo, waits up to 300 s (default) and saves the result with the overview picture and contact sheet. |
| `status [--wait SECONDS] [SCAN_ID]` | Checks the pending scans (or the given one) once, or keeps polling up to SECONDS. With nothing pending it lists the recent scans. |
| `pair SCAN_ID [SCAN_ID ...] [--anchor P:B]... [--exclude-color NAME]... [--exclude P:B]... [--query-en TEXT] [--query TEXT] [--top-k N] [--wait SECONDS] [--no-images]` | Finds the plans and downloads the pictures of the works. With `--query-en` it retries by itself for up to 240 s (default) while the GPU starts. |
| `whoami` | Shows the user ID, server and local folder. No network. |
| `mcp-config [--remote]` | Prints the JSON for the MCP setup (section 1). |
| `mcp` | The MCP bridge itself. The agent host runs it; don't run it yourself. |

| Exit | Meaning |
|---|---|
| 0 | Done: the scan finished, or the plans were found |
| 3 | Still running: the scan is not finished, or the GPU is still starting. Run `status --wait 300` (or the same `pair` again) |
| 1 | Error: read the `ERROR:` line. Also when the scan itself failed (`status: "failed"`, a `FAILED` line with the reason): upload once more |
| 2 | Usage error: bad arguments, a missing or oversized file |

The last output line is `RESULT {...}`, one line of JSON (`mcp-config` and `mcp` print none). Take the outcome
from it rather than from the text above: every RESULT has `exit_code` (no need to capture it from the shell),
`command` and `errors[]` (`code` and `message` of what went wrong, `scan_id` when one photo is the problem), and
all but an early failure have `user_id`.

- **Quick:** `status` (`done`, `starting_gpu`, `running`), `scan_ids`, `photos[]`, `pictures` (the local picture(s) to
  send, in order), `line_zh`, `work_id`, `rank`, `shown` / `more` (how many works shown so far, whether 换一个 has another),
  `results[]` (all works of this result, up to 3: `work_id`, `image_url`, `pair_image_url`, `line_zh`, `sentence_zh`,
  `buy_images[]`, `shopping_zh[]` the numbered list, for the page and for answering questions), `page_url`, `note`. With `--detail` instead: `pictures` (the A/B/C picture, then the cards) and
  `groups[]` (`label`, `anchor`, `summary_zh`, `page_url`, `plans[]` with `card` rows, `buy_zh`, `card_url`).
- **Scan:** `scan_id`, `status`, `boxes` (a count), `box_ids`, `notice`, `error`, `duplicate`, `expired`,
  `page_url`, `overview_image` and `sheet_image` (local paths: open them to see the boxes), `scan_file`,
  `user_id_created`, `pending_scan_ids`. The label guess, score and position of each box are in the `box N:`
  lines of the text and, in full, in `scan_file`.
- **Pair:** `find_id`, `scan_ids`, `anchors`, `exclude` (`colors`, `refs`), `excluded_colors` (the colours actually
  left out, in English), `used` (`query_en`, `top_k`), `plans[]`, `pairing_file`
  (the full result), `page_url`, `finds_left_today`. Each plan: `rank`, `work_id`, `image_url`, `local_image`,
  `score`, `uses[]` (the anchors it uses: `photo_index`, `scan_id`, `box_id`, `similarity`), `unused_anchors[]`,
  `buy[]` (one entry per group: the best box with `photo_index`, `scan_id`, `box_id`, `similarity`, and
  `look_alikes[]`, the other boxes of the group), `not_found` and `indexed_instances` (section 4), `base_rank`. A
  pair result has no `status`:
  exit code 0 means the plans are there. If `--wait` runs out while the GPU starts, it exits 3 with
  `gpu_starting` in `errors[]`, and the same command can simply be run again.

If your shell tool times out before `--wait` ends, nothing is lost: the scan ID is saved first, and the next
`status` picks it up. Don't call the server with curl or code of your own.

## 7. Rules

- **Relay notices verbatim**, translated faithfully into the user's language. `no_flowers` means nothing was
  detected in that photo: pass on its advice.
- **A label is not a flower name.** Never tell the user that a box "is" what its label says, and don't list the
  labels as what was found: they are usually wrong (section 3). Name flowers from what you see in the pictures,
  as your own reading. If you cannot view images, say that you cannot tell which flowers they are.
- **Never describe a picture you have not seen**, and never invent a reference work's contents.
- **Similarities and scores are not percentages.**
- **One photo per scan.** The same file uploaded again returns the earlier result (`duplicate`), without
  counting against the limit.
- **Limits per user ID per day:** 60 photos, 300 searches. If a limit is hit, tell the user; don't create a new ID.
- **The user ID is a credential.** Anyone with it can read this user's scans. `page_url` and the links to the
  user's own pictures (photo, overview, crops) contain an unguessable ID and open without a login: give them
  to the user only, never post them publicly. The gallery pictures (`image_url` of a work) are public.
  Never delete or replace `~/.flora-flow/user.json`. If the server does not recognise the ID, tell the user.
- **A new ID:** the first scan creates the ID (`user_id_created: true`). Tell the user once, in the reply that
  reports the scans: an ID was created and saved in `~/.flora-flow/user.json` (or the path the tool or script
  printed, when `FLORA_FLOW_HOME` is set), and it works like a password for their scans. You need not print the
  ID itself.
- **Privacy:** the photos are stored on the server, with location data and other metadata removed, and deleted
  after 7 days. Upload at once and don't announce it (the user asked for the photos to be analysed); if the user asks
  what happens to their photos, say so truthfully, and stop if they object. After 7 days a scan can no longer be
  used (`expired`): upload the photo again.
- **Blocked network:** if a command says the server cannot be reached or that something else answered, a
  sandbox, proxy or firewall is in the way. Ask the user to allow the server's host, then run the same command
  again.
- **Photo advice** when detection is poor: closer, in good light, flowers filling the frame, one stall per photo
  rather than the whole hall.

## 8. Files in `~/.flora-flow/`

| File | Content |
|---|---|
| `user.json` | `{"user_id", "server", "created_at"}` |
| `pending.json` | `{"scan_ids": [...]}`: uploaded, result not collected yet |
| `scans/<scan_id>/scan.json` | The scan: `status`, `photo`, `boxes[]` (`box_id`, `label`, `label_en`, `generic`, `score`, `box`, `crop_url`), `notice`, `page_url`, `expires_at` |
| `scans/<scan_id>/overview.jpg`, `sheet.jpg` | The numbered photo and the contact sheet of the crops |
| `pairings/<find_id>/pairing.json` | One search: `scan_ids`, `photos[]`, `anchors`, `exclude`, `excluded_colors`, `plans[]` in full |
| `pairings/<find_id>/refs/<work_id>.jpg` | Downloaded pictures of the works |
