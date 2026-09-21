## Description:

Google Ads (ads.google.com). Use this skill for ANY Google Ads request: reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to operate Google Ads through an OOMOL-connected account for campaign lookup, GAQL queries, customer list management, and campaign or ad group mutations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, or remove Google Ads resources when write or destructive actions are used.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running write or destructive actions.

Risk: First-time setup guidance includes remote installer commands for the oo CLI.

Mitigation: Install only if OOMOL and the oo CLI are trusted, and review the official install guide or installer script before execution.

Risk: Connected Google Ads credentials may expose broader account access than a task requires.

Mitigation: Use the least-privileged Google Ads account practical for the task.

## Reference(s):

- [Google Ads homepage](https://ads.google.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Google Ads skill listing](https://clawhub.ai/oomol/skills/oo-googleads)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Google Ads connector JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
