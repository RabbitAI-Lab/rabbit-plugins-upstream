---
name: "socialdatax-xhs-detail"
description: "用于小红书数据分析、小红书笔记详情、笔记数据、互动指标、内容调研和内容分析。覆盖 Xiaohongshu / XHS / RedNote note details，来自 SocialDataX 社媒数据助手。"
source_client: "socialdatax-skills"
source_platform: "clawhub"
source_skill: "socialdatax-xhs-detail"
metadata: {"openclaw":{"requires":{"env":["SOCIALDATAX_API_KEY"],"bins":["node","npm"]},"primaryEnv":"SOCIALDATAX_API_KEY","install":[{"kind":"node","package":"socialdatax-skills","bins":[]}],"emoji":"📄","homepage":"https://socialdatax.com/ai?from=clawhub"}}
---
<!-- AUTO-GENERATED from socialdatax-skill-source. Do not edit directly; run `node scripts/generate_socialdatax_skills.mjs`. -->

# 小红书数据分析 SocialDataX 笔记详情

Use this skill when the user wants 小红书笔记详情, Xiaohongshu / XHS / RedNote note details, note metrics, content analysis, or a structured view of one note.

Current platform support:

- Xiaohongshu / XHS / RedNote notes through the `xhs_get_note_detail_by_*` tools.

## API Key

Use `SOCIALDATAX_API_KEY` for data calls. The only official website for requesting or managing API access is <https://socialdatax.com/ai?from=clawhub>. If a user asks where to get a key, provide only this URL; do not infer alternate domains.
获取或管理 API Key：访问 <https://socialdatax.com/ai?from=clawhub>，按官网的 API Key 申请/管理入口操作。环境变量名固定使用 `SOCIALDATAX_API_KEY`；不要引导用户使用其他域名。

## Preferred Direct CLI

Prefer the direct CLI when the agent can run shell commands. It does not require MCP server configuration:

```bash
npx -y socialdatax-skills@latest xhs detail \
  --note-id "<note_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-xhs-detail

npx -y socialdatax-skills@latest xhs detail \
  --url "<note_url_or_share_text>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-xhs-detail
```

Optional arguments:

- XHS `--note-id <note_id>`: use the complete 24-character lowercase hexadecimal `note_id` returned from search, comments, creator note lists, or a previous detail result; do not pass only a prefix.
- XHS `--url <note_url_or_share_text>`: use for a note link, short link, or share text.
- `--pretty`: output formatting only.
- `--source-client socialdatax-skills --source-platform clawhub --source-skill socialdatax-xhs-detail`: usage attribution for this Agent Skill; keep these values unchanged when running examples from this Skill.

Use either the ID option or the URL option for detail commands, not both.

The command prints JSON with `platform`, `tool`, `arguments`, and `data`.

## Safety Boundary

This skill is read-only for SocialDataX detail requests. It uses `SOCIALDATAX_API_KEY` from the user's environment at runtime. Generated Skill files do not contain API keys. It does not read local browser data or perform login, posting, liking, commenting, or account changes. The optional XHS local save command writes only to the requested local `--output` path or `--output-dir` directory and does not require `SOCIALDATAX_API_KEY`.

## MCP Tools

MCP tools matching the direct CLI commands above:

- `xhs_get_note_detail_by_note_id`
- `xhs_get_note_detail_by_note_url`

If MCP tools are already available in the current agent, use one of these tools:
- `xhs_get_note_detail_by_note_id`: use when the complete 24-character lowercase hexadecimal `note_id` is already known; do not pass only a prefix.
- `xhs_get_note_detail_by_note_url`: use for note URLs, short links, or share text.

## Output Guidance

Return factual fields such as title or description, content, author, publish time, interaction counts, images, and media summary when available.
For XHS detail results, in every use of a returned `note_url`, such as final answers, display, references, storage, output, or forwarding, preserve it exactly as the full URL, including `xsec_token` query parameters. Do not modify, truncate, redact, mask, normalize, rebuild, or synthesize the URL from `note_id`; if `note_url` is null, show the `note_id` or say that no directly openable full link is available.
For XHS `note_id`, copy the complete 24-character lowercase hexadecimal ID exactly; do not pass or display only a prefix.
When the user wants to save XHS images or videos after detail, pass each returned `image_items[].image_url`, `image_items[].live_photo.video_url`, or `video.video_url` to `npx -y socialdatax-skills@latest xhs download-media --url "<media_url>" --output-dir <directory> --pretty`; this local save command does not require `SOCIALDATAX_API_KEY`.
Detail access is read-only and does not provide account actions.

## Troubleshooting

- For non-balance network or API errors, preserve the error message, check `SOCIALDATAX_API_KEY`, parameters, and link or ID format, then retry once when appropriate.
- If the response returns `insufficient_balance` or says the balance/credits are insufficient, do not retry repeatedly. Show the recharge URL from the error exactly as returned, then continue the same command after the user recharges.
- If the user has recharged but still sees insufficient balance, confirm `SOCIALDATAX_API_KEY` belongs to the same account that was recharged; if needed, copy a fresh API Key from the official dashboard.
