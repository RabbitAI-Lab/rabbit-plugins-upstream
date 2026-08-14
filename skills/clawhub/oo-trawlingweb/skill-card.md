## Description:

TrawlingWeb helps agents search indexed news and blog publications through an OOMOL-connected TrawlingWeb account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to search TrawlingWeb news and blog indexes from an OOMOL-connected account. The skill guides agents to inspect the live action schema, build a matching request payload, and run the read-only search action through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the OOMOL oo CLI and an OOMOL-connected TrawlingWeb account.

Mitigation: Before installing, confirm trust in OOMOL and the oo CLI, then authenticate and connect TrawlingWeb only through the documented OOMOL setup flow.

Risk: Incorrect request payloads may fail or return unintended search results if they do not match the live connector contract.

Mitigation: Inspect the action schema with `oo connector schema` before constructing `oo connector run` payloads.

Risk: Connection, credential, or billing state can block successful use.

Mitigation: Use the documented setup fallback only after an auth, connection, credential, app, scope, or HTTP 402 billing error occurs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-trawlingweb)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [TrawlingWeb Homepage](https://trawlingweb.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with inline shell command examples and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to fetch the live connector schema before constructing request payloads.]

## Skill Version(s):

1.0.0 (source: server evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
