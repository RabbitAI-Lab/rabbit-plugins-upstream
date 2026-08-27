---
name: "socialdatax-weibo-comments"
description: "用于微博评论分析、微博评论回复、微博评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Weibo comments and comment replies，来自 SocialDataX 社媒数据助手。"
source_client: "socialdatax-skills"
source_platform: "clawhub"
source_skill: "socialdatax-weibo-comments"
metadata: {"openclaw":{"requires":{"env":["SOCIALDATAX_API_KEY"],"bins":["node","npm"]},"primaryEnv":"SOCIALDATAX_API_KEY","install":[{"kind":"node","package":"socialdatax-skills","bins":[]}],"emoji":"💬","homepage":"https://socialdatax.com/ai?from=clawhub"}}
---
<!-- AUTO-GENERATED from socialdatax-skill-source. Do not edit directly; run `node scripts/generate_socialdatax_skills.mjs`. -->

# 微博评论分析 SocialDataX 评论洞察

Use this skill when the user wants 微博评论分析, Weibo first-level comments, comment replies, audience feedback, sentiment themes, objections, pain points, FAQ extraction, or discussion summaries.

Current platform support:

- Weibo / 微博 posts through the `weibo_get_post_comments_by_*` and `weibo_get_post_comment_replies_by_comment_id` tools.

## API Key

Use `SOCIALDATAX_API_KEY` for data calls. The only official website for requesting or managing API access is <https://socialdatax.com/ai?from=clawhub>. If a user asks where to get a key, provide only this URL; do not infer alternate domains.
获取或管理 API Key：访问 <https://socialdatax.com/ai?from=clawhub>，按官网的 API Key 申请/管理入口操作。环境变量名固定使用 `SOCIALDATAX_API_KEY`；不要引导用户使用其他域名。

## Preferred Direct CLI

Prefer the direct CLI when the agent can run shell commands. It does not require MCP server configuration:

```bash
npx -y socialdatax-skills@latest weibo comments \
  --post-id "<post_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-weibo-comments

npx -y socialdatax-skills@latest weibo comments \
  --post-url "<weibo_post_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-weibo-comments

npx -y socialdatax-skills@latest weibo replies \
  --post-id "<post_id>" --comment-id "<comment_id>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-weibo-comments
```

Optional arguments:

- Use the URL entrypoint shown in the CLI example for a content page URL, short link, or share text for first-level comments.
- `--page-token <next_page_token>`: opaque pagination token; pass the complete returned `next_page_token` back unchanged for the same content item or comment chain. Do not modify, truncate, redact, mask, omit, normalize, rebuild, generate, or replace the middle with ellipses.
- `--pages <n>`: fetch and merge N pages of first-level comments or replies.
- `--all`: continue first-level comments or replies until `next_page_token` is empty; there is no default item or page cap.
- `--max-items <n>`: stop after collecting N primary comments or replies.
- `--pretty`: output formatting only.
- Weibo `--post-id <post_id>`: preferred when the Weibo post ID is already known and should anchor the comment thread.
- Weibo `--post-url <weibo_post_url_or_share_text>`: use for a Weibo post URL, short link, or share text for first-level comments.
- `--source-client socialdatax-skills --source-platform clawhub --source-skill socialdatax-weibo-comments`: usage attribution for this Agent Skill; keep these values unchanged when running examples from this Skill.

Use one first-level comment entrypoint shown in the CLI example at a time; do not mix multiple content identifiers in one command. For reply commands, use the platform-specific reply identifiers shown in the CLI example.

The command prints JSON with `platform`, `tool`, `arguments`, and `data`. Multi-page output keeps merged primary comments in `data.items` and adds `page_count`, `item_count`, and the next-page marker. On platforms that support `--include-replies`, each first-level comment includes `replies`, `replies_page_count`, and `replies_next_page_token`.

## Safety Boundary

This skill is read-only. It uses `SOCIALDATAX_API_KEY` from the user's environment at runtime. Generated Skill files do not contain API keys. It does not read local browser data or perform login, posting, liking, commenting, or account changes.

## MCP Tools

MCP tools matching the direct CLI commands above:

- `weibo_get_post_comments_by_post_id`
- `weibo_get_post_comments_by_post_url`
- `weibo_get_post_comment_replies_by_comment_id`

If MCP tools are already available in the current agent, use one of these tools:
- `weibo_get_post_comments_by_post_id`: use when the post_id is known.
- `weibo_get_post_comments_by_post_url`: use for Weibo post URLs, short links, or share text.
- `weibo_get_post_comment_replies_by_comment_id`: use when the post_id and first-level comment ID are known.

- Comment pagination uses opaque `page_token` values. Pass the complete returned `next_page_token` back unchanged for the same content item or first-level comment chain. Do not modify, truncate, redact, mask, omit, normalize, rebuild, generate, or replace the middle with ellipses. Continue only when `next_page_token` is non-empty.

## Output Guidance

Group comments by observed themes before inferring sentiment or demand. Mention whether the result is one page or multiple pages. Empty comments can be a valid successful result.

## Troubleshooting

- If an SDK/dependency, npm network, Node.js/npm/npx availability, permission, or missing runtime error appears, treat it as a local runtime, dependency installation, network, or agent authorization issue, not a SocialDataX API key or business data error. If the current environment has permission, install or restore automatically. When network or execution authorization is needed, ask the user to approve or finish authorization, then continue the same command; do not use public web search as a substitute for SocialDataX data.
- For non-balance network or API errors, preserve the error message, check `SOCIALDATAX_API_KEY`, parameters, and link or ID format, then retry once when appropriate.
- If the response returns `insufficient_balance` or says the balance/credits are insufficient, do not retry repeatedly. Show the recharge URL from the error exactly as returned, then continue the same command after the user recharges.
- If the user has recharged but still sees insufficient balance, confirm `SOCIALDATAX_API_KEY` belongs to the same account that was recharged; if needed, copy a fresh API Key from the official dashboard.
