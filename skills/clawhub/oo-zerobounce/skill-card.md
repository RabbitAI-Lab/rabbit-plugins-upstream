## Description:

ZeroBounce (zerobounce.net). Use this skill for ANY ZeroBounce request - reading, creating, and updating data. Whenever a task involves ZeroBounce, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate ZeroBounce through an OOMOL-connected account for single-email validation, usage and credit lookups, activity checks, and custom filter rule management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path presents remote installer commands that execute shell or PowerShell scripts directly.

Mitigation: Review the oo CLI installation method before use and prefer a signed or checksum-verified installer from the vendor.

Risk: Email validation and account lookups may send sensitive or bulk email data through the connector.

Mitigation: Use the connector only when OOMOL's data handling terms meet the user's privacy and compliance requirements.

Risk: The create_filter_rule action can change ZeroBounce account state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ZeroBounce homepage](https://www.zerobounce.net)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub ZeroBounce skill](https://clawhub.ai/oomol/skills/oo-zerobounce)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce oo CLI connector commands and summarize JSON responses returned by ZeroBounce actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
