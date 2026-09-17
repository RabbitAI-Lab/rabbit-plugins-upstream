## Description:

Ashby lets an agent search and read Ashby recruiting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiting teams and agents supporting recruiting workflows use this skill to inspect Ashby connector schemas, list candidates and jobs, search candidates, and check API key information without handling raw Ashby API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that download and execute scripts.

Mitigation: Review the installer first or use a verified package, pinned release, or manually inspected installer before installation.

Risk: The connected OOMOL account can read Ashby candidate and job information.

Mitigation: Install and run the skill only for authorized users and accounts with appropriate Ashby access.

Risk: Connector responses may contain sensitive recruiting data.

Mitigation: Limit sharing of command output and handle candidate and job data according to the organization's data handling requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ashby)
- [Ashby homepage](https://www.ashbyhq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action results are returned as JSON when commands are run with the documented JSON flag.]

## Skill Version(s):

1.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
