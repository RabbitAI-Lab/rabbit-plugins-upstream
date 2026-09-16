## Description:

Short.io (short.io). Use this skill for reading, creating, updating, deleting, and reporting on Short.io links and domains through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Short.io links and domains from an agent workflow, including link creation, updates, deletion, retrieval, listing, and click statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup can execute code returned by the installer host.

Mitigation: Install the oo CLI from a verified source, inspect the installer first, and prefer pinned or integrity-checked releases.

Risk: Write and destructive actions can change or remove Short.io links.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or delete actions.

Risk: Connector payloads can drift from the current Short.io action contract.

Mitigation: Fetch the live action schema before constructing each connector payload.

## Reference(s):

- [Short.io skill release](https://clawhub.ai/oomol/skills/oo-short-io)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Short.io homepage](https://short.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema lookup before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
