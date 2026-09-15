## Description:

U301 (u301.com). Use this skill for U301 requests that read, create, update, or delete short-link data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage U301 short links from an OOMOL-connected account. It helps inspect live action schemas, create short links, list available domains, and delete short links with explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute directly in a shell.

Mitigation: Install the oo CLI from a verified, versioned source and validate checksums or signatures before running installer content.

Risk: The delete_link action is destructive and can remove a U301 short link.

Mitigation: Confirm the exact domain and slug with the user and obtain explicit approval before running the delete action.

## Reference(s):

- [U301 homepage](https://u301.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-u301)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include oo CLI JSON responses containing action data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
