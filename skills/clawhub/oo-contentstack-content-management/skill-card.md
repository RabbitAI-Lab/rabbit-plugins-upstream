## Description:

Contentstack Content Management (contentstack.com) helps agents read, create, and update Contentstack data through the OOMOL `oo` CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operations teams use this skill to let an agent inspect Contentstack schemas, list or retrieve content, and prepare confirmed create or update actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that pipe downloaded scripts directly to a shell.

Mitigation: Review official installation steps, prefer a pinned or verified installer, and do not allow an agent to run the installer automatically.

Risk: Create and update actions can change Contentstack state.

Mitigation: Inspect the live action schema and confirm the exact payload and intended effect with the user before running any write action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-contentstack-content-management)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Contentstack Homepage](https://www.contentstack.com/)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action-schema inspection before constructing connector payloads; write actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
