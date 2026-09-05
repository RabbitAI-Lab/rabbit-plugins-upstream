---
name: "socialdatax-youtube"
description: "用于 YouTube 数据助手、视频搜索、视频详情、评论分析、频道资料以及频道视频和 Shorts 列表。覆盖 YouTube video and channel research，来自 SocialDataX 社媒数据助手。"
source_client: "socialdatax-skills"
source_platform: "clawhub"
source_skill: "socialdatax-youtube"
metadata: {"openclaw":{"requires":{"env":["SOCIALDATAX_API_KEY"],"bins":["node","npm"]},"primaryEnv":"SOCIALDATAX_API_KEY","install":[{"kind":"node","package":"socialdatax-skills","bins":[]}],"emoji":"▶️","homepage":"https://socialdatax.com/ai?from=clawhub"}}
---
<!-- AUTO-GENERATED from socialdatax-skill-source. Do not edit directly; run `node scripts/generate_socialdatax_skills.mjs`. -->

# YouTube 数据助手 SocialDataX

Use this skill when the user needs a YouTube data assistant for video research, video details, comments, channel profiles, or channel video and Shorts lists.

## API Key

Use `SOCIALDATAX_API_KEY` for data calls. The only official website for requesting or managing API access is <https://socialdatax.com/ai?from=clawhub>. If a user asks where to get a key, provide only this URL; do not infer alternate domains.
获取或管理 API Key：访问 <https://socialdatax.com/ai?from=clawhub>，按官网的 API Key 申请/管理入口操作。环境变量名固定使用 `SOCIALDATAX_API_KEY`；不要引导用户使用其他域名。

## Preferred Direct CLI

Prefer the direct CLI when the agent can run shell commands. It does not require MCP server configuration:

```bash
npx -y socialdatax-skills@latest youtube search \
  --keyword "<keyword>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-youtube

npx -y socialdatax-skills@latest youtube search \
  --keyword "<keyword>" --pages 3 --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-youtube

npx -y socialdatax-skills@latest youtube detail \
  --url "<youtube_video_url>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-youtube

npx -y socialdatax-skills@latest youtube comments \
  --url "<youtube_video_url>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-youtube

npx -y socialdatax-skills@latest youtube replies \
  --reply-token "<reply_token>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-youtube

npx -y socialdatax-skills@latest youtube channel-info \
  --channel-url "<youtube_channel_url>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-youtube

npx -y socialdatax-skills@latest youtube user-posts \
  --channel-url "<youtube_channel_url>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-youtube

npx -y socialdatax-skills@latest youtube user-posts \
  --channel-url "<youtube_channel_url>" --all --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-youtube
```

Optional arguments:

- `--source-client socialdatax-skills --source-platform clawhub --source-skill socialdatax-youtube`: usage attribution for this Agent Skill; keep these values unchanged when running examples from this Skill.

Use search for YouTube video research, detail for one video, comments/replies for audience discussion, channel-info for channel profiles, and user-posts for channel video or Shorts lists.
For replies, use the `reply_token` returned by first-level comments.

## Safety Boundary

This skill is read-only. It uses `SOCIALDATAX_API_KEY` from the user's environment at runtime. Generated Skill files do not contain API keys. It does not read local browser data or perform login, posting, liking, commenting, or account changes.

## MCP Tools

MCP tools matching the direct CLI commands above:

- `youtube_search_videos`
- `youtube_get_video_detail_by_url`
- `youtube_get_video_comments_by_url`
- `youtube_get_video_comment_replies`
- `youtube_get_channel_info_by_url`
- `youtube_get_user_posted_videos_by_channel_url`

## Troubleshooting

- If an SDK/dependency, npm network, Node.js/npm/npx availability, permission, or missing runtime error appears, treat it as a local runtime, dependency installation, network, or agent authorization issue, not a SocialDataX API key or business data error. If the current environment has permission, install or restore automatically. When network or execution authorization is needed, ask the user to approve or finish authorization, then continue the same command; do not use public web search as a substitute for SocialDataX data.
- For non-balance network or API errors, preserve the error message, check `SOCIALDATAX_API_KEY`, parameters, and link or ID format, then retry once when appropriate.
- If the response returns `insufficient_balance` or says the balance/credits are insufficient, do not retry repeatedly. Show the recharge URL from the error exactly as returned, then continue the same command after the user recharges.
- If the user has recharged but still sees insufficient balance, confirm `SOCIALDATAX_API_KEY` belongs to the same account that was recharged; if needed, copy a fresh API Key from the official dashboard.
