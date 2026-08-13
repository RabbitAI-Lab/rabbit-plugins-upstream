## Description:

Openclaw learns a local user portrait of language, expertise, knowledge gaps, and communication preferences so an agent can phrase replies at the right level and manage that portrait on request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zbc0315](https://clawhub.ai/user/zbc0315)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent remember durable communication preferences across sessions and tailor replies without storing task content or secrets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates a persistent local profile that can influence replies across projects and sessions.

Mitigation: Install it only when this persistent personalization is desired, and use show, pause, correction, or reset controls when the profile becomes unwanted or inaccurate.

Risk: Sensitive or inappropriate information could be written into the portrait if users treat it as a task log.

Mitigation: Keep the portrait limited to durable communication preferences and person-level facts; do not store secrets, credentials, regulated personal data, confidential project details, task content, or one-off context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zbc0315/skills/user-portrait)
- [ClawHub publisher profile](https://clawhub.ai/user/zbc0315)
- [Related user-portrait Claude Code plugin](https://github.com/zbc0315/user-portrait)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Natural-language responses and Markdown profile updates with occasional shell commands for portrait controls.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads and writes the local portrait directory ~/.claude/user-portrait/ when active.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
