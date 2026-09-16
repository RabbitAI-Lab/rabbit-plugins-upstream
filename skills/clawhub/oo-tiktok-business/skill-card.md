## Description:

TikTok Business (business.tiktok.com). Use this skill for ANY TikTok Business request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate TikTok Business through OOMOL-connected accounts, inspect connector schemas, and run read-oriented advertiser, campaign, store, GMV Max reporting, and setup eligibility workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute code from OOMOL endpoints without local verification.

Mitigation: Review the setup path before installing and prefer a verified, version-pinned oo CLI installation method when available.

Risk: Connector commands act against a connected TikTok Business account and depend on live action schemas and account permissions.

Mitigation: Inspect the live connector schema before constructing payloads and obtain explicit user confirmation before running any action tagged as write or destructive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-tiktok-business)
- [TikTok Business Homepage](https://business.tiktok.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector responses as JSON when commands are run with --json.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
