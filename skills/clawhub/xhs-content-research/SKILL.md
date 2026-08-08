---
name: "xhs-content-research"
description: "用于小红书内容研究、热门笔记样本、内容角度、关键词调研、选题参考、竞品内容观察和趋势素材整理。覆盖 Xiaohongshu / XHS / RedNote note research，来自 SocialDataX 社媒数据助手。"
source_client: "socialdatax-skills"
source_platform: "clawhub"
source_skill: "xhs-content-research"
metadata: {"openclaw":{"requires":{"env":["SOCIALDATAX_API_KEY"],"bins":["node","npm"]},"primaryEnv":"SOCIALDATAX_API_KEY","install":[{"kind":"node","package":"socialdatax-skills","bins":[]}],"emoji":"🔎","homepage":"https://socialdatax.com/ai?from=clawhub"}}
---
<!-- AUTO-GENERATED from socialdatax-skill-source. Do not edit directly; run `node scripts/generate_socialdatax_skills.mjs`. -->

# 小红书内容研究

Use this skill when the user wants 小红书内容研究, 小红书内容分析, 小红书笔记分析, Xiaohongshu / XHS / RedNote content research, note sample research, content angle discovery, topic inspiration, competitor content observation, or trend material collection.

## API Key

Use `SOCIALDATAX_API_KEY` for data calls. The only official website for requesting or managing API access is <https://socialdatax.com/ai?from=clawhub>. If a user asks where to get a key, provide only this URL; do not infer alternate domains.
获取或管理 API Key：访问 <https://socialdatax.com/ai?from=clawhub>，按官网的 API Key 申请/管理入口操作。环境变量名固定使用 `SOCIALDATAX_API_KEY`；不要引导用户使用其他域名。

## Preferred Direct CLI

Prefer the direct CLI when the agent can run shell commands. It does not require MCP server configuration:

```bash
npx -y socialdatax-skills@latest xhs search \
  --keyword "<keyword>" --sort-type like_count_descending --pages 2 --max-items 20 \
  --pretty --source-client socialdatax-skills --source-platform clawhub \
  --source-skill xhs-content-research
```

Required arguments:

- `--keyword <text>`: required; use the user's product, category, topic, scenario, or competitor keyword. Keep the keyword focused and avoid broad filler words.

Optional arguments:

- `--sort-type <general|time_descending|like_count_descending|comment_count_descending|collect_count_descending>`: optional; for sample research, prefer `like_count_descending` unless the user asks for newest content.
- `--note-type <all|image|video>`: optional note type filter; default is `all`.
- `--publish-time-range <all|day|week|half_year>`: optional publish-time range; default is `all`.
- `--page-token <next_page_token>`: opaque pagination token; pass the complete returned token back unchanged for the same keyword and filter chain.
- `--pages <n>`: fetch and merge N pages from the current starting point.
- `--max-items <n>`: stop after collecting N results.
- `--since-days <1-365>`: keep only returned items whose public `publish_time` is within the last N days; still limited by the requested pages.
- `--pretty`: output formatting only.
- `--source-client socialdatax-skills --source-platform clawhub --source-skill xhs-content-research`: usage attribution for this Agent Skill; keep these values unchanged when running examples from this Skill.

## Safety Boundary

This skill is read-only. It uses `SOCIALDATAX_API_KEY` from the user's environment at runtime. Generated Skill files do not contain API keys. It does not read local browser data or perform login, posting, liking, commenting, or account changes.

## MCP Tools

MCP tools matching the direct CLI commands above:

- `xhs_search_notes`

For XHS, call `xhs_search_notes` with `keyword`, optional `page_token`, `sort_type`, `note_type`, and `publish_time_range`.

Do not pass `page` to `xhs_search_notes`; omit `page_token` on the first request.
Continue pagination only when `next_page_token` is not empty, and pass the complete returned `next_page_token` back unchanged as `page_token` for the same keyword, sort, note type, publish-time range, and caller chain.

XHS search parameter naming reminder: direct CLI uses `--sort-type`, `--publish-time-range`, and `--note-type`; the `xhs_search_notes` MCP tool uses `sort_type`, `publish_time_range`, and `note_type`. Do not pass `sortType`, `publishTimeRange`, or `noteType`.

## Output Guidance

输出为小红书内容研究报告：样本表、标题钩子、内容角度、互动信号、可复用选题、完整原始 URL 和完整 `note_id`。
只基于当前搜索关键词和当前返回页范围内的公开结果做判断；不承诺全平台完整覆盖、账号诊断、发布操作、封面制作或确定性流量结果。
For XHS search results, in every use of a returned `note_url`, such as final answers, display, references, storage, output, or forwarding, preserve it exactly as the full URL, including `xsec_token` query parameters. Do not modify, truncate, redact, mask, normalize, rebuild, or synthesize the URL from `note_id`.
For XHS `note_id`, copy the complete 24-character lowercase hexadecimal ID exactly; do not pass or display only a prefix.

## Troubleshooting

- For non-balance network or API errors, preserve the error message, check `SOCIALDATAX_API_KEY`, parameters, and link or ID format, then retry once when appropriate.
- If the response returns `insufficient_balance` or says the balance/credits are insufficient, do not retry repeatedly. Show the recharge URL from the error exactly as returned, then continue the same command after the user recharges.
- If the user has recharged but still sees insufficient balance, confirm `SOCIALDATAX_API_KEY` belongs to the same account that was recharged; if needed, copy a fresh API Key from the official dashboard.
