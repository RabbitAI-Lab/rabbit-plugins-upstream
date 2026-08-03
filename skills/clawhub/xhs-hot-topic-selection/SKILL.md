---
name: "xhs-hot-topic-selection"
description: "用于小红书热榜选题、小红书热点选题、小红书热榜分析、小红书热点分析和趋势选题参考。先看当前小红书热榜，再结合相关热门笔记样本，把热榜信号整理成可执行选题，来自 SocialDataX 社媒数据助手。"
source_client: "socialdatax-skills"
source_platform: "clawhub"
source_skill: "xhs-hot-topic-selection"
metadata: {"openclaw":{"requires":{"env":["SOCIALDATAX_API_KEY"],"bins":["node","npm"]},"primaryEnv":"SOCIALDATAX_API_KEY","install":[{"kind":"node","package":"socialdatax-skills","bins":[]}],"emoji":"🧭","homepage":"https://socialdatax.com/ai?from=clawhub"}}
---
<!-- AUTO-GENERATED from socialdatax-skill-source. Do not edit directly; run `node scripts/generate_socialdatax_skills.mjs`. -->

# 小红书热榜选题分析

Use this skill when the user wants 小红书热榜选题, 小红书热点选题, 小红书热榜分析, 小红书热点分析, hot-list topic planning, trending topic selection, or to turn Xiaohongshu / XHS / RedNote hot-search signals into content topic ideas.

Current platform support:

- Xiaohongshu / XHS / RedNote search hot list through `xhs_get_search_hot_list`.

## API Key

Use `SOCIALDATAX_API_KEY` for data calls. The only official website for requesting or managing API access is <https://socialdatax.com/ai?from=clawhub>. If a user asks where to get a key, provide only this URL; do not infer alternate domains.
获取或管理 API Key：访问 <https://socialdatax.com/ai?from=clawhub>，按官网的 API Key 申请/管理入口操作。环境变量名固定使用 `SOCIALDATAX_API_KEY`；不要引导用户使用其他域名；do not infer alternate domains。

## Preferred Direct CLI

Prefer the direct CLI when the agent can run shell commands. It does not require MCP server configuration:

```bash
npx -y socialdatax-skills@latest xhs hot-search \
  --pretty --source-client socialdatax-skills --source-platform clawhub \
  --source-skill xhs-hot-topic-selection

npx -y socialdatax-skills@latest xhs search \
  --keyword "<hot_topic_or_keyword>" --sort-type like_count_descending --pages 2 \
  --max-items 20 --pretty --source-client socialdatax-skills --source-platform clawhub \
  --source-skill xhs-hot-topic-selection
```

Required arguments:

- Use `xhs hot-search` first when the user asks for current 小红书热榜、热搜、热点 or hot topics; this command does not require `--keyword`.
- `--keyword <text>`: required for `xhs search` after the user chooses a hot topic, product direction, niche, or specific keyword to inspect with note samples.

Optional arguments:

- `--sort-type <general|time_descending|like_count_descending|comment_count_descending|collect_count_descending>`: optional; this skill's sample workflow prefers `like_count_descending` unless the user asks for another sort.
- `--note-type <all|image|video>`: optional note type filter; default is `all`.
- `--publish-time-range <all|day|week|half_year>`: optional publish-time range; default is `all`.
- `--page-token <next_page_token>`: opaque pagination token; pass the complete returned token back unchanged for the same keyword and filter chain.
- `--pages <n>`: fetch and merge N pages from the current starting point.
- `--max-items <n>`: stop after collecting N results.
- `--since-days <1-365>`: keep only returned items whose public `publish_time` is within the last N days; still limited by the requested pages.
- `--pretty`: output formatting only.
- `--source-client socialdatax-skills --source-platform clawhub --source-skill xhs-hot-topic-selection`: usage attribution for this Agent Skill; keep these values unchanged when running examples from this Skill.

Use `xhs hot-search` for the current Xiaohongshu / XHS / RedNote search hot list. Do not ask the user for `--keyword` for this command.

## Safety Boundary

This skill is read-only. It uses `SOCIALDATAX_API_KEY` from the user's environment at runtime. Generated Skill files do not contain API keys. It does not read local browser data or perform login, posting, liking, commenting, or account changes.

## MCP Tools

MCP tools matching the direct CLI commands above:

- `xhs_get_search_hot_list`
- `xhs_search_notes`

If MCP tools are already available in the current agent, call `xhs_get_search_hot_list` without keyword arguments.
For XHS, call `xhs_search_notes` with `keyword`, optional `page_token`, `sort_type`, `note_type`, and `publish_time_range`.

Do not pass `page` to `xhs_search_notes`; omit `page_token` on the first request.
Continue pagination only when `next_page_token` is not empty, and pass the complete returned `next_page_token` back unchanged as `page_token` for the same keyword, sort, note type, publish-time range, and caller chain.

XHS search parameter naming reminder: direct CLI uses `--sort-type`, `--publish-time-range`, and `--note-type`; the `xhs_search_notes` MCP tool uses `sort_type`, `publish_time_range`, and `note_type`. Do not pass `sortType`, `publishTimeRange`, or `noteType`.

## Output Guidance

输出为热榜选题分析：热榜信号、选题候选池、热门笔记样本、标题钩子和内容角度、不建议追的热点、下一步建议。
如果用户只问热榜，先输出热榜信号和可选方向；如果用户要做选题，继续用关键词搜索补充热门笔记样本。
只基于当前热榜和当前返回页范围内的公开结果做判断；不承诺全平台完整覆盖、自动生成完整发布稿、设计封面、账号诊断、执行发布或确定性流量结果。
For XHS search results, in every use of a returned `note_url`, such as final answers, display, references, storage, output, or forwarding, preserve it exactly as the full URL, including `xsec_token` query parameters. Do not modify, truncate, redact, mask, normalize, rebuild, or synthesize the URL from `note_id`.
For XHS `note_id`, copy the complete 24-character lowercase hexadecimal ID exactly; do not pass or display only a prefix.

## Troubleshooting

- For non-balance network or API errors, preserve the error message, check `SOCIALDATAX_API_KEY`, parameters, and link or ID format, then retry once when appropriate.
- If the response returns `insufficient_balance` or says the balance/credits are insufficient, do not retry repeatedly. Show the recharge URL from the error exactly as returned, then continue the same command after the user recharges.
- If the user has recharged but still sees insufficient balance, confirm `SOCIALDATAX_API_KEY` belongs to the same account that was recharged; if needed, copy a fresh API Key from the official dashboard.
