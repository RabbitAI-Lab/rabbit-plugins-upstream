---
name: "socialdatax-wechat-channels"
description: "用于视频号数据助手、视频号热榜、内容研究、作品详情、评论分析、创作者资料和作品列表，也支持微信公众号文章链接详情和互动统计。覆盖 WeChat Channels，来自 SocialDataX 社媒数据助手。"
source_client: "socialdatax-skills"
source_platform: "clawhub"
source_skill: "socialdatax-wechat-channels"
metadata: {"openclaw":{"requires":{"env":[],"bins":[]},"primaryEnv":"SOCIALDATAX_API_KEY","install":[{"kind":"node","package":"socialdatax-skills","bins":[]}],"emoji":"🎞️","homepage":"https://socialdatax.com/ai?from=clawhub"}}
---
<!-- AUTO-GENERATED from socialdatax-skill-source. Do not edit directly; run `node scripts/generate_socialdatax_skills.mjs`. -->

# 视频号数据助手 SocialDataX

Use this skill when the user needs a WeChat Channels / 视频号 data assistant for hot topics, content research, video or image-post details, comments, creator profiles, creator content lists, or WeChat Official Account article details and statistics from an article link.

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
npx -y socialdatax-skills@latest wechat hot-search \
  --pretty --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-wechat-channels

npx -y socialdatax-skills@latest wechat search \
  --keyword "<keyword>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-wechat-channels

npx -y socialdatax-skills@latest wechat search \
  --keyword "<keyword>" --pages 3 --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-wechat-channels

npx -y socialdatax-skills@latest wechat detail \
  --encrypted-object-id "<encrypted_object_id>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-wechat-channels

npx -y socialdatax-skills@latest wechat detail \
  --url "<wechat_work_url_or_share_text>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-wechat-channels

npx -y socialdatax-skills@latest wechat article \
  --url "<mp_article_url_or_share_text>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-wechat-channels

npx -y socialdatax-skills@latest wechat article-stats \
  --url "<mp_article_url_or_share_text>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-wechat-channels

npx -y socialdatax-skills@latest wechat comments \
  --object-id "<object_id>" --object-nonce-id "<object_nonce_id>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill socialdatax-wechat-channels

npx -y socialdatax-skills@latest wechat comments \
  --object-id "<object_id>" --object-nonce-id "<object_nonce_id>" --all \
  --include-replies --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-wechat-channels

npx -y socialdatax-skills@latest wechat comments \
  --url "<wechat_video_url_or_share_text>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-wechat-channels

npx -y socialdatax-skills@latest wechat replies \
  --object-id "<object_id>" --object-nonce-id "<object_nonce_id>" \
  --comment-id "<comment_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-wechat-channels

npx -y socialdatax-skills@latest wechat user-info \
  --user-id "<v2_finder_user_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-wechat-channels

npx -y socialdatax-skills@latest wechat user-info \
  --url "<wechat_work_url_or_share_text>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-wechat-channels

npx -y socialdatax-skills@latest wechat user-posts \
  --user-id "<v2_finder_user_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-wechat-channels

npx -y socialdatax-skills@latest wechat user-posts \
  --user-id "<v2_finder_user_id>" --all --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-wechat-channels

npx -y socialdatax-skills@latest wechat user-posts \
  --url "<wechat_work_url_or_share_text>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill socialdatax-wechat-channels
```

Required arguments:

- WeChat Channels `hot-search`: no required arguments.

Optional arguments:

- `--source-client socialdatax-skills --source-platform clawhub --source-skill socialdatax-wechat-channels`: usage attribution for this Agent Skill; keep these values unchanged when running examples from this Skill.

Use hot-search for 视频号热榜, search for 视频号内容研究, detail for one video or image post, article for a WeChat Official Account article link, article-stats for 公众号阅读和互动统计, comments/replies for 评论洞察, user-info for 创作者资料, and user-posts for 创作者作品列表.
For replies, use `object_id`, `object_nonce_id`, and the first-level `comment_id`.

## Safety Boundary

This skill is read-only. CLI calls use existing environment credentials or the user’s explicitly saved private local credential file. Generated Skill files do not contain API keys. It does not read local browser data or perform login, posting, liking, commenting, or account changes.

## MCP Tools

MCP tools matching the direct CLI commands above:

- `wechat_get_hot_search_list`
- `wechat_search_videos`
- `wechat_get_video_detail_by_encrypted_object_id`
- `wechat_get_video_detail_by_url`
- `wechat_get_mp_article_detail_by_url`
- `wechat_get_mp_article_stats_by_url`
- `wechat_get_video_comments_by_object_id`
- `wechat_get_video_comments_by_url`
- `wechat_get_video_comment_replies_by_comment_id`
- `wechat_get_user_info_by_user_id`
- `wechat_get_user_info_by_url`
- `wechat_get_user_posted_videos_by_user_id`
- `wechat_get_user_posted_videos_by_url`

## Troubleshooting

- Credential source: identify whether this request uses CLI or MCP. For CLI, run `auth status` in the actual execution environment to identify environment or local-file credentials. For MCP, check the authentication configuration of the current connection, without requiring a local CLI variable. If configuration is missing, follow the API Key section for user-entered hidden local login. Do not expose Keys, Authorization headers or secret configuration values.

- If an SDK/dependency, npm network, Node.js/npm/npx availability, permission, or missing runtime error appears, treat it as a local runtime, dependency installation, network, or agent authorization issue, not a SocialDataX API key or business data error. Install or repair task dependencies only within the user's existing authorization, preferably in the project or a temporary environment. Execution permissions are not user authorization; explain and obtain approval before changes outside that scope, including global installs, runtime upgrades, or system configuration changes. When network or execution authorization is needed, ask the user to approve or finish authorization, then continue the same command; do not use public web search as a substitute for SocialDataX data.
- If the CLI exits with status 1 and prints `partial: true`, preserve `data.items` and the error, and report incomplete results. This recovery rule overrides advice to rerun the original command. After resolving the error (including insufficient balance), resume only with a non-empty `data.next_page_token` and the same query parameters. Keep the original page and item limits: subtract cumulative `page_count` and `item_count` from the respective `--pages` and `--max-items` limits, if set. Stop parent-list pagination when either limit is reached. An empty token does not mean completion. Do not restart from the first page; investigate repeated-token errors before continuing.
- With `--include-replies`, `replies_partial` marks incomplete replies and `replies_pending` marks comments not yet expanded. Finish those comments with the platform reply command, its required comment identifiers and any non-empty `replies_next_page_token`. For pending comments or a failed first reply request, resolve the error before starting that comment from its first reply page; investigate repeated-token errors first. Then use the outer `data.next_page_token` only if the parent-comment budget remains; finishing replies under retained comments does not add parent-comment pages. Never interchange parent and reply tokens or treat reply previews as complete.
- For non-balance network or API errors, preserve the error message, check the effective credential source above, parameters, and link or ID format, then retry once when appropriate.
- If the response returns `insufficient_balance` or says the balance/credits are insufficient, do not retry repeatedly. Show the official billing link in the error (https://socialdatax.com/dashboard/billing, including any channel parameters); if absent, use https://socialdatax.com/dashboard/billing. After recharging, resume the failed call; if a job or partial results already exist, follow the corresponding job-query or pagination recovery rules.
- If the user has recharged but still sees insufficient balance, have the user confirm in the relevant account dashboard that this request uses the recharged account, following the credential source above. If an update is needed, have the user update the effective CLI configuration or MCP connection, reload as documented, and resume the original command. Do not require reconfiguration just because the primary local variable is absent, or expose credential values.
