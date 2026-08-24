---
name: "douyin-video-copy-extract"
description: "用于抖音文案提取、抖音文案一键提取、抖音视频文案提取、抖音视频转文字、抖音口播转文字和抖音逐字稿。用户粘贴抖音视频链接、分享文案或 aweme_id 后，提取视频上下文、原视频简介和口播逐字稿，来自 SocialDataX 社媒数据助手。"
source_client: "socialdatax-skills"
source_platform: "clawhub"
source_skill: "douyin-video-copy-extract"
metadata: {"openclaw":{"requires":{"env":["SOCIALDATAX_API_KEY"],"bins":["node","npm"]},"primaryEnv":"SOCIALDATAX_API_KEY","install":[{"kind":"node","package":"socialdatax-skills","bins":[]}],"emoji":"🎙️","homepage":"https://socialdatax.com/ai?from=clawhub"}}
---
<!-- AUTO-GENERATED from socialdatax-skill-source. Do not edit directly; run `node scripts/generate_socialdatax_skills.mjs`. -->

# 抖音文案提取

Use this skill when the user wants 抖音文案提取, 抖音文案一键提取, 抖音视频文案提取, 抖音视频转文字, 抖音口播转文字, 抖音逐字稿, Douyin transcript extraction, spoken copy extraction, or to check a Douyin transcript job.

Current platform support:

- Douyin / 抖音 video work speech-to-text transcript jobs through the `douyin_*video_speech_text*` tools.

## API Key

Use `SOCIALDATAX_API_KEY` for data calls. The only official website for requesting or managing API access is <https://socialdatax.com/ai?from=clawhub>. If a user asks where to get a key, provide only this URL; do not infer alternate domains.
获取或管理 API Key：访问 <https://socialdatax.com/ai?from=clawhub>，按官网的 API Key 申请/管理入口操作。环境变量名固定使用 `SOCIALDATAX_API_KEY`；不要引导用户使用其他域名。

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

- If an SDK/dependency, npm network, Node.js/npm/npx availability, permission, or missing runtime error appears, treat it as a local runtime, dependency installation, network, or agent authorization issue, not a SocialDataX API key or business data error. If the current environment has permission, install or restore automatically. When network or execution authorization is needed, ask the user to approve or finish authorization, then continue the same command; do not use public web search as a substitute for SocialDataX data.
- If the response returns `insufficient_balance` or says the balance/credits are insufficient, do not submit another job or keep polling. Show the recharge URL from the error exactly as returned, then continue the same command after the user recharges.
- If the user has recharged but still sees insufficient balance, confirm `SOCIALDATAX_API_KEY` belongs to the same account that was recharged; if needed, copy a fresh API Key from the official dashboard.
- If a transcript `job_id` already exists, only check that same job; do not submit the video again.
