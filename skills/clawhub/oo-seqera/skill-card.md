## Description:

Seqera enables an agent to read Seqera data and launch workflows through OOMOL's connected oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workflow operators use this skill to inspect Seqera users, workspaces, pipelines, and workflow runs, and to launch workflows after checking the live connector schema and confirming state-changing payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the oo CLI through a remote shell script can execute publisher-provided installation code.

Mitigation: Confirm trust in OOMOL as the connector provider and prefer the official install guide or a verified installer before running installation commands.

Risk: Launching a Seqera workflow changes state and may trigger compute, data, or billing impact.

Mitigation: Review the exact workspace, payload, and expected effect with the user before approving workflow launch execution.

## Reference(s):

- [ClawHub Seqera Skill](https://clawhub.ai/oomol/skills/oo-seqera)
- [Seqera Homepage](https://seqera.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands target the OOMOL oo CLI and may return JSON connector responses.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
