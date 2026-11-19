## Description:

Manage connected social accounts through AdaptlyPost by scheduling and publishing posts, reviewing analytics, and handling inbox activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

Social media managers and teams use this skill to manage posts, analytics, connected accounts, and inbox activity for their AdaptlyPost workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags media uploads as publicly accessible and notes that the skill documentation lacks a privacy warning; the scan also reports an undeclared LinkedIn organization lookup and says its evidence is incomplete.

Mitigation: Review upload visibility before installation and avoid uploading sensitive or unpublished media until its exposure is understood. Review the LinkedIn organization lookup behavior; treat the suspicious rating as a review signal rather than a finding of malicious intent.

## Reference(s):

- [AdaptlyPost](https://adaptlypost.com)
- [AdaptlyPost API reference](artifact/references/api-reference.md)
- [Platform configurations](artifact/references/platform-configs.md)
- [AdaptlyPost OpenClaw plugin](https://github.com/adaptlypost/adaptlypost-openclaw/tree/main/openclaw-plugin)
- [ClawHub release page](https://clawhub.ai/tarasshyn/skills/adaptlypost)

## Skill Output:

**Output Type(s):** [API Calls, Text, Configuration, Guidance]

**Output Format:** [API requests and natural-language summaries or guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or change social content and connected-account data; high-impact actions require explicit user confirmation.]

## Skill Version(s):

1.35.1 (source: frontmatter; server release 1.35.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
