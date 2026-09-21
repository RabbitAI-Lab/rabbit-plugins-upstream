---
name: instagram-publish
description: Use when publishing images to Instagram via the Graph API from a Creator or Business account. Triggers when the user wants to automate Instagram posting, push an image with caption to their account, set up Instagram API access for the first time, or troubleshoot Instagram Graph API errors like "Media download has failed" or "Unsupported post request". Assumes one-time Meta App setup is complete and an Access Token is available.
---

# Instagram Publish

Publish images to Instagram through Meta's Graph API. Part 1 is one-time manual setup (browser clicks); Part 2 is the repeatable automated publish (this skill does it for you).

## When to use

- User wants to post an image to Instagram programmatically
- User has a public image URL and wants to attach a caption and publish
- User just registered a Meta App and needs the rest of the wiring done
- User is hitting "Media download has failed" or "Unsupported post request"

## When NOT to use

- Posting Reels or Stories (single-image posts and multi-image Carousels are supported)
- Local files (image must be a public URL — see error #1 below)
- Account is still a personal account (must be Creator or Business first)

## Quick Start (after Part 1 setup is done)

```bash
# 1. Put credentials in .env (one time)
cp .env.example .env
# edit .env with ACCESS_TOKEN (and optionally IG_USER_ID)

# 2a. Single image
python3 scripts/publish.py \
  --image-urls "https://example.com/photo.jpg" \
  --caption "Hello from Instagram API"

# 2b. Carousel (2-10 images, swipable in feed)
python3 scripts/publish.py \
  --image-urls "https://example.com/1.jpg" "https://example.com/2.jpg" "https://example.com/3.jpg" \
  --caption "Swipe → slide 1 / slide 2 / slide 3"
```

The script prints the new post ID on success. Done.

---

# Part 1: One-time manual setup (browser only)

These steps cannot be automated — they require human logins, email verification, and Meta's UI. Do them once, save the resulting `ACCESS_TOKEN`, and you never need to touch Meta's dashboard again unless permissions change.

## Step 1 — Switch Instagram to a Creator account

Visit <https://www.instagram.com/accounts/professional_account_settings/> and follow:

```
Settings
  ↓
Account Type
  ↓
Switch to Professional Account
  ↓
Creator
```

## Step 2 — Create a Meta Developer account

Visit <https://developers.facebook.com/> and sign in with your Facebook account, then:

```
Get Started
  ↓
Verify Email
  ↓
Accept Terms
```

## Step 3 — Create an App

Visit <https://developers.facebook.com/apps/>:

```
Create App
  ↓
Use cases: Manage messaging & content on Instagram
  ↓
Do NOT connect a Business portfolio
```

> ⚠️ Skipping the Business portfolio avoids the "insufficient developer permissions" error later.

## Step 4 — Finish App settings

In **App settings → Basic**:

- Upload an app icon
- Fill in Privacy Policy URL and Data Deletion URL
- Pick an app category
- (Optional) In **Use cases → Customize**, configure account linking at <https://accountscenter.instagram.com/connected_experiences/>
- Click **Publish** to make the app live

## Step 5 — Generate the Access Token

```
Use cases → Customize
  ↓
Left sidebar: API setup with Instagram login
  ↓
Add required messaging permissions
  ↓
Add account → authorize your Instagram account
  ↓
Generate token
  ↓
Check "I understand" → copy the token
```

The token starts with `IGAA...`. Save it to `.env` (next section).

## Credentials you should have after Part 1

| Field | Example | Lives in |
|---|---|---|
| `ACCESS_TOKEN` | `IGAAxxxxx...` | `.env` |
| `IG_USER_ID` | `2700xxxxxx` | `.env` (optional — script can auto-fetch) |
| `USERNAME` | `xxxxx` | reference only |

> ⚠️ Never commit `.env` to git. The token is the only thing that authenticates posts on your behalf.

---

# Part 2: Automated publishing (the skill does this)

The Graph API calls below are bundled in `scripts/publish.py`. You run one command; the script runs the whole flow. The path is chosen automatically from the number of URLs:

- **1 URL → single-image mode** (3 calls):
  ```
  [1] Validate token   →  GET /me?fields=id,username
         ↓
  [2] Create container  →  POST /{ig_user_id}/media   (image_url + caption)
         ↓
  [3] Publish           →  POST /{ig_user_id}/media_publish   (creation_id)
  ```

- **2–10 URLs → Carousel mode** (5+ calls):
  ```
  [1] Validate token   →  GET /me?fields=id,username
         ↓
  [2a] Create item     →  POST /{ig_user_id}/media   (image_url + is_carousel_item=true)   × N
         ↓
  [2b] Create carousel →  POST /{ig_user_id}/media   (media_type=CAROUSEL + children=id1,id2,...)
         ↓
  [3]  Publish         →  POST /{ig_user_id}/media_publish   (creation_id)
  ```

## Setting up `.env`

```bash
cp .env.example .env
```

`.env` contents:

```
ACCESS_TOKEN=IGAAxxxxxxxxxxxxxxxxxxxx
IG_USER_ID=2700xxxxxxxx        # optional — auto-detected if missing
```

The script reads `.env` from the skill directory. If you run it from elsewhere, pass `--env /path/to/.env`.

## Publishing an image with public reachable url

可以调用可用的文生图模型或生图 SKILL来生图，通常会返回一个公网 CDN 临时 URL。无需下载图片后再上传到图床，直接用这个图片 URL 传入以下脚本即可用于发布 ins 帖子。

```bash
python3 scripts/publish.py \
  --image-urls "https://example.com/photo.jpg" \
  --caption "Hello from Instagram API"
```

Optional flags:

| Flag | Default | Notes |
|---|---|---|
| `--image-urls URL [URL ...]` | required | One or more public image URLs. 1 URL = single post, 2-10 URLs = Carousel. Each URL must be reachable by Meta's servers. Usually, use the the returned url from image generation model. if user provides a local file, you should invoke relevant skill to upload it to OSS/COS platform and get a public url before publishing |
| `--caption TEXT` | empty | Instagram's caption, with hashtags and mentions |
| `--env PATH` | `./.env` | Path to a `.env` file |
| `--api-version` | `v24.0` | Graph API version |
| `--dry-run` | off | Validate token and build the container, but skip the final publish |

Successful single-image output:

```
✓ Token valid — user: xxxxx (id: 2700xxxxxx)
→ Single-image mode
✓ Container created: xxxxx
✓ Published: xxxxx
https://www.instagram.com/p/xxxxxxxxx
```

## Publishing a multi-image Carousel (2–10 images)

Pass 2–10 URLs to `--image-urls` and the script will switch to Carousel mode automatically. The flow is:

```
For each image URL:
  POST /{ig_user_id}/media   image_url=...  is_carousel_item=true
       → returns N creation_ids

Then:
  POST /{ig_user_id}/media   media_type=CAROUSEL  children=id1,id2,...  caption=...
       → returns one carousel creation_id

Then:
  POST /{ig_user_id}/media_publish   creation_id=<carousel id>
       → returns the published post id
```

Example:

```bash
python3 scripts/publish.py \
  --image-urls "https://example.com/1.jpg" "https://example.com/2.jpg" "https://example.com/3.jpg" \
  --caption "这是 OpenClaw 自动发布的多图帖子 #carousel"
```

Successful Carousel output:

```
✓ Token valid — user: xxxxx (id: 2700xxxxxx)
→ Carousel mode (3 images)
✓ Carousel item 1/3 container: 111111111111
✓ Carousel item 2/3 container: 222222222222
✓ Carousel item 3/3 container: 333333333333
✓ Carousel container created: 999999999999
✓ Published: 1789xxxxxxxx
https://www.instagram.com/p/xxxxxxxxx
```

Constraints:

- Carousels require **2 to 10** items — the script rejects anything outside that range.
- Every URL must be **publicly reachable by Meta's servers** — same rule as single-image mode (no localhost, no private IPs).
- Carousel items can be a mix of images and videos, but **this script only handles image URLs**. Videos need a separate video upload flow.
- Order = left-to-right swipe order on Instagram, so list URLs in the order you want users to see them.
- Each item container can take a few seconds to finish processing; if `media_publish` returns "Media ID is not available", re-run with `--dry-run` first or wait 30–60s between `create_carousel_container` and `publish_container`.

## Alternative: stitch into a single image (no Carousel API needed)

If you only need a "fake carousel" and don't want to use the Carousel API, stitch images vertically with ImageMagick and publish as a single image:

```bash  
magick img1.jpg img2.jpg -append -resize 1080x /tmp/combined.jpg
# 裁切到精确 4:5
magick /tmp/combined.jpg -gravity Center -crop 1080x1350+0+0 +repage /tmp/final.jpg
```

Use this when:
- You want fewer API calls and simpler error handling
- You're under the 10-image ceiling but want a single-image "look"
- IG 推荐 4:5（1080×1350）竖图，比例超过 1:2.67（高/宽）时 IG 会自动裁切

### 其他图床链接兼容处理
- 如果用户是用了本地的图片，缺少公开 URL，你可以帮助它采用任何匿名公共图床上传服务例如imgur.com等来获取公开 URL
- 如果用户要求上传图片到 google drive 用作图床，需要将其 standard sharing public link 转换成 raw image url, 例如：返回的链接是 `https://drive.google.com/file/d/xxxxxx/view?usp=sharing` ，要提取文件ID并转换为 `https://drive.google.com/uc?export=view&id=xxxxxx`
- 如果用户要求上传图片到 github 用作图床, 需要将其转换为`https://raw.githubusercontent.com/<username>/<repo>/<branch>/<path>/<image>.jpg`形式，例如：`https://github.com/mebusw/instagram-assets/blob/main/images/post-001.jpg`要转为`https://raw.githubusercontent.com/mebusw/instagram-assets/main/images/post-001.jpg`
---

# Common errors

## "Media download has failed"

```json
{"error": {"message": "Media download has failed"}}
```

Meta's servers cannot reach your `image_url`. Fix:

- Usually the image generation modal should return a public url of image, if not, then host the image somewhere public: Alibaba Cloud OSS, Tencent Cloud COS, AWS S3, GitHub Raw, any CDN
- Open the URL in a fresh browser *while logged out* — if you can't see it, Meta can't either
- Avoid `localhost`, `127.0.0.1`, and private network IPs

## "Media ID is not available"

原因是 container 刚创建就立即 publish，解决方案是等待 30–60 秒。

## "Unsupported post request"

```json
{"error": {"message": "Unsupported post request"}}
```

Almost always a token-permission issue. Fix:

- Back to **Use cases → Customize** in the App dashboard
- Confirm `instagram_content_publish` and `instagram_basic` are granted
- Re-generate the token and replace `ACCESS_TOKEN` in `.env`

## Token expired

Long-lived tokens still expire (default ~60 days). If `/me` returns an auth error, regenerate the token in the App dashboard and update `.env`.

---

# Files in this skill

```
instagram-publish/
├── SKILL.md            # this file
├── .env.example        # template for ACCESS_TOKEN and IG_USER_ID
├── .gitignore          # keeps .env out of git
└── scripts/
    └── publish.py      # the three-step publisher
```
