---
name: juicer-social-feed
description: Put a brand's social media posts on its website with Juicer. Creates a social feed from Instagram, TikTok, Facebook, X, YouTube, LinkedIn and 10+ more networks, sets up moderation and returns the embed code for any site, WordPress, Wix, Squarespace, Shopify or Webflow. Use for "add our Instagram to the website", "embed social media feed", "social media aggregator", "show our TikTok on the homepage", "social proof on the website".
version: 1.0.0
metadata:
  openclaw:
    emoji: "🖼️"
    homepage: https://www.juicer.io
    primaryEnv: JUICER_API_KEY
    envVars:
      - name: JUICER_API_KEY
        required: false
        description: Optional. Only needed when the Juicer MCP server is not connected. Get one at https://www.juicer.io/developer
---

# Social feed on a website with Juicer

Goal: in one conversation the user goes from "put our socials on the site" to a working embed code, with only the posts they want.

## Steps

1. **Connect Juicer** (see the `juicer` skill). A free Juicer account is enough to start; `get_account` shows the feed and source limits.
2. **Ask what to show**, in one message: which accounts and hashtags per network, where on the site, and what to keep out (competitors, swear words, certain hashtags).
3. **Check the accounts** with `get_data_profiles` when the user gives names rather than exact handles, and confirm with the user before adding anything. Showing the wrong brand on someone's website is the worst outcome here.
4. **Create the feed**: `create_feed` with a clear name ("Homepage social feed").
5. **Add sources**: call `list_platforms` for the exact `platform` and `term_type` values, then `create_source` once per account or hashtag.
   - Some sources need the user to connect their own account (Instagram stories and mentions, Facebook mentions, Slack, Tumblr). If `create_source` returns `social_account_required`, call `create_social_account_connect_url`, send the link to the user and explain it opens a sign-in with that network and expires in 30 minutes. Retry after they say it is done.
   - If the feed or source limit is reached, show the user the upgrade link from the error. Do not delete their other feeds to make room.
6. **Set moderation** with `update_feed`:
   - `profanity: true` and `prevent_duplicates: true` are good defaults.
   - `disallowed`: comma-separated words to block (competitor names, words the user listed).
   - `queue: true` if the user wants to approve every post before it shows.
7. **Review the first posts**: `list_feed_posts`, then show the user 5 to 10 with links. Reject anything off-brand with `moderate_post` (`reject`), pin the best one (`pin`) if they want a post on top.
8. **Hand over the embed code**: `get_feed_embed` returns JavaScript, iframe and WordPress versions. Give the one that fits their site:
   - WordPress: the shortcode, pasted into a Shortcode block.
   - Wix, Squarespace, Webflow, Shopify: the JavaScript snippet in an HTML or Custom Code block.
   - Plain HTML: the JavaScript snippet where the feed should appear.
9. **Finish** with the feed name, what it shows, how it is moderated and the link to change the look in the Juicer dashboard (https://www.juicer.io/dashboard).

## Good to know

- New posts appear on their own; the feed syncs automatically. How often depends on the plan.
- Layout, colours and post count are set in the Juicer dashboard; the embed code does not change when the design does.
- Ask before deleting any feed, source or post.
