## Description:

MiniMax H3 视频生成 helps creators, marketing teams, e-commerce teams, and short-form production teams generate videos from text or reference media through AI Hive, including media upload, task submission, progress checks, and result download.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, e-commerce operators, and production teams use this skill to generate advertising, product, social, short-drama, and comic-drama videos from prompts and optional image, video, or audio references. Developers and agents can also use it to submit AI Hive video-generation jobs, check task status, upload media, and manage downloaded outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI Hive API key and can send the bearer token to the configured API base URL.

Mitigation: Use only the default or a fully trusted base URL, keep the API key limited to this workflow, and rotate or revoke it if exposed.

Risk: The skill uploads selected image, video, or audio files to AI Hive.

Mitigation: Review media before upload and avoid sending sensitive, confidential, or rights-restricted assets.

Risk: The skill can write downloaded generation results to the local output directory.

Mitigation: Use --no-download or a dedicated output directory for untrusted tasks, and review generated files before sharing or publishing.

Risk: The server security verdict is suspicious because of credential and file-write risks.

Mitigation: Review and scan the skill before deployment, and run it in an isolated environment if those risks are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/minimax-h3)
- [AI Hive API key console](https://ai-hive.iclip.cn/chat)
- [AI Hive OpenAPI base endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and JSON task/status output; generated media is saved as video files when downloads are enabled.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload user-selected media to AI Hive, query real-time model and pricing data, save task IDs, and download generated MP4/MOV results to the selected output directory.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
