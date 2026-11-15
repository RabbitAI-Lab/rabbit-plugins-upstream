---
name: "socialdatax-x-twitter"
description: "用于 X / Twitter 内容搜索、帖子详情、评论分析、创作者资料、帖子列表及博主发出的回复（含自回复）。覆盖 X post and creator research，来自 SocialDataX 社媒数据助手。"
source_client: "socialdatax-skills"
source_platform: "clawhub"
source_skill: "socialdatax-x-twitter"
metadata: {"openclaw":{"requires":{"env":[],"bins":[]},"primaryEnv":"SOCIALDATAX_API_KEY","install":[{"kind":"node","package":"socialdatax-skills","bins":[]}],"emoji":"𝕏","homepage":"https://socialdatax.com/ai?from=clawhub"}}
---
<!-- AUTO-GENERATED from socialdatax-skill-source. Do not edit directly; run `node scripts/generate_socialdatax_skills.mjs`. -->

# X / Twitter 数据助手 SocialDataX

Use this skill when the user needs an X / Twitter data assistant for post research, post details, comments, creator profiles, or creator post lists. Also use for replies authored by an X creator, including self-replies.

Current platform support:

- X / Twitter replies authored by a creator through `x_get_user_replies_by_*`, including self-replies.

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

npx -y socialdatax-skills@latest x user-replies \
  --user-id "<user_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-x-twitter

npx -y socialdatax-skills@latest x user-replies \
  --username "<username>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-x-twitter

npx -y socialdatax-skills@latest x user-replies \
  --profile-url "<profile_url>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-x-twitter
```

Optional arguments:

- `--source-client socialdatax-skills --source-platform clawhub --source-skill socialdatax-x-twitter`: usage attribution for this Agent Skill; keep these values unchanged when running examples from this Skill.

Use search for X / Twitter content research, detail for one post, comments/replies for discussion analysis, user-info for creator profiles, and user-posts for creator content lists.
For replies, use the returned `post_id` together with the first-level `comment_id`.
X creator replies: use `x user-replies` for replies authored by the creator, including self-replies; use `x comments` or `x replies` for discussions under a post. Choose exactly one of `--user-id`, `--username`, or `--profile-url`. Keep identity and the full returned token unchanged; `user-posts` tokens cannot be reused. An empty page with a nonempty token can continue. `--since-days` is not supported.

## Safety Boundary

This skill is read-only. CLI calls use existing environment credentials or the user’s explicitly saved private local credential file. Generated Skill files do not contain API keys. It does not read local browser data or perform login, posting, liking, commenting, or account changes.

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
- `x_get_user_replies_by_user_id`
- `x_get_user_replies_by_username`
- `x_get_user_replies_by_profile_url`

## Troubleshooting

- Credential source: identify whether this request uses CLI or MCP. For CLI, run `auth status` in the actual execution environment to identify environment or local-file credentials. For MCP, check the authentication configuration of the current connection, without requiring a local CLI variable. If configuration is missing, follow the API Key section for user-entered hidden local login. Do not expose Keys, Authorization headers or secret configuration values.

- If an SDK/dependency, npm network, Node.js/npm/npx availability, permission, or missing runtime error appears, treat it as a local runtime, dependency installation, network, or agent authorization issue, not a SocialDataX API key or business data error. Install or repair task dependencies only within the user's existing authorization, preferably in the project or a temporary environment. Execution permissions are not user authorization; explain and obtain approval before changes outside that scope, including global installs, runtime upgrades, or system configuration changes. When network or execution authorization is needed, ask the user to approve or finish authorization, then continue the same command; do not use public web search as a substitute for SocialDataX data.
- If the CLI exits with status 1 and prints `partial: true`, preserve `data.items` and the error, and report incomplete results. This recovery rule overrides advice to rerun the original command. After resolving the error (including insufficient balance), resume only with a non-empty `data.next_page_token` and the same query parameters. Keep the original page and item limits: subtract cumulative `page_count` and `item_count` from the respective `--pages` and `--max-items` limits, if set. Stop parent-list pagination when either limit is reached. An empty token does not mean completion. Do not restart from the first page; investigate repeated-token errors before continuing.
- For non-balance network or API errors, preserve the error message, check the effective credential source above, parameters, and link or ID format, then retry once when appropriate.
- If the response returns `insufficient_balance` or says the balance/credits are insufficient, do not retry repeatedly. Show the official billing link in the error (https://socialdatax.com/dashboard/billing, including any channel parameters); if absent, use https://socialdatax.com/dashboard/billing. After recharging, resume the failed call; if a job or partial results already exist, follow the corresponding job-query or pagination recovery rules.
- If the user has recharged but still sees insufficient balance, have the user confirm in the relevant account dashboard that this request uses the recharged account, following the credential source above. If an update is needed, have the user update the effective CLI configuration or MCP connection, reload as documented, and resume the original command. Do not require reconfiguration just because the primary local variable is absent, or expose credential values.
