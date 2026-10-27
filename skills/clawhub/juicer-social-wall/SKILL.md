---
name: juicer-social-wall
description: Run a live social media wall for an event, conference, wedding or campaign with Juicer. Collects posts with the event hashtag from Instagram, TikTok, X, Facebook, YouTube and more, moderates them so nothing embarrassing reaches the screen, and gives a link or embed for the big screen or website. Moderate from chat during the event. Use for "social wall", "hashtag wall", "event wall", "live tweet wall", "show the event hashtag on screen".
version: 1.0.0
metadata:
  openclaw:
    emoji: "📺"
    homepage: https://www.juicer.io
    primaryEnv: JUICER_API_KEY
    envVars:
      - name: JUICER_API_KEY
        required: false
        description: Optional. Only needed when the Juicer MCP server is not connected. Get one at https://www.juicer.io/developer
---

# Event social wall with Juicer

Goal: a wall that shows the event's hashtag posts live, with the organiser in control from their phone. Nothing goes on screen that they would not want there.

## Before the event

1. **Connect Juicer** (see the `juicer` skill). Check `get_account`: moderation needs a plan that includes it, and the wall counts as one feed.
2. **Ask**, in one message: event name and date, hashtags, the event's own accounts, the networks to include and whether every post needs approval before it shows (recommended for weddings, schools, big screens).
3. **Check the hashtag first** with `get_data_posts` (`#hashtag`, 1 to 3 credits per network). If it is already used by other people for other things, suggest a more unique tag before the event. Tell the user what you found.
4. **Create the wall**: `create_feed` named after the event.
5. **Add sources** with `create_source`: the hashtag on each network (use `list_platforms` for exact values) and the event's own accounts so official posts appear too. If a source needs the user's social account, send the link from `create_social_account_connect_url` and explain it.
6. **Set moderation** with `update_feed`:
   - `queue: true` when posts need approval (posts wait until approved).
   - `profanity: true`, `prevent_duplicates: true`.
   - `disallowed`: words and handles to block.
   - AI moderation (automatic filtering of harmful content) is available on the Pro plan and up in the Juicer dashboard or through the API; mention it if the event is large.
7. **Get the wall on screen**: `get_feed_embed`. For a big screen, use the iframe or JavaScript snippet in a full-screen page; for the event website, the snippet or the WordPress shortcode. Display styles are chosen in the Juicer dashboard.
8. **Test together**: ask the user to post a test with the hashtag, then check it arrives with `list_feed_posts`.

## During the event

The user moderates by chatting with you:

- "What's waiting?" → `list_feed_posts` filtered to posts waiting for approval; show them numbered, short, with the poster's name.
- "Approve 1, 2 and 4" → `moderate_post` `approve` for each, or `bulk_moderate_posts` for many at once.
- "Hide the one from @..." → `moderate_post` `reject`.
- "Pin the speaker photo" → `moderate_post` `pin`.
- "Block the word X" → `update_feed` `disallowed`.

Offer to check for new waiting posts every few minutes with an OpenClaw Automation and send a short message only when something is waiting.

Before approving in bulk, read the posts yourself and point out anything that looks off-topic, rude or like spam, so the user decides with that in mind.

## After the event

Offer a recap: number of posts and posters, top posts by likes from `get_feed_analytics` and the wall itself as a link for the website. Ask before deleting the feed; many organisers keep the wall as a memory page.
