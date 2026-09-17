## Description:

TrawlingWeb (trawlingweb.com). Use this skill for ANY TrawlingWeb request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search indexed news and blog publications through TrawlingWeb via an OOMOL-connected account. It supports schema inspection, connector execution, and setup recovery guidance for normal TrawlingWeb search workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer scripts that execute directly in the shell.

Mitigation: Review the installer source and prefer a verified, pinned installation method before using the skill.

Risk: Requests go through OOMOL using the connected account.

Mitigation: Use the skill only for intended TrawlingWeb searches and confirm the account connection, scopes, and credit status when errors occur.

## Reference(s):

- [TrawlingWeb homepage](https://trawlingweb.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-trawlingweb)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
