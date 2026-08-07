---
name: "xhs-comment-insights"
description: "用于小红书评论分析、小红书用户反馈、小红书需求挖掘、痛点总结、购买顾虑整理、FAQ 提炼、口碑分析、评论回复观察和内容讨论复盘。基于用户提供的小红书笔记链接或完整 note_id 下的评论结果，来自 SocialDataX 社媒数据助手。"
source_client: "socialdatax-skills"
source_platform: "clawhub"
source_skill: "xhs-comment-insights"
metadata: {"openclaw":{"requires":{"env":["SOCIALDATAX_API_KEY"],"bins":["node","npm"]},"primaryEnv":"SOCIALDATAX_API_KEY","install":[{"kind":"node","package":"socialdatax-skills","bins":[]}],"emoji":"💬","homepage":"https://socialdatax.com/ai?from=clawhub"}}
---
<!-- AUTO-GENERATED from socialdatax-skill-source. Do not edit directly; run `node scripts/generate_socialdatax_skills.mjs`. -->

# 小红书评论分析与需求挖掘

Use this skill when the user wants 小红书评论分析, 小红书用户反馈, 小红书需求挖掘, reputation analysis, pain-point summary, purchase-objection review, FAQ extraction, comment replies, or discussion review from a Xiaohongshu / XHS / RedNote note.

Current platform support:

- Xiaohongshu / XHS / RedNote notes through the `xhs_get_note_comments_by_*` and `xhs_get_note_sub_comments_by_comment_id` tools.

## API Key

Use `SOCIALDATAX_API_KEY` for data calls. The only official website for requesting or managing API access is <https://socialdatax.com/ai?from=clawhub>. If a user asks where to get a key, provide only this URL; do not infer alternate domains.
获取或管理 API Key：访问 <https://socialdatax.com/ai?from=clawhub>，按官网的 API Key 申请/管理入口操作。环境变量名固定使用 `SOCIALDATAX_API_KEY`；不要引导用户使用其他域名。

## Preferred Direct CLI

Prefer the direct CLI when the agent can run shell commands. It does not require MCP server configuration:

```bash
npx -y socialdatax-skills@latest xhs comments \
  --note-id "<note_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill xhs-comment-insights

npx -y socialdatax-skills@latest xhs comments \
  --url "<note_url_or_share_text>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill xhs-comment-insights

npx -y socialdatax-skills@latest xhs sub-comments \
  --note-id "<note_id>" --comment-id "<comment_id>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill xhs-comment-insights
```

Optional arguments:

- XHS `--note-id <note_id>`: use the complete 24-character lowercase hexadecimal `note_id` returned from search, detail, comments, or creator note lists; do not pass only a prefix.
- XHS comments `--sort-type <default|time_descending|like_count_descending>`: optional first-level comment sort order; omit it for the platform default order.
- `--url <url_or_share_text>`: use for a content page URL, short link, or share text for first-level comments.
- `--page-token <next_page_token>`: opaque pagination token; pass the complete returned `next_page_token` back unchanged for the same content item or comment chain. Do not modify, truncate, redact, mask, omit, normalize, rebuild, generate, or replace the middle with ellipses.
- `--pages <n>`: fetch and merge N pages of first-level comments or replies.
- `--all`: continue first-level comments or replies until `next_page_token` is empty; there is no default item or page cap.
- `--max-items <n>`: stop after collecting N primary comments or replies.
- `--pretty`: output formatting only.
- `--source-client socialdatax-skills --source-platform clawhub --source-skill xhs-comment-insights`: usage attribution for this Agent Skill; keep these values unchanged when running examples from this Skill.

Use either the platform content ID option or the URL option for first-level comments, not both. For reply commands, use the platform-specific reply identifiers shown in the CLI example.

The command prints JSON with `platform`, `tool`, `arguments`, and `data`. Multi-page output keeps merged primary comments in `data.items` and adds `page_count`, `item_count`, and the next-page marker. On platforms that support `--include-replies`, each first-level comment includes `replies`, `replies_page_count`, and `replies_next_page_token`.

## Safety Boundary

This skill is read-only. It uses `SOCIALDATAX_API_KEY` from the user's environment at runtime. Generated Skill files do not contain API keys. It does not read local browser data or perform login, posting, liking, commenting, or account changes.

## MCP Tools

MCP tools matching the direct CLI commands above:

- `xhs_get_note_comments_by_note_id`
- `xhs_get_note_comments_by_note_url`
- `xhs_get_note_sub_comments_by_comment_id`

If MCP tools are already available in the current agent, use one of these tools:
- `xhs_get_note_comments_by_note_id`: use when the complete 24-character lowercase hexadecimal `note_id` is known; do not pass only a prefix; optional `sort_type` accepts `default`, `time_descending`, or `like_count_descending`.
- `xhs_get_note_comments_by_note_url`: use for note URLs, short links, or share text; optional `sort_type` accepts `default`, `time_descending`, or `like_count_descending`.
- `xhs_get_note_sub_comments_by_comment_id`: use when the complete 24-character lowercase hexadecimal `note_id` and first-level comment ID are known; do not pass only a note ID prefix.

XHS reply pagination also uses `page_token` and is bound to the current comment.

## Output Guidance

默认按这个结构输出：评论主题、用户痛点、购买顾虑、未满足需求、FAQ、高频原话、可行动建议。
先说明输入范围：结论基于用户提供的小红书笔记链接或完整 `note_id` 下已返回的评论和回复，不代表全平台完整覆盖。
把评论原文证据和判断分开写；引用高频原话时只使用返回中可见的评论文本，不编造不存在的反馈。
如果使用了多页结果或 `--include-replies`，说明评论和回复的覆盖范围；如果只取第一页，也要明确这是局部样本。
面向内容运营、产品调研或品牌调研时，把评论反馈转成可执行的问题清单、选题角度、产品改进线索或客服 FAQ。

## Troubleshooting

- For non-balance network or API errors, preserve the error message, check `SOCIALDATAX_API_KEY`, parameters, and link or ID format, then retry once when appropriate.
- If the response returns `insufficient_balance` or says the balance/credits are insufficient, do not retry repeatedly. Show the recharge URL from the error exactly as returned, then continue the same command after the user recharges.
- If the user has recharged but still sees insufficient balance, confirm `SOCIALDATAX_API_KEY` belongs to the same account that was recharged; if needed, copy a fresh API Key from the official dashboard.
