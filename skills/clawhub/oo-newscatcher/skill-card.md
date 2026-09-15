## Description:

NewsCatcher helps agents search global news, retrieve recent headlines, list indexed sources, and check subscription allowance through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate NewsCatcher through an OOMOL-connected account for news search, latest-headline retrieval, source discovery, and subscription status checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The declared oo command permission is broader than the documented read-only NewsCatcher actions.

Mitigation: Use the skill only in an environment where the authenticated OOMOL account and CLI scope are acceptable, and review intended oo commands before execution.

Risk: Remote installer commands can execute downloaded scripts.

Mitigation: Install the oo CLI through a verified official method and avoid letting an agent automatically run installer commands.

## Reference(s):

- [NewsCatcher Skill Page](https://clawhub.ai/oomol/skills/oo-newscatcher)
- [NewsCatcher Homepage](https://www.newscatcherapi.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
