## Description:

Cochrane helps agents search and read Cochrane review data through the OOMOL `oo` CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Cochrane connector schemas and retrieve review metadata, document roles, translations, and version history through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connector payloads may be processed through OOMOL as an intermediary for Cochrane requests.

Mitigation: Avoid sending sensitive unpublished or personal research data unless OOMOL processing is acceptable for the user's use case.

Risk: Setup instructions include remote installer commands.

Mitigation: Prefer an official, versioned, verifiable oo CLI installation method before using the connector.

Risk: The routing instructions are broader than the listed Cochrane actions.

Mitigation: Use the skill only for Cochrane review metadata, roles, translations, and version history, and inspect the live action schema before running an action.

## Reference(s):

- [Cochrane homepage](https://www.cochrane.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cochrane)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, Shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing Cochrane action payloads.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
