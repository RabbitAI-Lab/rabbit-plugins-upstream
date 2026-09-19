## Description:

Stannp (stannp.com). Use this skill for ANY Stannp request: reading, creating, updating, and deleting data through the OOMOL Stannp connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Stannp recipients and groups, validate postal addresses, and check account balance through an OOMOL-connected Stannp account. It supports read, write, and destructive connector actions with confirmation guidance for state-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup fallback includes remote installer commands that should not be run blindly.

Mitigation: Install only after verifying the installer through an approved package or source process.

Risk: Write and destructive Stannp actions can change or remove recipient and group data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running state-changing actions.

## Reference(s):

- [Stannp homepage](https://www.stannp.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-stannp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
