---
name: "socialdatax-bilibili"
description: "用于 B站数据助手、视频和专栏搜索、内容详情、评论分析、点赞转发观察、UP主资料及视频、专栏和动态列表。覆盖 Bilibili / 哔哩哔哩，来自 SocialDataX 社媒数据助手。"
source_client: "socialdatax-skills"
source_platform: "clawhub"
source_skill: "socialdatax-bilibili"
metadata: {"openclaw":{"requires":{"env":["SOCIALDATAX_API_KEY"],"bins":["node","npm"]},"primaryEnv":"SOCIALDATAX_API_KEY","install":[{"kind":"node","package":"socialdatax-skills","bins":[]}],"emoji":"📺","homepage":"https://socialdatax.com/ai?from=clawhub"}}
---
<!-- AUTO-GENERATED from socialdatax-skill-source. Do not edit directly; run `node scripts/generate_socialdatax_skills.mjs`. -->

# B站数据助手 SocialDataX

Use this skill when the user needs a Bilibili / 哔哩哔哩 / B站 data assistant for video or article research, content details, comments, reactions, creator profiles, creator videos, articles, dynamics, or explicitly asks to save a Bilibili video locally.

## API Key

Use `SOCIALDATAX_API_KEY` for data calls. The only official website for requesting or managing API access is <https://socialdatax.com/ai?from=clawhub>. If a user asks where to get a key, provide only this URL; do not infer alternate domains.
获取或管理 API Key：访问 <https://socialdatax.com/ai?from=clawhub>，按官网的 API Key 申请/管理入口操作。环境变量名固定使用 `SOCIALDATAX_API_KEY`；不要引导用户使用其他域名。

## Preferred Direct CLI

Prefer the direct CLI when the agent can run shell commands. It does not require MCP server configuration:

```bash
npx -y socialdatax-skills@latest bilibili search-videos \
  --keyword "<keyword>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-bilibili

npx -y socialdatax-skills@latest bilibili search-articles \
  --keyword "<keyword>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-bilibili

npx -y socialdatax-skills@latest bilibili detail \
  --content-id "<content_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-bilibili

npx -y socialdatax-skills@latest bilibili detail \
  --url "<bilibili_content_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-bilibili

npx -y socialdatax-skills@latest bilibili comments \
  --content-id "<content_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-bilibili

npx -y socialdatax-skills@latest bilibili comments \
  --url "<bilibili_content_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-bilibili

npx -y socialdatax-skills@latest bilibili replies \
  --comment-object-id "<comment_object_id>" \
  --comment-object-type "<comment_object_type>" --comment-id "<comment_id>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-bilibili

npx -y socialdatax-skills@latest bilibili reactions \
  --post-id "<post_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-bilibili

npx -y socialdatax-skills@latest bilibili reactions \
  --url "<bilibili_opus_or_dynamic_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-bilibili

npx -y socialdatax-skills@latest bilibili user-info \
  --user-id "<user_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-bilibili

npx -y socialdatax-skills@latest bilibili user-info \
  --profile-url "<profile_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-bilibili

npx -y socialdatax-skills@latest bilibili user-videos \
  --user-id "<user_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-bilibili

npx -y socialdatax-skills@latest bilibili user-videos \
  --profile-url "<profile_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-bilibili

npx -y socialdatax-skills@latest bilibili user-articles \
  --user-id "<user_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-bilibili

npx -y socialdatax-skills@latest bilibili user-articles \
  --profile-url "<profile_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-bilibili

npx -y socialdatax-skills@latest bilibili user-dynamics \
  --user-id "<user_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-bilibili

npx -y socialdatax-skills@latest bilibili user-dynamics \
  --profile-url "<profile_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-bilibili

npx -y socialdatax-skills@latest bilibili download \
  --url "<bilibili_video_url_or_share_text>" --output-dir ./downloads --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-bilibili
```

Optional arguments:

- `--source-client socialdatax-skills --source-platform clawhub --source-skill socialdatax-bilibili`: usage attribution for this Agent Skill; keep these values unchanged when running examples from this Skill.

Use search-videos or search-articles for Bilibili / 哔哩哔哩 / B站 content research, detail for one video, article, or dynamic, comments/replies for discussion analysis, reactions for likes and reposts, user-info for creator profiles, creator list commands for videos, articles, and dynamics, and run download only when the user explicitly asks to save a video locally.
For replies, use the `comment_object_id`, `comment_object_type`, and first-level `comment_id` returned by first-level comments.

## Safety Boundary

SocialDataX requests in this skill are read-only and do not modify social accounts or platform content. It uses `SOCIALDATAX_API_KEY` from the user's environment at runtime; generated Skill files do not contain API keys. It does not read local browser data or perform login, posting, liking, commenting, or account changes. The optional `bilibili download` command writes video and audio tracks plus the merged video to the user-selected local output path, uses local `ffmpeg`, and removes temporary tracks unless `--keep-tracks` is set.

## MCP Tools

MCP tools matching the direct CLI commands above:

- `bilibili_search_videos`
- `bilibili_search_articles`
- `bilibili_get_content_detail_by_id`
- `bilibili_get_content_detail_by_url`
- `bilibili_get_content_comments_by_id`
- `bilibili_get_content_comments_by_url`
- `bilibili_get_content_comment_replies_by_comment_id`
- `bilibili_get_content_likes_and_reposts_by_post_id`
- `bilibili_get_content_likes_and_reposts_by_url`
- `bilibili_get_user_info_by_user_id`
- `bilibili_get_user_info_by_profile_url`
- `bilibili_get_user_posted_videos_by_user_id`
- `bilibili_get_user_posted_videos_by_profile_url`
- `bilibili_get_user_posted_articles_by_user_id`
- `bilibili_get_user_posted_articles_by_profile_url`
- `bilibili_get_user_posted_dynamics_by_user_id`
- `bilibili_get_user_posted_dynamics_by_profile_url`
- `bilibili_get_video_download_links`

## Troubleshooting

- If an SDK/dependency, npm network, Node.js/npm/npx availability, permission, or missing runtime error appears, treat it as a local runtime, dependency installation, network, or agent authorization issue, not a SocialDataX API key or business data error. If the current environment has permission, install or restore automatically. When network or execution authorization is needed, ask the user to approve or finish authorization, then continue the same command; do not use public web search as a substitute for SocialDataX data.
- For non-balance network or API errors, preserve the error message, check `SOCIALDATAX_API_KEY`, parameters, and link or ID format, then retry once when appropriate.
- If the response returns `insufficient_balance` or says the balance/credits are insufficient, do not retry repeatedly. Show the recharge URL from the error exactly as returned, then continue the same command after the user recharges.
- If the user has recharged but still sees insufficient balance, confirm `SOCIALDATAX_API_KEY` belongs to the same account that was recharged; if needed, copy a fresh API Key from the official dashboard.
