## Description:

Ashby (ashbyhq.com). Use this skill for Ashby requests that search and read recruiting data through an OOMOL-connected Ashby account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect Ashby connector schemas and run read-oriented Ashby actions for candidates, jobs, API key information, and candidate search without handling raw Ashby API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer scripts that are piped directly into a shell.

Mitigation: Review the oo CLI installation path first and prefer a signed or checksum-verified, version-pinned installer.

Risk: The skill accesses Ashby recruiting data through an OOMOL-connected account.

Mitigation: Connect only an Ashby account and scopes whose recruiting data are appropriate to access through OOMOL.

## Reference(s):

- [Ashby homepage](https://www.ashbyhq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ashby)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; read actions return JSON data and execution metadata through the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
