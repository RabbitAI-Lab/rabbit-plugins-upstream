---
name: "socialdatax-xhs"
description: "用于小红书数据助手、小红书搜索热榜、小红书数据分析、小红书笔记搜索、笔记详情、评论分析、博主数据和博主笔记。覆盖 Xiaohongshu / XHS / RedNote，来自 SocialDataX 社媒数据助手。"
source_client: "socialdatax-skills"
source_platform: "clawhub"
source_skill: "socialdatax-xhs"
metadata: {"openclaw":{"requires":{"env":[],"bins":[]},"primaryEnv":"SOCIALDATAX_API_KEY","install":[{"kind":"node","package":"socialdatax-skills","bins":[]}],"emoji":"📕","homepage":"https://socialdatax.com/ai?from=clawhub"}}
---
<!-- AUTO-GENERATED from socialdatax-skill-source. Do not edit directly; run `node scripts/generate_socialdatax_skills.mjs`. -->

# 小红书数据助手 SocialDataX

Use this skill when the user needs a Xiaohongshu / 小红书 / XHS / RedNote data assistant for search hot list, content research, note search, note details, comment analysis, creator profile lookup, or creator note lists.

## API Key

Use `SOCIALDATAX_API_KEY` for data calls. The only official website for requesting or managing API access is <https://socialdatax.com/ai?from=clawhub>. If a user asks where to get a key, provide only this URL; do not infer alternate domains.
获取或管理 API Key：访问 <https://socialdatax.com/ai?from=clawhub>，按官网的 API Key 申请/管理入口操作。环境变量名固定使用 `SOCIALDATAX_API_KEY`；不要引导用户使用其他域名。
- Before a CLI call requiring an API Key, run `npx -y socialdatax-skills@latest auth status` in the actual execution environment. It makes no paid request and reports only `apiKeyReadable` and source `environment` / `file` / `null`, never the Key. Reuse working configuration; handle command, permission and malformed-file errors as reported instead of treating every failure as a missing Key. Authenticated hosted MCP keeps its current connection authentication and needs no separate local CLI setup.
- If missing, have the user obtain a Key from the official URL above and run `npx -y socialdatax-skills@latest auth login` in their own local terminal, entering it at the hidden prompt. The CLI saves it under that terminal user's home at `.config/socialdatax/credentials.json`, with mode 600 on Unix or a private current-user ACL on Windows; saving fails if permissions cannot be restricted. Never put the Key in AI chat, model-captured input, logs, screenshots, command history, Skill files or version control. The Agent must not read or display credential-file content.
- Each CLI invocation reads the private user file without depending on a client loading shell configuration or changing client/system settings. A nonempty `SOCIALDATAX_API_KEY` has priority, then the existing legacy variable, then the file. Saving a file does not replace an effective environment credential. For authentication failures, check the actual source/account and have the user correct it locally while preserving other configuration.
- After local entry, rerun `auth status` in the same environment as the business command. If false, stop business calls and check the OS user, home directory and file access. True only means readable credentials; authentication and results are determined by the original business response, without an extra paid call solely to check configuration.
- Remote/container CLI runs use the remote/container user's configuration; a local file does not transfer automatically. Use interactive login there only with an interactive terminal and persistent home; otherwise use the deployment platform's supported Secret/environment injection. Explain persistence or sandbox limits without copying Keys into chat, project files or temporary command arguments, or bypassing isolation.
- When persistence acceptance is requested, fully quit the client and background execution processes, reopen, recheck, then resume the original request. Normal use reuses verified configuration without repeated restarts or entry.

## Preferred Direct CLI

Choose the matching SocialDataX command:

```bash
npx -y socialdatax-skills@latest xhs hot-search \
  --pretty --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-xhs

npx -y socialdatax-skills@latest xhs search \
  --keyword "<keyword>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-xhs

npx -y socialdatax-skills@latest xhs search \
  --keyword "<keyword>" --pages 3 --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-xhs

npx -y socialdatax-skills@latest xhs detail \
  --note-id "<note_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-xhs

npx -y socialdatax-skills@latest xhs detail \
  --url "<note_url_or_share_text>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-xhs

npx -y socialdatax-skills@latest xhs comments \
  --note-id "<note_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-xhs

npx -y socialdatax-skills@latest xhs comments \
  --note-id "<note_id>" --all --include-replies --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-xhs

npx -y socialdatax-skills@latest xhs comments \
  --url "<note_url_or_share_text>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-xhs

npx -y socialdatax-skills@latest xhs sub-comments \
  --note-id "<note_id>" --comment-id "<comment_id>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-xhs

npx -y socialdatax-skills@latest xhs user-info \
  --user-id "<user_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-xhs

npx -y socialdatax-skills@latest xhs user-info \
  --profile-url "<profile_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-xhs

npx -y socialdatax-skills@latest xhs user-posts \
  --user-id "<user_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-xhs

npx -y socialdatax-skills@latest xhs user-posts \
  --user-id "<user_id>" --all --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-xhs

npx -y socialdatax-skills@latest xhs user-posts \
  --profile-url "<profile_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-xhs

npx -y socialdatax-skills@latest xhs search-suggestions \
  --keyword "<keyword>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-xhs
```

Required arguments:

- XHS `hot-search`: no required arguments.

Optional arguments:

- XHS comments `--sort-type <default|time_descending|like_count_descending>`: optional first-level comment sort order; omit it for the platform default order.
- `--source-client socialdatax-skills --source-platform clawhub --source-skill socialdatax-xhs`: usage attribution for this Agent Skill; keep these values unchanged when running examples from this Skill.

Use hot-search for 小红书搜索热榜, search for 小红书数据分析 and note discovery, detail for one note, comments for comment analysis and replies, user-info for 博主信息, and user-posts for 博主笔记.
For XHS keyword completion, use `xhs_search_suggestions`; use `xhs search` or `xhs_search_notes` when the user needs note results instead of suggestions.

## Safety Boundary

This skill is read-only. CLI calls use existing environment credentials or the user’s explicitly saved private local credential file. Generated Skill files do not contain API keys. It does not read local browser data or perform login, posting, liking, commenting, or account changes.

## MCP Tools

MCP tools matching the direct CLI commands above:

- `xhs_get_search_hot_list`
- `xhs_search_notes`
- `xhs_get_note_detail_by_note_id`
- `xhs_get_note_detail_by_note_url`
- `xhs_get_note_comments_by_note_id`
- `xhs_get_note_comments_by_note_url`
- `xhs_get_note_sub_comments_by_comment_id`
- `xhs_get_user_info_by_user_id`
- `xhs_get_user_info_by_profile_url`
- `xhs_get_user_posted_notes_by_user_id`
- `xhs_get_user_posted_notes_by_profile_url`
- `xhs_search_suggestions`

XHS search parameter naming reminder: direct CLI uses `--sort-type`, `--publish-time-range`, and `--note-type`; the `xhs_search_notes` MCP tool uses `sort_type`, `publish_time_range`, and `note_type`. Do not pass `sortType`, `publishTimeRange`, or `noteType`.

## Output Guidance

For XHS search or detail results, in every use of a returned `note_url`, such as final answers, display, references, storage, output, or forwarding, preserve it exactly as the full URL, including `xsec_token` query parameters. Do not modify, truncate, redact, mask, normalize, rebuild, or synthesize the URL from `note_id`; if detail `note_url` is null, show the `note_id` or say that no directly openable full link is available.
For XHS `note_id`, copy the entire returned `note_id` exactly; do not pass or display only a prefix.

## Troubleshooting

- Credential source: identify whether this request uses CLI or MCP. For CLI, run `auth status` in the actual execution environment to identify environment or local-file credentials. For MCP, check the authentication configuration of the current connection, without requiring a local CLI variable. If configuration is missing, follow the API Key section for user-entered hidden local login. Do not expose Keys, Authorization headers or secret configuration values.

- If an SDK/dependency, npm network, Node.js/npm/npx availability, permission, or missing runtime error appears, treat it as a local runtime, dependency installation, network, or agent authorization issue, not a SocialDataX API key or business data error. Install or repair task dependencies only within the user's existing authorization, preferably in the project or a temporary environment. Execution permissions are not user authorization; explain and obtain approval before changes outside that scope, including global installs, runtime upgrades, or system configuration changes. When network or execution authorization is needed, ask the user to approve or finish authorization, then continue the same command; do not use public web search as a substitute for SocialDataX data.
- If the CLI exits with status 1 and prints `partial: true`, preserve `data.items` and the error, and report incomplete results. This recovery rule overrides advice to rerun the original command. After resolving the error (including insufficient balance), resume only with a non-empty `data.next_page_token` and the same query parameters. Keep the original page and item limits: subtract cumulative `page_count` and `item_count` from the respective `--pages` and `--max-items` limits, if set. Stop parent-list pagination when either limit is reached. An empty token does not mean completion. Do not restart from the first page; investigate repeated-token errors before continuing.
- With `--include-replies`, `replies_partial` marks incomplete replies and `replies_pending` marks comments not yet expanded. Finish those comments with the platform reply command, its required comment identifiers and any non-empty `replies_next_page_token`. For pending comments or a failed first reply request, resolve the error before starting that comment from its first reply page; investigate repeated-token errors first. Then use the outer `data.next_page_token` only if the parent-comment budget remains; finishing replies under retained comments does not add parent-comment pages. Never interchange parent and reply tokens or treat reply previews as complete.
- For non-balance network or API errors, preserve the error message, check the effective credential source above, parameters, and link or ID format, then retry once when appropriate.
- If the response returns `insufficient_balance` or says the balance/credits are insufficient, do not retry repeatedly. Show the official billing link in the error (https://socialdatax.com/dashboard/billing, including any channel parameters); if absent, use https://socialdatax.com/dashboard/billing. After recharging, resume the failed call; if a job or partial results already exist, follow the corresponding job-query or pagination recovery rules.
- If the user has recharged but still sees insufficient balance, have the user confirm in the relevant account dashboard that this request uses the recharged account, following the credential source above. If an update is needed, have the user update the effective CLI configuration or MCP connection, reload as documented, and resume the original command. Do not require reconfiguration just because the primary local variable is absent, or expose credential values.
