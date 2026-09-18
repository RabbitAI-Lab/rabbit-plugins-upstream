## Description:

Uses the OOMOL-connected oo CLI to search and read Recruiterflow candidates, jobs, and users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and recruiting operations teams use this skill to retrieve and list Recruiterflow candidates, jobs, and users through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute downloaded shell or PowerShell content.

Mitigation: Install the oo CLI through a verified method, or verify the installer source and integrity before running it.

Risk: The skill accesses Recruiterflow data through an OOMOL-connected account.

Mitigation: Use an account with appropriate Recruiterflow permissions and review returned recruiting data before sharing it outside the intended workflow.

## Reference(s):

- [Recruiterflow Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-recruiterflow)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Recruiterflow Homepage](https://recruiterflow.com)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; command responses are expected as JSON from the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
