## Description:

Enables agents to search and read Klipfolio clients, dashboards, data sources, and Klips through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and business users use this skill to inspect Klipfolio clients, dashboards, data sources, and Klips through an OOMOL-connected account without calling the Klipfolio API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's setup fallback includes remote installer snippets for the oo CLI.

Mitigation: Do not let an agent run installer snippets automatically; install the oo CLI only through a trusted, verified method.

Risk: The skill can read Klipfolio assets visible to the connected API key.

Mitigation: Use only the listed read actions, inspect the live connector schema before each call, and manually confirm login, connection, credential, scope, and billing recovery steps.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-klipfolio)
- [Klipfolio Homepage](https://www.klipfolio.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
