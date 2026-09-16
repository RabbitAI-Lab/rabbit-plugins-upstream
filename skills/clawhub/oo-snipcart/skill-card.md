## Description:

Snipcart (snipcart.com). Use this skill for Snipcart requests involving reading, creating, and updating data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Snipcart connector schemas and retrieve customer or order data through an OOMOL-connected account. It also provides setup guidance when the oo CLI, authentication, connection, or billing state blocks connector use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute external code.

Mitigation: Independently trust and verify the OOMOL CLI installer before use; prefer a signed or checksummed installation method.

Risk: Connector use routes Snipcart customer and order operations through an OOMOL-connected account.

Mitigation: Confirm account connection, scopes, and organizational approval before using the connector on customer or order data.

Risk: State-changing or destructive connector actions could modify Snipcart data.

Mitigation: Inspect the live action schema and confirm the exact payload and effect with the user before running any action tagged write or destructive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-snipcart)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Snipcart Homepage](https://snipcart.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
