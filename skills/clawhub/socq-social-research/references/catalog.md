# Capability Catalog

Generated from SocQ Capability Registry schema `v1-dc091b011267`. Do not edit endpoint definitions manually.

| Endpoint | Purpose | Required input | Cost |
| --- | --- | --- | --- |
| [`facebook-ad-library/ad`](https://docs.socq.ai/api-manual/facebook-ad-library/ad) | Facebook Ad Library Ad API | url | 0.6 credits/result |
| [`facebook-ad-library/company-ads`](https://docs.socq.ai/api-manual/facebook-ad-library/company-ads) | Facebook Ad Library Company Ads API | page_id | 0.5 credits/result |
| [`facebook-ad-library/company-search`](https://docs.socq.ai/api-manual/facebook-ad-library/company-search) | Facebook Ad Library Company Search API | query | 0.5 credits/result |
| [`facebook-ad-library/search`](https://docs.socq.ai/api-manual/facebook-ad-library/search) | Facebook Ad Library Search API | query | 0.5 credits/result |
| [`facebook-marketplace/item`](https://docs.socq.ai/api-manual/facebook-marketplace/item) | Facebook Marketplace Item API | urls | 0.6 credits/result |
| [`facebook-marketplace/location-search`](https://docs.socq.ai/api-manual/facebook-marketplace/location-search) | Facebook Marketplace Location Search API | query | 0.3 credits/result |
| [`facebook-marketplace/search`](https://docs.socq.ai/api-manual/facebook-marketplace/search) | Facebook Marketplace Search API | latitude, longitude, query | 0.7 credits/result |
| [`facebook/ad-transcript`](https://docs.socq.ai/api-manual/facebook/ad-transcript) | Extract transcripts from public Facebook ads. | urls | 0.5 credits/result |
| [`facebook/comment-replies`](https://docs.socq.ai/api-manual/facebook/comment-replies) | Collect public Facebook comment replies. | one of: comment_id + url; expansion_token + feedback_id | 0.3 credits/result |
| [`facebook/comments`](https://docs.socq.ai/api-manual/facebook/comments) | Facebook Comments API | urls | 0.3 credits/result |
| [`facebook/company-reviews`](https://docs.socq.ai/api-manual/facebook/company-reviews) | Collect public Facebook company reviews. | urls | 0.5 credits/result |
| [`facebook/event-details`](https://docs.socq.ai/api-manual/facebook/event-details) | Collect public Facebook event details. | urls | 0.5 credits/result |
| [`facebook/events-search`](https://docs.socq.ai/api-manual/facebook/events-search) | Search public Facebook events by keyword. | query | 0.6 credits/result |
| [`facebook/group-posts`](https://docs.socq.ai/api-manual/facebook/group-posts) | Collect posts from public Facebook groups. | urls | 1.2 credits/result |
| [`facebook/pages`](https://docs.socq.ai/api-manual/facebook/pages) | Facebook Page API | one of: query; urls; usernames | 2.4 credits/result |
| [`facebook/posts`](https://docs.socq.ai/api-manual/facebook/posts) | Facebook Posts API | one of: query; urls; usernames | 1 credits/result |
| [`facebook/profile-events`](https://docs.socq.ai/api-manual/facebook/profile-events) | Collect public Facebook profile events. | urls | 0.6 credits/result |
| [`facebook/profile-photos`](https://docs.socq.ai/api-manual/facebook/profile-photos) | Collect public Facebook profile photos. | urls | 0.5 credits/result |
| [`facebook/profiles`](https://docs.socq.ai/api-manual/facebook/profiles) | Collect public Facebook profile details. | urls | 1.2 credits/result |
| [`facebook/reels`](https://docs.socq.ai/api-manual/facebook/reels) | Collect public Facebook profile reels. | urls | 0.7 credits/result |
| [`facebook/video-transcript`](https://docs.socq.ai/api-manual/facebook/video-transcript) | Extract transcripts from public Facebook videos and reels. | urls | 0.7 credits/result |
| [`instagram/audio-reels`](https://docs.socq.ai/api-manual/instagram/audio-reels) | Collect public Instagram reels by audio identifier. | audio_ids | 0.5 credits/result |
| [`instagram/comments`](https://docs.socq.ai/api-manual/instagram/comments) | Instagram Comments API | urls | 0.3 credits/result |
| [`instagram/followers-count`](https://docs.socq.ai/api-manual/instagram/followers-count) | Instagram Followers Count API | one of: query; urls; usernames | 0.52 credits/result |
| [`instagram/followers-list`](https://docs.socq.ai/api-manual/instagram/followers-list) | Collect public profiles from an Instagram account follower list. | usernames | 0.3 credits/result |
| [`instagram/following-list`](https://docs.socq.ai/api-manual/instagram/following-list) | Collect public profiles followed by an Instagram account. | usernames | 0.3 credits/result |
| [`instagram/hashtag-posts`](https://docs.socq.ai/api-manual/instagram/hashtag-posts) | Collect public Instagram posts matching a hashtag. | hashtags | 0.5 credits/result |
| [`instagram/highlight-items`](https://docs.socq.ai/api-manual/instagram/highlight-items) | Collect public Instagram highlight items. | highlight_ids | 0.5 credits/result |
| [`instagram/post-info`](https://docs.socq.ai/api-manual/instagram/post-info) | Collect public Instagram post details. | urls | 0.5 credits/result |
| [`instagram/posts`](https://docs.socq.ai/api-manual/instagram/posts) | Instagram Post API | one of: query; urls; usernames | 0.34 credits/result |
| [`instagram/profiles`](https://docs.socq.ai/api-manual/instagram/profiles) | Collect public Instagram profile metadata and statistics. | usernames | 0.6 credits/result |
| [`instagram/reels`](https://docs.socq.ai/api-manual/instagram/reels) | Instagram Reel API | one of: query; urls; usernames | 0.52 credits/result |
| [`instagram/reels-search`](https://docs.socq.ai/api-manual/instagram/reels-search) | Search public Instagram reels. | query | 0.5 credits/result |
| [`instagram/search`](https://docs.socq.ai/api-manual/instagram/search) | Instagram Search API | one of: query; urls; usernames | 0.54 credits/result |
| [`instagram/story-highlights`](https://docs.socq.ai/api-manual/instagram/story-highlights) | Collect public Instagram story highlights. | usernames | 0.5 credits/result |
| [`instagram/tagged-posts`](https://docs.socq.ai/api-manual/instagram/tagged-posts) | Collect public posts that tag an Instagram profile. | usernames | 0.5 credits/result |
| [`instagram/transcript`](https://docs.socq.ai/api-manual/instagram/transcript) | Extract transcripts from public Instagram posts and reels. | urls | 0.7 credits/result |
| [`instagram/trending-reels`](https://docs.socq.ai/api-manual/instagram/trending-reels) | Collect public trending Instagram reels. | none | 0.5 credits/result |
| [`linkedin/companies`](https://docs.socq.ai/api-manual/linkedin/companies) | LinkedIn Companies API | urls | 2 credits/result |
| [`linkedin/jobs`](https://docs.socq.ai/api-manual/linkedin/jobs) | LinkedIn Jobs API | urls | 0.8 credits/result |
| [`linkedin/posts`](https://docs.socq.ai/api-manual/linkedin/posts) | LinkedIn Posts API | urls | 1 credits/result |
| [`linkedin/profiles`](https://docs.socq.ai/api-manual/linkedin/profiles) | LinkedIn Profiles API | urls | 2.5 credits/result |
| [`pinterest/pins`](https://docs.socq.ai/api-manual/pinterest/pins) | Pinterest Pins API | urls | 0.5 credits/result |
| [`pinterest/profiles`](https://docs.socq.ai/api-manual/pinterest/profiles) | Pinterest Profiles API | urls | 0.6 credits/result |
| [`pinterest/search`](https://docs.socq.ai/api-manual/pinterest/search) | Pinterest Search API | query | 0.6 credits/result |
| [`pinterest/user-pins`](https://docs.socq.ai/api-manual/pinterest/user-pins) | Pinterest User Pins API | urls | 0.5 credits/result |
| [`reddit/comments`](https://docs.socq.ai/api-manual/reddit/comments) | Reddit Comments API | urls | 0.3 credits/result |
| [`reddit/posts`](https://docs.socq.ai/api-manual/reddit/posts) | Reddit Posts API | urls | 0.5 credits/result |
| [`reddit/search`](https://docs.socq.ai/api-manual/reddit/search) | Reddit Search API | query | 0.6 credits/result |
| [`reddit/subreddit-posts`](https://docs.socq.ai/api-manual/reddit/subreddit-posts) | Reddit Subreddit Posts API | urls | 0.5 credits/result |
| [`seo/google-organic-serp`](https://docs.socq.ai/api-manual/seo/google-organic-serp) | Retrieve live organic search results. | query | 0.1 credits/result |
| [`seo/keyword-difficulty`](https://docs.socq.ai/api-manual/seo/keyword-difficulty) | Calculate ranking difficulty for each input keyword. | keywords | 0.1 credits/input |
| [`seo/keyword-overview`](https://docs.socq.ai/api-manual/seo/keyword-overview) | Return combined metrics for each input keyword. | keywords | 0.15 credits/input |
| [`seo/keyword-search-volume`](https://docs.socq.ai/api-manual/seo/keyword-search-volume) | Batch search volume, CPC, competition, and monthly trends. | keywords | 24 credits/request |
| [`seo/keyword-suggestions`](https://docs.socq.ai/api-manual/seo/keyword-suggestions) | Find long-tail terms containing a seed keyword. | query | 0.1 credits/result |
| [`seo/keywords-for-site`](https://docs.socq.ai/api-manual/seo/keywords-for-site) | Generate keywords relevant to a website. | target | 0.1 credits/result |
| [`seo/ranked-keywords`](https://docs.socq.ai/api-manual/seo/ranked-keywords) | Find keywords already ranked by a domain or page. | target | 0.1 credits/result |
| [`seo/related-keywords`](https://docs.socq.ai/api-manual/seo/related-keywords) | Find semantically and lexically related keywords. | query | 0.1 credits/result |
| [`seo/relevant-pages`](https://docs.socq.ai/api-manual/seo/relevant-pages) | Find pages with measurable SEO value. | target | 0.15 credits/result |
| [`seo/search-intent`](https://docs.socq.ai/api-manual/seo/search-intent) | Classify the intent of each input keyword. | keywords | 0.1 credits/input |
| [`threads/posts`](https://docs.socq.ai/api-manual/threads/posts) | Threads Posts API | urls | 0.5 credits/result |
| [`threads/profiles`](https://docs.socq.ai/api-manual/threads/profiles) | Threads Profiles API | urls | 0.6 credits/result |
| [`threads/user-posts`](https://docs.socq.ai/api-manual/threads/user-posts) | Threads User Posts API | urls | 0.5 credits/result |
| [`tiktok-shop/product`](https://docs.socq.ai/api-manual/tiktok-shop/product) | TikTok Shop Product API | url | 0.7 credits/result |
| [`tiktok-shop/product-reviews`](https://docs.socq.ai/api-manual/tiktok-shop/product-reviews) | TikTok Shop Product Reviews API | url | 0.3 credits/result |
| [`tiktok-shop/products`](https://docs.socq.ai/api-manual/tiktok-shop/products) | TikTok Shop Products API | url | 0.7 credits/result |
| [`tiktok-shop/search`](https://docs.socq.ai/api-manual/tiktok-shop/search) | TikTok Shop Search API | query | 0.7 credits/result |
| [`tiktok-shop/user-showcase`](https://docs.socq.ai/api-manual/tiktok-shop/user-showcase) | TikTok Shop User Showcase API | username | 0.7 credits/result |
| [`tiktok/comment-replies`](https://docs.socq.ai/api-manual/tiktok/comment-replies) | Collect public TikTok comment replies. | comment_id, url | 0.5 credits/result |
| [`tiktok/comments`](https://docs.socq.ai/api-manual/tiktok/comments) | TikTok Comments API | urls | 0.25 credits/result |
| [`tiktok/followers-list`](https://docs.socq.ai/api-manual/tiktok/followers-list) | Collect public TikTok follower profiles. | usernames | 0.5 credits/result |
| [`tiktok/following-list`](https://docs.socq.ai/api-manual/tiktok/following-list) | Collect public TikTok followed profiles. | usernames | 0.5 credits/result |
| [`tiktok/hashtags`](https://docs.socq.ai/api-manual/tiktok/hashtags) | TikTok Hashtags API | hashtags | 0.7 credits/result |
| [`tiktok/live-room-info`](https://docs.socq.ai/api-manual/tiktok/live-room-info) | Collect public TikTok live room metadata and audience metrics. | room_id, user_id | 0.5 credits/result |
| [`tiktok/profiles`](https://docs.socq.ai/api-manual/tiktok/profiles) | TikTok Profiles API | usernames | 0.6 credits/result |
| [`tiktok/search`](https://docs.socq.ai/api-manual/tiktok/search) | TikTok Search API | query | 0.7 credits/result |
| [`tiktok/trending-feed`](https://docs.socq.ai/api-manual/tiktok/trending-feed) | Collect trending TikTok videos for a region. | region | 0.7 credits/result |
| [`tiktok/user-videos`](https://docs.socq.ai/api-manual/tiktok/user-videos) | Collect public videos from TikTok profiles. | usernames | 0.5 credits/result |
| [`tiktok/video-transcript`](https://docs.socq.ai/api-manual/tiktok/video-transcript) | Extract transcripts from public TikTok videos. | urls | 0.5 credits/result |
| [`tiktok/videos`](https://docs.socq.ai/api-manual/tiktok/videos) | TikTok Videos API | urls | 0.7 credits/result |
| [`x/followers-list`](https://docs.socq.ai/api-manual/x/followers-list) | Collect public X follower profiles. | usernames | 0.5 credits/result |
| [`x/following-list`](https://docs.socq.ai/api-manual/x/following-list) | Collect public X followed profiles. | usernames | 0.5 credits/result |
| [`x/post-quotes`](https://docs.socq.ai/api-manual/x/post-quotes) | Collect public quotes of X posts. | urls | 0.5 credits/result |
| [`x/post-replies`](https://docs.socq.ai/api-manual/x/post-replies) | Collect public replies to X posts. | urls | 0.5 credits/result |
| [`x/post-retweeters`](https://docs.socq.ai/api-manual/x/post-retweeters) | Collect public profiles that reposted X posts. | urls | 0.5 credits/result |
| [`x/posts`](https://docs.socq.ai/api-manual/x/posts) | X Posts API | urls | 0.5 credits/result |
| [`x/profiles`](https://docs.socq.ai/api-manual/x/profiles) | X Profiles API | usernames | 0.6 credits/result |
| [`x/search`](https://docs.socq.ai/api-manual/x/search) | X Search API | query | 0.7 credits/result |
| [`x/trends`](https://docs.socq.ai/api-manual/x/trends) | Collect public X trends by location identifier. | woeids | 0.5 credits/result |
| [`x/user-posts`](https://docs.socq.ai/api-manual/x/user-posts) | X User Posts API | usernames | 0.5 credits/result |
| [`youtube/channel-live-videos`](https://docs.socq.ai/api-manual/youtube/channel-live-videos) | Collect public YouTube channel live videos. | urls | 0.5 credits/result |
| [`youtube/channel-videos`](https://docs.socq.ai/api-manual/youtube/channel-videos) | YouTube Channel Videos API | urls | 0.5 credits/result |
| [`youtube/channels`](https://docs.socq.ai/api-manual/youtube/channels) | YouTube Channels API | urls | 0.26 credits/result |
| [`youtube/comment-replies`](https://docs.socq.ai/api-manual/youtube/comment-replies) | Collect public YouTube comment replies. | one of: comment_id + url; continuation_token | 0.5 credits/result |
| [`youtube/comments`](https://docs.socq.ai/api-manual/youtube/comments) | YouTube Comments API | urls | 0.3 credits/result |
| [`youtube/community-posts`](https://docs.socq.ai/api-manual/youtube/community-posts) | Collect public YouTube community posts. | urls | 0.5 credits/result |
| [`youtube/hashtag-search`](https://docs.socq.ai/api-manual/youtube/hashtag-search) | Search public YouTube videos by hashtag. | hashtags | 0.5 credits/result |
| [`youtube/playlist-videos`](https://docs.socq.ai/api-manual/youtube/playlist-videos) | Collect videos from a public YouTube playlist. | urls | 0.5 credits/result |
| [`youtube/search`](https://docs.socq.ai/api-manual/youtube/search) | YouTube Search API | query | 0.5 credits/result |
| [`youtube/shorts`](https://docs.socq.ai/api-manual/youtube/shorts) | YouTube Shorts API | urls | 0.5 credits/result |
| [`youtube/transcripts`](https://docs.socq.ai/api-manual/youtube/transcripts) | YouTube Transcripts API | urls | 0.5 credits/result |
| [`youtube/videos`](https://docs.socq.ai/api-manual/youtube/videos) | YouTube Videos API | urls | 0.5 credits/result |
