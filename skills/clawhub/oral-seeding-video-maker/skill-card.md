## Description:

Spoken Seeding Video Maker turns a product, service, or topic into a short narrated vertical recommendation video plan with a shot list, generated beat frames, narration, optional music, and a final clip animated from the opening frame.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent users use this skill to plan and generate short recommendation-style social videos from a single subject when they have no recorded footage, product photo, or voice recording. It is aimed at product seeding posts, creator recommendations, review-style shorts, service explainers, and account-building content for short-form platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Beatra device credential that is shared across Beatra skills and can authorize paid account actions.

Mitigation: Install only if that account authority is acceptable, keep the credential private, and revoke the device in the Beatra Console when access is no longer trusted.

Risk: The bundled client silently self-updates installed package code by default.

Mitigation: Use the documented auto-update controls to disable silent updates before normal use if the deployment requires fixed reviewed code.

Risk: The release security verdict is suspicious because broad account authority and silent updates increase review burden.

Mitigation: Review the package, its security guidance, and generated paid-call approvals before installation or production use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/oral-seeding-video-maker)
- [Publisher Profile](https://clawhub.ai/user/beatra-ai)
- [Beatra Skill Homepage](https://beatra.ai/skills/oral-seeding-video-maker)
- [Choosing the pattern](references/script-patterns.md)
- [Writing the spoken lines](references/spoken-lines.md)
- [Seeding video workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, JSON request examples, task metadata, artifact links, and generated media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include an approved shot list, generated still frames, narration audio, optional music audio, one vertical video clip, task IDs, model choices, returned dimensions and duration, and billing facts when available.]

## Skill Version(s):

0.1.8 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
