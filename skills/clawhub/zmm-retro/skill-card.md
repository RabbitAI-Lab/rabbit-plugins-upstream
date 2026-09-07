## Description:

A post-publish short-video retrospective skill that collects real platform data, compares it with pre-publish assumptions, attributes outcomes through observable funnel metrics, and records validated learning into skill memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and their agents use this skill after a short video is published to collect Douyin performance data, compare it with the original topic and hook expectations, identify supported and unsupported conclusions, and update content-system memory with validated patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and rewrite broad shared skill memory, so incorrect retrospective conclusions may influence future content work.

Mitigation: Require proposed file changes to be shown before writing, limit reads and writes to the specific video and related skill folders, and keep version history for rollback.

Risk: Retrospectives may include platform analytics and private-message signals.

Mitigation: Avoid storing raw private-message content and keep only the minimum aggregated signals needed for future decisions.

## Reference(s):

- [规则卡](artifact/references/规则卡.md)
- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-retro)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown guidance with structured retrospective findings, next-step recommendations, and proposed memory or data-file updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose edits to shared content-system memory and video tracking files after reviewing post-publish performance data.]

## Skill Version(s):

0.2.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
