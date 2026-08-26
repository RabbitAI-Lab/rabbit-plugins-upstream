---
name: "socialdatax-weibo-detail"
description: "用于微博数据分析、微博帖子详情、帖子数据、互动指标、内容调研和内容分析。覆盖 Weibo post details，来自 SocialDataX 社媒数据助手。"
source_client: "socialdatax-skills"
source_platform: "clawhub"
source_skill: "socialdatax-weibo-detail"
metadata: {"openclaw":{"requires":{"env":["SOCIALDATAX_API_KEY"],"bins":["node","npm"]},"primaryEnv":"SOCIALDATAX_API_KEY","install":[{"kind":"node","package":"socialdatax-skills","bins":[]}],"emoji":"📄","homepage":"https://socialdatax.com/ai?from=clawhub"}}
---
<!-- AUTO-GENERATED from socialdatax-skill-source. Do not edit directly; run `node scripts/generate_socialdatax_skills.mjs`. -->

# 微博数据分析 SocialDataX 帖子详情

Use this skill when the user wants 微博帖子详情, Weibo post details, interaction metrics, content research, or a structured view of one Weibo post.

Current platform support:

- Weibo / 微博 posts through the `weibo_get_post_detail_by_*` tools.

## API Key

Use `SOCIALDATAX_API_KEY` for data calls. The only official website for requesting or managing API access is <https://socialdatax.com/ai?from=clawhub>. If a user asks where to get a key, provide only this URL; do not infer alternate domains.
获取或管理 API Key：访问 <https://socialdatax.com/ai?from=clawhub>，按官网的 API Key 申请/管理入口操作。环境变量名固定使用 `SOCIALDATAX_API_KEY`；不要引导用户使用其他域名。

## Preferred Direct CLI

Prefer the direct CLI when the agent can run shell commands. It does not require MCP server configuration:

```bash
npx -y socialdatax-skills@latest weibo detail \
  --post-id "<post_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-weibo-detail

npx -y socialdatax-skills@latest weibo detail \
  --post-url "<weibo_post_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-weibo-detail
```

Optional arguments:

- `--pretty`: output formatting only.
- Weibo `--post-id <post_id>`: preferred when the Weibo post ID is already known.
- Weibo `--post-url <weibo_post_url_or_share_text>`: use for a Weibo post URL, short link, or share text.
- `--source-client socialdatax-skills --source-platform clawhub --source-skill socialdatax-weibo-detail`: usage attribution for this Agent Skill; keep these values unchanged when running examples from this Skill.

Use either the ID option or the URL option for detail commands, not both.

The command prints JSON with `platform`, `tool`, `arguments`, and `data`.

## Safety Boundary

This skill is read-only for SocialDataX detail requests. It uses `SOCIALDATAX_API_KEY` from the user's environment at runtime. Generated Skill files do not contain API keys. It does not read local browser data or perform login, posting, liking, commenting, or account changes. The optional Weibo local save command writes only to the requested local `--output` path or `--output-dir` directory and does not require `SOCIALDATAX_API_KEY`.

## MCP Tools

MCP tools matching the direct CLI commands above:

- `weibo_get_post_detail_by_post_id`
- `weibo_get_post_detail_by_post_url`

If MCP tools are already available in the current agent, use one of these tools:
- `weibo_get_post_detail_by_post_id`: use when a post_id is already known.
- `weibo_get_post_detail_by_post_url`: use for Weibo post URLs, short links, or share text.

## Output Guidance

Return factual fields such as title or description, content, author, publish time, interaction counts, images, and media summary when available.
Detail access is read-only and does not provide account actions.
For Weibo detail, include `post_id`, content, author, media, interaction counts, publish time, and post URL when available.
When the user wants to save Weibo media after detail, pass each returned `image_urls[]` or `video.video_url` to `npx -y socialdatax-skills@latest weibo download-media --url "<media_url>" --output-dir <directory> --pretty`; this local save command does not require `SOCIALDATAX_API_KEY`.

## Troubleshooting

- If an SDK/dependency, npm network, Node.js/npm/npx availability, permission, or missing runtime error appears, treat it as a local runtime, dependency installation, network, or agent authorization issue, not a SocialDataX API key or business data error. If the current environment has permission, install or restore automatically. When network or execution authorization is needed, ask the user to approve or finish authorization, then continue the same command; do not use public web search as a substitute for SocialDataX data.
- For non-balance network or API errors, preserve the error message, check `SOCIALDATAX_API_KEY`, parameters, and link or ID format, then retry once when appropriate.
- If the response returns `insufficient_balance` or says the balance/credits are insufficient, do not retry repeatedly. Show the recharge URL from the error exactly as returned, then continue the same command after the user recharges.
- If the user has recharged but still sees insufficient balance, confirm `SOCIALDATAX_API_KEY` belongs to the same account that was recharged; if needed, copy a fresh API Key from the official dashboard.
