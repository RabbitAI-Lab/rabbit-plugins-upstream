## Description:

Manatal connector skill for reading, creating, and updating candidates, jobs, matches, and organizations through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiting teams and agents use this skill to inspect Manatal action schemas and run read or write operations for candidates, jobs, matches, and organizations through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can run unverified internet installer commands for the oo CLI.

Mitigation: Review the installer path first and prefer a pinned or verified oo CLI release before executing installer pipelines.

Risk: Write actions can create or update Manatal recruitment records.

Mitigation: Inspect the live action schema and confirm the exact payload and intended effect before running write actions.

## Reference(s):

- [ClawHub Manatal skill page](https://clawhub.ai/oomol/skills/oo-manatal)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Manatal homepage](https://www.manatal.com/)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions should inspect the live connector schema before building payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
