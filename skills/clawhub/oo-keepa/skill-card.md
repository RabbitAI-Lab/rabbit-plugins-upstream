## Description:

Use Keepa through an OOMOL-connected account to search and read Keepa data with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with an OOMOL-connected Keepa account use this skill to inspect live Keepa action schemas and run product, category, seller, token, best-seller, deal, and product-history queries through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote oo CLI installer commands are presented without version pinning or integrity checks.

Mitigation: Install the oo CLI only from a verified release path, inspect installer contents before execution, and avoid elevated shells.

Risk: Keepa requests are brokered through an OOMOL-connected account.

Mitigation: Install and use the skill only when you trust OOMOL and are comfortable with OOMOL handling requests through the connected Keepa account.

Risk: Live connector schemas may change over time.

Mitigation: Inspect the action schema immediately before constructing each payload and confirm exact payloads before any write or destructive action.

## Reference(s):

- [Keepa homepage](https://keepa.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Keepa skill page](https://clawhub.ai/oomol/skills/oo-keepa)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo CLI schema inspection before payload construction; command responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.1 (source: server release metadata, skill metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
