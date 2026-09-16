## Description:

This skill helps agents search and read Smartlead campaign, lead, and email account data through the OOMOL smartlead_ai connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Smartlead schemas and retrieve campaign, lead, campaign list, and email account data through an OOMOL-connected Smartlead account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts without checksum or signature verification.

Mitigation: Review before installing; prefer a signed, versioned, or checksum-verified oo CLI release and avoid running setup from an elevated shell.

## Reference(s):

- [Smartlead homepage](https://www.smartlead.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-smartlead-ai)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or connector results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are expected to include data and meta.executionId when actions succeed.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
