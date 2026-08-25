---
name: "socialdatax-douyin"
description: "用于抖音数据助手、抖音热榜、抖音数据分析、作品搜索、作品详情、评论分析、评论回复分析、达人数据、达人作品和达人短剧/合集。覆盖 Douyin hot search and work research，来自 SocialDataX 社媒数据助手。"
source_client: "socialdatax-skills"
source_platform: "clawhub"
source_skill: "socialdatax-douyin"
metadata: {"openclaw":{"requires":{"env":["SOCIALDATAX_API_KEY"],"bins":["node","npm"]},"primaryEnv":"SOCIALDATAX_API_KEY","install":[{"kind":"node","package":"socialdatax-skills","bins":[]}],"emoji":"🎬","homepage":"https://socialdatax.com/ai?from=clawhub"}}
---
<!-- AUTO-GENERATED from socialdatax-skill-source. Do not edit directly; run `node scripts/generate_socialdatax_skills.mjs`. -->

# 抖音数据助手 SocialDataX

Use this skill when the user needs a Douyin / 抖音 data assistant for content research, hot search, work search, image/text post search, content details, comment analysis, comment replies, creator profile lookup, creator work lists, or creator short-drama series.

## API Key

Use `SOCIALDATAX_API_KEY` for data calls. The only official website for requesting or managing API access is <https://socialdatax.com/ai?from=clawhub>. If a user asks where to get a key, provide only this URL; do not infer alternate domains.
获取或管理 API Key：访问 <https://socialdatax.com/ai?from=clawhub>，按官网的 API Key 申请/管理入口操作。环境变量名固定使用 `SOCIALDATAX_API_KEY`；不要引导用户使用其他域名。

## Preferred Direct CLI

Choose the matching SocialDataX command:

```bash
npx -y socialdatax-skills@latest douyin hot-search \
  --pretty --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-douyin

npx -y socialdatax-skills@latest douyin search \
  --keyword "<keyword>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-douyin

npx -y socialdatax-skills@latest douyin search \
  --keyword "<keyword>" --pages 3 --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-douyin

npx -y socialdatax-skills@latest douyin detail \
  --aweme-id "<aweme_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-douyin

npx -y socialdatax-skills@latest douyin detail \
  --url "<douyin_content_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-douyin

npx -y socialdatax-skills@latest douyin comments \
  --aweme-id "<aweme_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-douyin

npx -y socialdatax-skills@latest douyin comments \
  --aweme-id "<aweme_id>" --all --include-replies --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-douyin

npx -y socialdatax-skills@latest douyin comments \
  --url "<douyin_content_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-douyin

npx -y socialdatax-skills@latest douyin replies \
  --aweme-id "<aweme_id>" --comment-id "<comment_id>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-douyin

npx -y socialdatax-skills@latest douyin user-info \
  --sec-user-id "<sec_user_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-douyin

npx -y socialdatax-skills@latest douyin user-info \
  --profile-url "<profile_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-douyin

npx -y socialdatax-skills@latest douyin user-posts \
  --sec-user-id "<sec_user_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-douyin

npx -y socialdatax-skills@latest douyin user-posts \
  --sec-user-id "<sec_user_id>" --all --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-douyin

npx -y socialdatax-skills@latest douyin user-posts \
  --profile-url "<profile_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-douyin

npx -y socialdatax-skills@latest douyin user-series \
  --sec-user-id "<sec_user_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-douyin

npx -y socialdatax-skills@latest douyin user-series \
  --sec-user-id "<sec_user_id>" --all --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-douyin

npx -y socialdatax-skills@latest douyin user-series \
  --profile-url "<profile_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-douyin
```

Optional arguments:

- `--source-client socialdatax-skills --source-platform clawhub --source-skill socialdatax-douyin`: usage attribution for this Agent Skill; keep these values unchanged when running examples from this Skill.

Use hot-search for 抖音热榜, search for 抖音数据分析 and content discovery, detail for one work, comments/replies for 评论分析和评论回复分析, user-info for 达人信息, user-posts for 达人作品, and user-series for 达人短剧/合集.
For replies, pass both `aweme_id` and the first-level `comment_id`; use `page_token` to continue pagination.

## Safety Boundary

This skill is read-only. It uses `SOCIALDATAX_API_KEY` from the user's environment at runtime. Generated Skill files do not contain API keys. It does not read local browser data or perform login, posting, liking, commenting, or account changes.

## MCP Tools

MCP tools matching the direct CLI commands above:

- `douyin_get_hot_search_list`
- `douyin_search_videos`
- `douyin_get_video_detail_by_aweme_id`
- `douyin_get_video_detail_by_url`
- `douyin_get_video_comments_by_aweme_id`
- `douyin_get_video_comments_by_url`
- `douyin_get_video_comment_replies_by_comment_id`
- `douyin_get_user_info_by_sec_user_id`
- `douyin_get_user_info_by_profile_url`
- `douyin_get_user_posted_videos_by_sec_user_id`
- `douyin_get_user_posted_videos_by_profile_url`
- `douyin_get_user_series_by_sec_user_id`
- `douyin_get_user_series_by_profile_url`

MCP-only tools not available through the direct CLI: `douyin_search_users`, `douyin_get_user_info_by_douyin_id`

## Troubleshooting

- If an SDK/dependency, npm network, Node.js/npm/npx availability, permission, or missing runtime error appears, treat it as a local runtime, dependency installation, network, or agent authorization issue, not a SocialDataX API key or business data error. If the current environment has permission, install or restore automatically. When network or execution authorization is needed, ask the user to approve or finish authorization, then continue the same command; do not use public web search as a substitute for SocialDataX data.
- For non-balance network or API errors, preserve the error message, check `SOCIALDATAX_API_KEY`, parameters, and link or ID format, then retry once when appropriate.
- If the response returns `insufficient_balance` or says the balance/credits are insufficient, do not retry repeatedly. Show the recharge URL from the error exactly as returned, then continue the same command after the user recharges.
- If the user has recharged but still sees insufficient balance, confirm `SOCIALDATAX_API_KEY` belongs to the same account that was recharged; if needed, copy a fresh API Key from the official dashboard.
