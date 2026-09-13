---
name: linkedin-poster
description: Post text content to LinkedIn using the official API. Triggers on "post to LinkedIn", "share on LinkedIn", or /linkedin-direct.
---

# LinkedIn Poster 🦾

Post text content to LinkedIn using the official LinkedIn UGC API via curl.

## Setup

### 1. Create a LinkedIn Developer App

1. Go to [LinkedIn Developers](https://www.linkedin.com/developers/apps) and create a new app
2. Under **Products**, request **"Share on LinkedIn"** (requires LinkedIn Marketing Solution membership approval)
3. Under **Auth** tab, note your **Client ID** and **Client Secret**

### 2. Generate an OAuth Token

Use LinkedIn's **Token Generator** (in your app's Auth tab) to generate a token with these scopes:
```
openid profile w_member_social
```

> **Important:** Copy the token immediately — it's only shown once.

### 3. Get Your Person URN

```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  "https://api.linkedin.com/v2/userinfo"
```

Look for the `"sub"` field — this is your Person URN (format: `urn:li:person:XXXXX`).

### 4. Configure Credentials

Set these in **hPanel → OpenClaw → Dashboard → Environment**:
```
LINKEDIN_ACCESS_TOKEN=your_token_here
LINKEDIN_PERSON_URN=urn:li:person:XXXXX
```

> ⚠️ **Token Expiry:** Tokens expire after ~60 days with no refresh token for standard apps. You'll need to manually renew via the Token Generator. Set a calendar reminder!

---

## Posting

```bash
curl -X POST \
  -H "Authorization: Bearer ${LINKEDIN_ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -H "X-Restli-Protocol-Version: 2.0.0" \
  -d '{
    "author": "'"${LINKEDIN_PERSON_URN}"'",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
      "com.linkedin.ugc.ShareContent": {
        "shareCommentary": {
          "text": "YOUR_POST_TEXT_HERE"
        },
        "shareMediaCategory": "NONE"
      }
    },
    "visibility": {
      "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
  }' \
  "https://api.linkedin.com/v2/ugcPosts"
```

**Replace `YOUR_POST_TEXT_HERE`** with your actual JSON-escaped post content. Never post literal placeholder text.

---

## Formatting Notes

LinkedIn doesn't render Markdown. Use:
- **Emoji** as section markers (📌, 🔑, ✅, etc.)
- **Blank lines** to separate paragraphs
- **Emoji + text** instead of headings

---

## Troubleshooting

| Status | Cause | Fix |
|--------|-------|-----|
| **401 Unauthorized** | Invalid or expired token | Regenerate token via Token Generator |
| **403 Forbidden** | Missing `w_member_social` scope | Request the scope and regenerate token |
| **Empty response** | Missing Person URN | Verify `LINKEDIN_PERSON_URN` is correct |
| **422 Unprocessable** | Invalid JSON or malformed URN | Check JSON syntax and URN format |
