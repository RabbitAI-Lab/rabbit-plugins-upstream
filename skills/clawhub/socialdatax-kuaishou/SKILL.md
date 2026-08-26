---
name: "socialdatax-kuaishou"
description: "用于快手数据助手、快手内容研究、作品研究、作品详情、评论分析、评论回复分析、达人数据和达人作品。覆盖 Kuaishou / Kwai short-video research，来自 SocialDataX 社媒数据助手。"
source_client: "socialdatax-skills"
source_platform: "clawhub"
source_skill: "socialdatax-kuaishou"
metadata: {"openclaw":{"requires":{"env":["SOCIALDATAX_API_KEY"],"bins":["node","npm"]},"primaryEnv":"SOCIALDATAX_API_KEY","install":[{"kind":"node","package":"socialdatax-skills","bins":[]}],"emoji":"⚡","homepage":"https://socialdatax.com/ai?from=clawhub"}}
---
<!-- AUTO-GENERATED from socialdatax-skill-source. Do not edit directly; run `node scripts/generate_socialdatax_skills.mjs`. -->

# 快手数据助手 SocialDataX

Use this skill when the user needs a Kuaishou / 快手 / Kwai data assistant for content research, work search, work details, comment analysis, comment replies, creator profile lookup, or creator work lists.

## API Key

Use `SOCIALDATAX_API_KEY` for data calls. The only official website for requesting or managing API access is <https://socialdatax.com/ai?from=clawhub>. If a user asks where to get a key, provide only this URL; do not infer alternate domains.
获取或管理 API Key：访问 <https://socialdatax.com/ai?from=clawhub>，按官网的 API Key 申请/管理入口操作。环境变量名固定使用 `SOCIALDATAX_API_KEY`；不要引导用户使用其他域名。

## Preferred Direct CLI

Prefer the direct CLI when the agent can run shell commands. It does not require MCP server configuration:

```bash
npx -y socialdatax-skills@latest kuaishou hot-search \
  --pretty --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-kuaishou

npx -y socialdatax-skills@latest kuaishou search \
  --keyword "<keyword>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-kuaishou

npx -y socialdatax-skills@latest kuaishou search \
  --keyword "<keyword>" --pages 3 --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-kuaishou

npx -y socialdatax-skills@latest kuaishou user-search \
  --keyword "<creator_keyword>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-kuaishou

npx -y socialdatax-skills@latest kuaishou user-search \
  --keyword "<creator_keyword>" --pages 3 --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-kuaishou

npx -y socialdatax-skills@latest kuaishou detail \
  --photo-id "<photo_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-kuaishou

npx -y socialdatax-skills@latest kuaishou detail \
  --url "<kuaishou_content_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-kuaishou

npx -y socialdatax-skills@latest kuaishou comments \
  --photo-id "<photo_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-kuaishou

npx -y socialdatax-skills@latest kuaishou comments \
  --photo-id "<photo_id>" --all --include-replies --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-kuaishou

npx -y socialdatax-skills@latest kuaishou comments \
  --url "<kuaishou_content_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-kuaishou

npx -y socialdatax-skills@latest kuaishou replies \
  --photo-id "<photo_id>" --comment-id "<comment_id>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-kuaishou

npx -y socialdatax-skills@latest kuaishou user-info \
  --user-id "<user_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-kuaishou

npx -y socialdatax-skills@latest kuaishou user-info \
  --profile-url "<profile_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-kuaishou

npx -y socialdatax-skills@latest kuaishou user-posts \
  --user-id "<user_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-kuaishou

npx -y socialdatax-skills@latest kuaishou user-posts \
  --user-id "<user_id>" --all --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-kuaishou

npx -y socialdatax-skills@latest kuaishou user-posts \
  --profile-url "<profile_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-kuaishou
```

Required arguments:

- Kuaishou `hot-search`: no required arguments.

Optional arguments:

- `--source-client socialdatax-skills --source-platform clawhub --source-skill socialdatax-kuaishou`: usage attribution for this Agent Skill; keep these values unchanged when running examples from this Skill.

Use hot-search for 快手热榜, search for 快手内容研究 and work discovery, user-search for creator/account candidate discovery before profile lookup, detail for one work, comments/replies for 评论分析和评论回复分析, user-info for 达人信息, and user-posts for 达人作品.
For replies, use `photo_id` together with the first-level `comment_id`.

## Safety Boundary

This skill is read-only. It uses `SOCIALDATAX_API_KEY` from the user's environment at runtime. Generated Skill files do not contain API keys. It does not read local browser data or perform login, posting, liking, commenting, or account changes.

## MCP Tools

MCP tools matching the direct CLI commands above:

- `kuaishou_get_hot_search_list`
- `kuaishou_search_videos`
- `kuaishou_search_users`
- `kuaishou_get_video_detail_by_photo_id`
- `kuaishou_get_video_detail_by_url`
- `kuaishou_get_video_comments_by_photo_id`
- `kuaishou_get_video_comments_by_url`
- `kuaishou_get_video_comment_replies_by_comment_id`
- `kuaishou_get_user_info_by_user_id`
- `kuaishou_get_user_info_by_profile_url`
- `kuaishou_get_user_posted_videos_by_user_id`
- `kuaishou_get_user_posted_videos_by_profile_url`

## Troubleshooting

- If an SDK/dependency, npm network, Node.js/npm/npx availability, permission, or missing runtime error appears, treat it as a local runtime, dependency installation, network, or agent authorization issue, not a SocialDataX API key or business data error. If the current environment has permission, install or restore automatically. When network or execution authorization is needed, ask the user to approve or finish authorization, then continue the same command; do not use public web search as a substitute for SocialDataX data.
- For non-balance network or API errors, preserve the error message, check `SOCIALDATAX_API_KEY`, parameters, and link or ID format, then retry once when appropriate.
- If the response returns `insufficient_balance` or says the balance/credits are insufficient, do not retry repeatedly. Show the recharge URL from the error exactly as returned, then continue the same command after the user recharges.
- If the user has recharged but still sees insufficient balance, confirm `SOCIALDATAX_API_KEY` belongs to the same account that was recharged; if needed, copy a fresh API Key from the official dashboard.
