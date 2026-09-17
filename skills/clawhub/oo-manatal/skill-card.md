## Description:

Manatal (manatal.com). Use this skill for ANY Manatal request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read, create, and update Manatal recruiting records through an OOMOL-connected account. It supports candidate, job, match, and organization workflows while directing the agent to inspect live connector schemas before submitting payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Review the installer path before installing and prefer a trusted, versioned, verifiable installation method.

Risk: The skill can create or update Manatal recruiting data.

Mitigation: Only allow create or update actions after checking the exact Manatal records and payloads involved.

## Reference(s):

- [ClawHub Manatal skill](https://clawhub.ai/oomol/skills/oo-manatal)
- [Manatal homepage](https://www.manatal.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill expects command output from the oo CLI as JSON responses containing data and metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
