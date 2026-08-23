## Description:

PractiTest lets agents read, create, update, and delete PractiTest project and test data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users managing PractiTest use this skill to inspect projects and tests, then perform approved create, update, and delete test operations through their connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can permanently change PractiTest test data through update and delete actions.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

Risk: Installing the skill lets agents manage PractiTest through the user's OOMOL-connected account.

Mitigation: Install only for users who intend to delegate PractiTest management and review state-changing requests carefully.

## Reference(s):

- [ClawHub PractiTest Skill Page](https://clawhub.ai/oomol/skills/oo-practitest)
- [PractiTest Homepage](https://www.practitest.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; state-changing actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
