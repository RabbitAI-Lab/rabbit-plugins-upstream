## Description:

NewsData.io helps agents retrieve latest, cryptocurrency, source-domain, and archive news data through the OOMOL NewsData.io connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to query NewsData.io for current news, cryptocurrency news, source domains, and historical archive results through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands for the oo CLI.

Mitigation: Install the oo CLI only through a trusted, versioned, verifiable method instead of running remote installer scripts automatically.

Risk: The security summary says the stated scope does not match the documented actions.

Mitigation: Treat the skill as read-oriented unless the live connector schema proves a requested write action exists, and confirm the exact payload before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-newsdata-io)
- [NewsData.io homepage](https://newsdata.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL NewsData.io connection](https://console.oomol.com/app-connections?provider=newsdata_io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are JSON with data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
