---
name: "socialdatax-douyin-detail"
description: "用于抖音数据分析、抖音作品详情、图文详情、作品数据、互动指标、内容调研和内容分析。覆盖 Douyin work details，来自 SocialDataX 社媒数据助手。"
source_client: "socialdatax-skills"
source_platform: "clawhub"
source_skill: "socialdatax-douyin-detail"
metadata: {"openclaw":{"requires":{"env":["SOCIALDATAX_API_KEY"],"bins":["node","npm"]},"primaryEnv":"SOCIALDATAX_API_KEY","install":[{"kind":"node","package":"socialdatax-skills","bins":[]}],"emoji":"📄","homepage":"https://socialdatax.com/ai?from=clawhub"}}
---
<!-- AUTO-GENERATED from socialdatax-skill-source. Do not edit directly; run `node scripts/generate_socialdatax_skills.mjs`. -->

# 抖音数据分析 SocialDataX 作品详情

Use this skill when the user wants 抖音作品详情, Douyin work details, image/text post details, interaction metrics, content research, or a structured view of one Douyin work.

Current platform support:

- Douyin / 抖音 works, including video and image/text posts, through the `douyin_get_video_detail_by_*` tools.

## API Key

Use `SOCIALDATAX_API_KEY` for data calls. The only official website for requesting or managing API access is <https://socialdatax.com/ai?from=clawhub>. If a user asks where to get a key, provide only this URL; do not infer alternate domains.
获取或管理 API Key：访问 <https://socialdatax.com/ai?from=clawhub>，按官网的 API Key 申请/管理入口操作。环境变量名固定使用 `SOCIALDATAX_API_KEY`；不要引导用户使用其他域名。

## Preferred Direct CLI

Prefer the direct CLI when the agent can run shell commands. It does not require MCP server configuration:

```bash
npx -y socialdatax-skills@latest douyin detail \
  --aweme-id "<aweme_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-douyin-detail

npx -y socialdatax-skills@latest douyin detail \
  --url "<douyin_content_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-douyin-detail
```

Optional arguments:

- Douyin `--aweme-id <aweme_id>`: preferred when the Douyin work ID is already known.
- Douyin `--url <douyin_content_url_or_share_text>`: use for a Douyin content page URL, short link, or share text; do not pass `video.play_url`.
- `--pretty`: output formatting only.
- `--source-client socialdatax-skills --source-platform clawhub --source-skill socialdatax-douyin-detail`: usage attribution for this Agent Skill; keep these values unchanged when running examples from this Skill.

Use either the ID option or the URL option for detail commands, not both.

The command prints JSON with `platform`, `tool`, `arguments`, and `data`.

## Safety Boundary

This skill is read-only for SocialDataX detail requests. It uses `SOCIALDATAX_API_KEY` from the user's environment at runtime. Generated Skill files do not contain API keys. It does not read local browser data or perform login, posting, liking, commenting, or account changes. The optional Douyin local save command writes only to the requested local `--output` path or `--output-dir` directory and does not require `SOCIALDATAX_API_KEY`.

## MCP Tools

MCP tools matching the direct CLI commands above:

- `douyin_get_video_detail_by_aweme_id`
- `douyin_get_video_detail_by_url`

If MCP tools are already available in the current agent, use one of these tools:
- `douyin_get_video_detail_by_aweme_id`: use when an aweme_id is already known.
- `douyin_get_video_detail_by_url`: use for Douyin content page URLs, short links, or share text; do not pass playback URLs such as `video.play_url`.

## Output Guidance

Return factual fields such as title or description, content, author, publish time, interaction counts, images, and media summary when available.
For Douyin detail, include `content_type` when available.
For Douyin detail, use `images` for image/text posts; `video` is the platform player resource and may be audio for image/text posts; `music` is the bound music or original-sound asset.
When the user wants to save Douyin media after detail, pass each returned `images[].url`, `images[].live_photo.play_url`, `video.play_url`, `music.play_url`, or `cover_image_url` to `npx -y socialdatax-skills@latest douyin download-media --url "<media_url>" --output-dir <directory> --pretty`; this local save command does not require `SOCIALDATAX_API_KEY`.
Detail access is read-only and does not provide account actions.

## Troubleshooting

- If an SDK/dependency, npm network, Node.js/npm/npx availability, permission, or missing runtime error appears, treat it as a local runtime, dependency installation, network, or agent authorization issue, not a SocialDataX API key or business data error. If the current environment has permission, install or restore automatically. When network or execution authorization is needed, ask the user to approve or finish authorization, then continue the same command; do not use public web search as a substitute for SocialDataX data.
- For non-balance network or API errors, preserve the error message, check `SOCIALDATAX_API_KEY`, parameters, and link or ID format, then retry once when appropriate.
- If the response returns `insufficient_balance` or says the balance/credits are insufficient, do not retry repeatedly. Show the recharge URL from the error exactly as returned, then continue the same command after the user recharges.
- If the user has recharged but still sees insufficient balance, confirm `SOCIALDATAX_API_KEY` belongs to the same account that was recharged; if needed, copy a fresh API Key from the official dashboard.
