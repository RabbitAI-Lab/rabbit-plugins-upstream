## Description:

Atlas.so (atlas.so). Use this skill for ANY Atlas.so request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Atlas.so through an OOMOL-connected account, including reading customer, account, and session data and performing confirmed customer or account updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path directs users to run a remote installer, which could execute arbitrary code if the source is not verified.

Mitigation: Review the installer path before installing and prefer a verified, versioned oo CLI release with checksums or signatures.

Risk: The skill can read customer, account, and session data and can make customer or account updates through the connected OOMOL account.

Mitigation: Connect Atlas.so only when that access is intended, and confirm the exact payload and effect before running write or upsert actions.

## Reference(s):

- [ClawHub Atlas.so skill page](https://clawhub.ai/oomol/skills/oo-atlas-so)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Atlas.so homepage](https://atlas.so)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects that include data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
