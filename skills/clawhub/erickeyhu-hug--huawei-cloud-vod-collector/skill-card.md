## Description:

Captures poor Huawei Cloud developer experiences and distills them into structured Voice of Developer feedback records and GitCode issue reports for product and engineering teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, and engineering teams use this skill to capture Huawei Cloud tool or service failures, user rejections, and report requests, then convert them into structured local feedback and configured GitCode issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can collect rich local environment and dialog context into .vod feedback records.

Mitigation: Review and narrow the configuration before use, inspect generated feedback before delivery, remove thinking fields, and rely on the included sanitizer for sensitive values.

Risk: Auto-login can install AtomGit-GO helper binaries and create persistent local AtomGit/GitCode credentials.

Mitigation: Run installer or auto-login steps only after trusting the AtomGit-GO source and token storage model, use a controlled AtomGit home, and delete stored credentials when no longer needed.

Risk: Delivery can publish issue content to the configured GitCode repository.

Mitigation: Confirm the configured repository destination and review issue content before delivery, especially when feedback includes environment or dialog context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-vod-collector)
- [Hook setup guide](references/hooks-setup.md)
- [OpenClaw integration guide](references/openclaw-integration.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [VoD feedback record template](assets/VOD_FEEDBACKS.md)
- [GitCode issue template](assets/VOD_ISSUE.md)
- [AtomGit-GO source](https://gitcode.com/weixin_45218422/AtomGit-GO)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown feedback records and issue content, with inline shell commands and JSON status responses from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local .vod/feedbacks records, can install AtomGit-GO helper tooling, and can submit reports to the configured GitCode repository.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
