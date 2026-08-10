## Description:

Resolves Bilibili video links through yige.zone and returns direct watermark-free video and cover download links for single or batch requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessdy](https://clawhub.ai/user/jessdy)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as content creators, video collectors, and operations analysts use this skill to parse Bilibili links, obtain temporary direct download URLs and cover links, and save authorized content for editing, backup, or offline review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bilibili URLs and the YIGE_API_KEY are sent to yige.zone for parsing.

Mitigation: Use the skill only when that data sharing is acceptable, and keep the API key in an environment variable or another secure secret store.

Risk: API keys may be exposed if pasted into prompts, logs, command history, or shared files.

Mitigation: Avoid hard-coding or pasting keys in plain text; rotate or revoke the key if exposure is suspected.

Risk: Downloading videos without appropriate rights can create policy or legal issues.

Mitigation: Use the skill only for videos you own, are authorized to download, or may lawfully preserve for the intended purpose.

## Reference(s):

- [Server-resolved source repository](https://github.com/jessdy/yige-skills/tree/main/skills/bilibili-video-downloader)
- [ClawHub skill listing](https://clawhub.ai/jessdy/skills/bilibili-video-downloader-3)
- [Core workflow](references/core_workflow.md)
- [YigeHub API key settings](https://yige.zone/settings/api-keys?source=github)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown tables with video and cover links, plus optional JSON output from the downloader script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a YIGE_API_KEY and Bilibili URL input; returned video links are described as valid for about 5 minutes.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
