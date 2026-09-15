## Description:

Instatus (instatus.com). Use this skill for ANY Instatus request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Instatus status pages, components, incidents, and incident updates through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts into shell interpreters.

Mitigation: Install the oo CLI only through a verified, user-approved method and do not allow an agent to run installer pipes automatically.

Risk: Write and destructive connector actions can create, update, or delete Instatus data.

Mitigation: Confirm the exact payload, target resource, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [Instatus homepage](https://instatus.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Instatus ClawHub listing](https://clawhub.ai/oomol/skills/oo-instatus)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, OOMOL sign-in, and a connected Instatus account before actions can run.]

## Skill Version(s):

1.0.2 (source: server evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
