## Description:

Best Buy enables agents to search and read Best Buy product, category, review, and store information through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to look up Best Buy catalog, product review, and store data from an OOMOL-connected Best Buy account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer scripts that are piped directly into a shell.

Mitigation: Install the oo CLI only from a trusted OOMOL source or a verified vendor installation method, and review installer behavior before execution.

Risk: Connector behavior depends on live action schemas and account connection state.

Mitigation: Fetch the action schema before constructing payloads, and run authentication or connection setup only after a matching command failure.

Risk: Future or changed connector actions may include write or destructive behavior.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged write or destructive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-bestbuy)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Best Buy Homepage](https://www.bestbuy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses include Best Buy connector data and meta.executionId when actions are run with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
