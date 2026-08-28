## Description:

Wachete (wachete.com). Use this skill for ANY Wachete request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Wachete monitors through an OOMOL-connected account, including reading monitor data and creating, updating, or deleting SinglePage monitors after reviewing the live action schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wachete actions route through OOMOL and the oo CLI, and write or destructive actions can create, replace, or delete monitors.

Mitigation: Use read actions directly when appropriate, but confirm the exact target, payload, and expected effect with the user before write or destructive actions.

## Reference(s):

- [Wachete homepage](https://www.wachete.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Wachete skill](https://clawhub.ai/oomol/skills/oo-wachete)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing Wachete actions require schema inspection and user confirmation before execution.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
