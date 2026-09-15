## Description:

Provides JazzHR read access through the OOMOL oo CLI for searching and retrieving applicants, jobs, and users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect JazzHR action schemas and run read-only get/list actions for applicants, jobs, and users through an OOMOL-connected JazzHR account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include internet-downloaded install scripts for the oo CLI.

Mitigation: Review the install path first, prefer signed or checksum-verified installation, and avoid running curl|bash or irm|iex commands in an elevated shell.

Risk: JazzHR applicant and user records may contain sensitive recruiting or personnel data.

Mitigation: Use the skill only for intended read operations, limit queries to the requested records, and avoid exposing retrieved data beyond the authorized workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-jazzhr)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [JazzHR homepage](https://www.jazzhr.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only JazzHR action guidance and JSON-oriented command patterns; responses from the connector are JSON with data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
