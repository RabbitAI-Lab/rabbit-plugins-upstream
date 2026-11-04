---
name: "douyin-video-copy-extract"
description: "用于抖音文案提取、抖音文案一键提取、抖音视频文案提取、抖音视频转文字、抖音口播转文字和抖音逐字稿。用户粘贴抖音视频链接、分享文案或 aweme_id 后，提取视频上下文、原视频简介和口播逐字稿，来自 SocialDataX 社媒数据助手。"
source_client: "socialdatax-skills"
source_platform: "clawhub"
source_skill: "douyin-video-copy-extract"
metadata: {"openclaw":{"requires":{"env":[],"bins":[]},"primaryEnv":"SOCIALDATAX_API_KEY","install":[{"kind":"node","package":"socialdatax-skills","bins":[]}],"emoji":"🎙️","homepage":"https://socialdatax.com/ai?from=clawhub"}}
---
<!-- AUTO-GENERATED from socialdatax-skill-source. Do not edit directly; run `node scripts/generate_socialdatax_skills.mjs`. -->

# 抖音文案提取

Use this skill when the user wants 抖音文案提取, 抖音文案一键提取, 抖音视频文案提取, 抖音视频转文字, 抖音口播转文字, 抖音逐字稿, Douyin transcript extraction, spoken copy extraction, or to check a Douyin transcript job.

Current platform support:

- Douyin / 抖音 video work speech-to-text transcript jobs through the `douyin_*video_speech_text*` tools.

## API Key

Use `SOCIALDATAX_API_KEY` for data calls. The only official website for requesting or managing API access is <https://socialdatax.com/ai?from=clawhub>. If a user asks where to get a key, provide only this URL; do not infer alternate domains.
获取或管理 API Key：访问 <https://socialdatax.com/ai?from=clawhub>，按官网的 API Key 申请/管理入口操作。环境变量名固定使用 `SOCIALDATAX_API_KEY`；不要引导用户使用其他域名。
- Identify the invocation route and actual command execution environment first. Authenticated hosted MCP needs no local CLI variable or Node/npm. For direct CLI calls requiring a Key, run the probe below in the same execution environment; if readable, resume the task without overwriting existing configuration. An unavailable command tool or missing Node.js is an execution-environment issue, not evidence of a missing Key. Direct the user to the official URL above only when they confirm they have no Key.
- Local Agent: prefer the client's documented persistent Secret / env that injects into Agent command processes. In WorkBuddy merge `{"env":{"SOCIALDATAX_API_KEY":"<YOUR_API_KEY>"}}` into `.codebuddy/settings.local.json` in the current trusted workspace, preserving other settings and env entries. This path is WorkBuddy-specific and workspace-scoped. Have the user enter the real Key locally and keep the file out of version control.
- Remote Agent: configure the client's persistent Secret / env on the remote host or service that actually executes commands, reload its execution process as documented, then probe in that same remote session. Local machine environment variables do not automatically transfer to the remote host; a successful local probe does not establish remote access.
- Container or cloud sandbox Agent: prefer the platform's persistent Secret / environment injection into the actual CLI container or sandbox. Recreate or reload it as documented and probe inside it. Host-machine variables are not a substitute for sandbox injection. If the platform cannot persist or inject variables, explain the limitation and use a platform-supported authentication route without bypassing isolation.
- When the probe is false, first check the configuration/Secret host, workspace and scope, workspace trust, correct fields and preserved existing settings, injection into command processes (MCP-server-only env is insufficient), and the documented reload or full restart. Correct these and recheck in the original execution environment. Use that environment's documented user/service environment fallback only after confirming client persistence is unsupported or exhausting these checks; one failed probe or reload alone is not grounds to switch to OS configuration.
- Apply OS fallback on the actual execution host: Windows user environment variables are an option. On macOS the user can read a Key via hidden local terminal input (for example Bash `read -s`) and pass it to `launchctl setenv`; this is login-session-only and needs reloading after login/computer restart. On input failure, empty input or setup failure, report an explicit error and stop with a nonzero exit status; temporary-variable cleanup must preserve the original failure status. Fully quit the relevant client and background processes before reopening; remote services reload according to their runtime, while sandboxes still require platform injection. A separate terminal export, shell startup file alone, or closing a window does not prove inheritance. Keep real keys out of chat, logs, screenshots, command history and Skill files.
- In the same environment that executes the CLI, run `node -e "console.log(JSON.stringify({apiKeyReadable:Boolean(['SOCIALDATAX_API_KEY','SOCIAL_MEDIA_MCP_API_KEY'].map(name=>process.env[name]?.trim()).find(Boolean))}))"` and report only the boolean, never the Key or full environment. Follow CLI lookup order: trimmed primary variable, then legacy compatibility for existing configurations; all new setup still uses `SOCIALDATAX_API_KEY`. If apiKeyReadable is false, stop business requests and diagnose in the order above. True only proves a readable nonempty value; resume the original request to verify authentication, without claiming validity or available credits. Never inject a temporary value into the probe to force success.

## Preferred Direct CLI

Prefer the direct CLI when the agent can run shell commands. It does not require MCP server configuration:

```bash
npx -y socialdatax-skills@latest douyin transcript \
  --url "<douyin_content_url_or_share_text>" --pretty \
  --source-client socialdatax-skills --source-platform clawhub \
  --source-skill douyin-video-copy-extract

npx -y socialdatax-skills@latest douyin transcript \
  --aweme-id "<aweme_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill douyin-video-copy-extract

npx -y socialdatax-skills@latest douyin transcript \
  --job-id "<job_id>" --pretty --source-client socialdatax-skills \
  --source-platform clawhub --source-skill douyin-video-copy-extract
```

Required arguments:

- `--url <douyin_content_url_or_share_text>`: use for a Douyin video URL, short link, or share text.
- `--aweme-id <aweme_id>`: use when the Douyin video ID is already known.
- `--job-id <job_id>`: use to continue checking an existing transcript job. Use exactly one of `--url`, `--aweme-id`, or `--job-id`.

Optional arguments:

- `--pretty`: output formatting only.
- `--source-client socialdatax-skills --source-platform clawhub --source-skill douyin-video-copy-extract`: usage attribution for this Agent Skill; keep these values unchanged when running examples from this Skill.

Use the direct CLI first when the agent can run shell commands. These video speech-to-text transcript / 口播转文字 workflows submit a bounded analysis job or check an existing job.
Direct CLI transcript commands try to deliver the final result in one run: submit waits server-side up to 240 seconds, then the CLI keeps querying the same `job_id`; each get-job call also waits up to 240 seconds for that job. Do not start a second submit job just to poll status.
If the direct CLI returns a non-terminal job because the command was interrupted or reached `--max-wait-seconds`, keep the returned `job_id` and continue with the matching `transcript --job-id <job_id>` command.
平台边界：使用本 Skill 命令示例列出的平台和入口；其他平台的视频转写任务使用对应的能力 Skill。

## Safety Boundary

This skill can submit bounded video speech-to-text analysis jobs through the direct CLI or hosted MCP tools. It uses `SOCIALDATAX_API_KEY` from the user's environment at runtime. Generated Skill files do not contain API keys. It does not read local browser data or perform login, posting, liking, commenting, or account changes. Prefer the direct CLI; hosted MCP tools are optional when the current agent already supports authenticated streamable HTTP MCP.

## MCP Tools

MCP tools matching the direct CLI commands above:

- `douyin_submit_video_speech_text_by_video_url`
- `douyin_submit_video_speech_text_by_aweme_id`
- `douyin_get_video_speech_text_job`

If MCP tools are already available in the current agent, use one of these tools:
- `douyin_submit_video_speech_text_by_video_url`: submit a transcript job from a Douyin video URL, short link, or share text.
- `douyin_submit_video_speech_text_by_aweme_id`: submit a transcript job from a known aweme_id.
- `douyin_get_video_speech_text_job`: check an existing transcript job by job_id.

Transcript jobs can be asynchronous. After submitting by URL or aweme_id, keep the returned `job_id` and query the same job until the response reaches a terminal completed or failed state. Do not resubmit the same video while a job is still pending.

## Output Guidance

固定输出结构：视频基础信息、原视频简介 `description`、口播逐字稿、可复制文案版、精简版、任务状态。
如果任务未完成，返回 `job_id`、当前状态和下一步续查命令；不要把未完成任务说成没有文案。
只输出返回中可见的视频上下文和 transcript 内容；不承诺视频下载、封面制作、自动改写、账号诊断、发布操作或保证爆款。

## Troubleshooting

- Credential source: identify whether this request uses CLI or MCP. For CLI, check the effective configuration in the actual execution environment using the API Key section (primary variable first, then legacy compatibility). For MCP, check the authentication configuration of the current connection, without requiring a local CLI variable. If configuration is missing, follow the earlier client diagnosis and fallback order. Do not expose Keys, Authorization headers or secret configuration values.

- If an SDK/dependency, npm network, Node.js/npm/npx availability, permission, or missing runtime error appears, treat it as a local runtime, dependency installation, network, or agent authorization issue, not a SocialDataX API key or business data error. Install or repair task dependencies only within the user's existing authorization, preferably in the project or a temporary environment. Execution permissions are not user authorization; explain and obtain approval before changes outside that scope, including global installs, runtime upgrades, or system configuration changes. When network or execution authorization is needed, ask the user to approve or finish authorization, then continue the same command; do not use public web search as a substitute for SocialDataX data.
- If the response returns `insufficient_balance` or says the balance/credits are insufficient, do not submit another job or keep polling. Show the official billing link in the error (https://socialdatax.com/dashboard/billing, including any channel parameters); if absent, use https://socialdatax.com/dashboard/billing. After recharging, resume the failed call; if a job or partial results already exist, follow the corresponding job-query or pagination recovery rules.
- If the user has recharged but still sees insufficient balance, have the user confirm in the relevant account dashboard that this request uses the recharged account, following the credential source above. If an update is needed, have the user update the effective CLI configuration or MCP connection, reload as documented, and resume the original command. Do not require reconfiguration just because the primary local variable is absent, or expose credential values.
- If a transcript `job_id` already exists, only check that same job; do not submit the video again.
