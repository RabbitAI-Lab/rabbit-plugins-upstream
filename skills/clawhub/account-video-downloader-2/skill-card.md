## Description:

Account Video Downloader helps an agent fetch recent works from Douyin, Kuaishou, Bilibili, or YouTube accounts, resolve media download links, and optionally batch download files locally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessdy](https://clawhub.ai/user/jessdy)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, operators, and developers use this skill to collect account-level video work lists, review engagement metadata, resolve download resources, and save authorized media for backup, analysis, or offline viewing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables bulk watermark-free media downloading with weak privacy, permission, and lawful-use guardrails.

Mitigation: Use it only for media the user owns or is authorized to download, and confirm lawful use before resolving or saving media.

Risk: Account IDs, profile URLs, target video URLs, and the YIGE API key are sent to yige.zone.

Mitigation: Avoid sensitive or private targets, keep the API key out of prompts, code, logs, and output files, and rotate the key if exposure is suspected.

Risk: Resolved download links may appear in chat output, JSON output, local files, or logs.

Mitigation: Treat generated links as sensitive, share outputs only with authorized recipients, and clean up local outputs when they are no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jessdy/skills/account-video-downloader-2)
- [Server-Resolved GitHub Provenance](https://github.com/jessdy/yige-skills/tree/main/skills/account-video-downloader)
- [Publisher Profile](https://clawhub.ai/user/jessdy)
- [YIGE API Key Setup](https://yige.zone/settings/api-keys?source=github)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, files, guidance]

**Output Format:** [Markdown tables or JSON, with optional downloaded media files and shell command guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports platform and account selection, pagination, date filters, rate limiting, and optional batch download to a local output directory.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
