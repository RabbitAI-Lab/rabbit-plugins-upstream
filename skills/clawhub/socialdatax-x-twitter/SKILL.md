---
name: "socialdatax-x-twitter"
description: "用于 X / Twitter 数据助手、内容搜索、帖子详情、评论分析、创作者资料和创作者帖子列表。覆盖 X post and creator research，来自 SocialDataX 社媒数据助手。"
source_client: "socialdatax-skills"
source_platform: "clawhub"
source_skill: "socialdatax-x-twitter"
metadata: {"openclaw":{"requires":{"env":["SOCIALDATAX_API_KEY"],"bins":["node","npm"]},"primaryEnv":"SOCIALDATAX_API_KEY","install":[{"kind":"node","package":"socialdatax-skills","bins":[]}],"emoji":"𝕏","homepage":"https://socialdatax.com/ai?from=clawhub"}}
---
<!-- AUTO-GENERATED from socialdatax-skill-source. Do not edit directly; run `node scripts/generate_socialdatax_skills.mjs`. -->

# X / Twitter 数据助手 SocialDataX

Use this skill when the user needs an X / Twitter data assistant for post research, post details, comments, creator profiles, or creator post lists.

## API Key

Use `SOCIALDATAX_API_KEY` for data calls. The only official website for requesting or managing API access is <https://socialdatax.com/ai?from=clawhub>. If a user asks where to get a key, provide only this URL; do not infer alternate domains.
获取或管理 API Key：访问 <https://socialdatax.com/ai?from=clawhub>，按官网的 API Key 申请/管理入口操作。环境变量名固定使用 `SOCIALDATAX_API_KEY`；不要引导用户使用其他域名。

## Preferred Direct CLI

Prefer the direct CLI when the agent can run shell commands. It does not require MCP server configuration:

```bash
npx -y socialdatax-skills@latest x search \
  --keyword "<keyword>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-x-twitter

npx -y socialdatax-skills@latest x search \
  --keyword "<keyword>" --pages 3 --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-x-twitter

npx -y socialdatax-skills@latest x detail \
  --post-id "<post_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-x-twitter

npx -y socialdatax-skills@latest x detail \
  --post-url "<x_post_url_or_share_text>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-x-twitter

npx -y socialdatax-skills@latest x comments \
  --post-id "<post_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-x-twitter

npx -y socialdatax-skills@latest x comments \
  --post-url "<x_post_url_or_share_text>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-x-twitter

npx -y socialdatax-skills@latest x replies \
  --post-id "<post_id>" --comment-id "<comment_id>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-x-twitter

npx -y socialdatax-skills@latest x user-info \
  --user-id "<user_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-x-twitter

npx -y socialdatax-skills@latest x user-info \
  --username "<username>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-x-twitter

npx -y socialdatax-skills@latest x user-info \
  --profile-url "<profile_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-x-twitter

npx -y socialdatax-skills@latest x user-posts \
  --user-id "<user_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-x-twitter

npx -y socialdatax-skills@latest x user-posts \
  --username "<username>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-x-twitter

npx -y socialdatax-skills@latest x user-posts \
  --profile-url "<profile_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-x-twitter

npx -y socialdatax-skills@latest x user-posts \
  --username "<username>" --all --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-x-twitter
```

Optional arguments:

- `--source-client socialdatax-skills --source-platform clawhub --source-skill socialdatax-x-twitter`: usage attribution for this Agent Skill; keep these values unchanged when running examples from this Skill.

Use search for X / Twitter content research, detail for one post, comments/replies for discussion analysis, user-info for creator profiles, and user-posts for creator content lists.
For replies, use the returned `post_id` together with the first-level `comment_id`.

## Safety Boundary

This skill is read-only. It uses `SOCIALDATAX_API_KEY` from the user's environment at runtime. Generated Skill files do not contain API keys. It does not read local browser data or perform login, posting, liking, commenting, or account changes.

## MCP Tools

MCP tools matching the direct CLI commands above:

- `x_search_posts`
- `x_get_post_detail_by_post_id`
- `x_get_post_detail_by_post_url`
- `x_get_post_comments_by_post_id`
- `x_get_post_comments_by_post_url`
- `x_get_post_comment_replies_by_comment_id`
- `x_get_user_info_by_user_id`
- `x_get_user_info_by_username`
- `x_get_user_info_by_profile_url`
- `x_get_user_posts_by_user_id`
- `x_get_user_posts_by_username`
- `x_get_user_posts_by_profile_url`

## Troubleshooting

- If an SDK/dependency, npm network, Node.js/npm/npx availability, permission, or missing runtime error appears, treat it as a local runtime, dependency installation, network, or agent authorization issue, not a SocialDataX API key or business data error. If the current environment has permission, install or restore automatically. When network or execution authorization is needed, ask the user to approve or finish authorization, then continue the same command; do not use public web search as a substitute for SocialDataX data.
- For non-balance network or API errors, preserve the error message, check `SOCIALDATAX_API_KEY`, parameters, and link or ID format, then retry once when appropriate.
- If the response returns `insufficient_balance` or says the balance/credits are insufficient, do not retry repeatedly. Show the recharge URL from the error exactly as returned, then continue the same command after the user recharges.
- If the user has recharged but still sees insufficient balance, confirm `SOCIALDATAX_API_KEY` belongs to the same account that was recharged; if needed, copy a fresh API Key from the official dashboard.
