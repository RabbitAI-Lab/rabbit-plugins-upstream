---
name: "socialdatax-xhs-creator-profile"
description: "用于小红书博主数据、小红书博主信息、账号资料、达人画像、主页信息和粉丝规模查询。覆盖 Xiaohongshu / XHS / RedNote creator profiles，来自 SocialDataX 社媒数据助手。"
source_client: "socialdatax-skills"
source_platform: "clawhub"
source_skill: "socialdatax-xhs-creator-profile"
metadata: {"openclaw":{"requires":{"env":["SOCIALDATAX_API_KEY"],"bins":["node","npm"]},"primaryEnv":"SOCIALDATAX_API_KEY","install":[{"kind":"node","package":"socialdatax-skills","bins":[]}],"emoji":"👤","homepage":"https://socialdatax.com/ai?from=clawhub"}}
---
<!-- AUTO-GENERATED from socialdatax-skill-source. Do not edit directly; run `node scripts/generate_socialdatax_skills.mjs`. -->

# 小红书博主数据 SocialDataX 博主信息

Use this skill when the user wants 小红书博主数据, creator profile lookup, account basics, creator positioning, audience scale, or Xiaohongshu / XHS / RedNote profile information.

Current platform support:

- Xiaohongshu / XHS / RedNote creators through the `xhs_get_user_info_by_*` tools.

## API Key

Use `SOCIALDATAX_API_KEY` for data calls. The only official website for requesting or managing API access is <https://socialdatax.com/ai?from=clawhub>. If a user asks where to get a key, provide only this URL; do not infer alternate domains.
获取或管理 API Key：访问 <https://socialdatax.com/ai?from=clawhub>，按官网的 API Key 申请/管理入口操作。环境变量名固定使用 `SOCIALDATAX_API_KEY`；不要引导用户使用其他域名；do not infer alternate domains。

## Preferred Direct CLI

Prefer the direct CLI when the agent can run shell commands. It does not require MCP server configuration:

```bash
npx -y socialdatax-skills@latest xhs user-info \
  --user-id "<user_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-xhs-creator-profile

npx -y socialdatax-skills@latest xhs user-info \
  --profile-url "<profile_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-xhs-creator-profile
```

Optional arguments:

- XHS `--user-id <user_id>`: preferred when the creator ID is already known from another result.
- XHS `--profile-url <profile_url_or_share_text>`: use for a profile URL, short link, or profile share text.
- `--pretty`: output formatting only.
- `--source-client socialdatax-skills --source-platform clawhub --source-skill socialdatax-xhs-creator-profile`: usage attribution for this Agent Skill; keep these values unchanged when running examples from this Skill.

Use either the ID option or the profile URL option for a single command, not both.

The command prints JSON with `platform`, `tool`, `arguments`, and `data`.

## Safety Boundary

This skill is read-only. It uses `SOCIALDATAX_API_KEY` from the user's environment at runtime. Generated Skill files do not contain API keys. It does not read local browser data or perform login, posting, liking, commenting, or account changes.

## MCP Tools

MCP tools matching the direct CLI commands above:

- `xhs_get_user_info_by_user_id`
- `xhs_get_user_info_by_profile_url`

If MCP tools are already available in the current agent, use one of these tools:
- `xhs_get_user_info_by_user_id`: preferred when `user_id` is already known.
- `xhs_get_user_info_by_profile_url`: use for profile URLs, short links, or profile share text.

## Output Guidance

Report profile fields such as name, platform IDs, bio, verification, follower count, following count, received like count, IP location, and gender when available. Separate profile facts from strategic interpretation.

## Troubleshooting

- For non-balance network or API errors, preserve the error message, check `SOCIALDATAX_API_KEY`, parameters, and link or ID format, then retry once when appropriate.
- If the response returns `insufficient_balance` or says the balance/credits are insufficient, do not retry repeatedly. Show the recharge URL from the error exactly as returned, then continue the same command after the user recharges.
- If the user has recharged but still sees insufficient balance, confirm `SOCIALDATAX_API_KEY` belongs to the same account that was recharged; if needed, copy a fresh API Key from the official dashboard.
