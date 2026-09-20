## Description:

HaiGuanJia access for reading, creating, updating, and deleting account data through the OOMOL hgj connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate HaiGuanJia workflows through OOMOL-connected oo CLI actions, including logistics tracking, customs, manifest, vessel schedule, and port container tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions may cause an agent to run a remote oo CLI installer directly in a shell.

Mitigation: Review the setup path first, install the CLI from an official and verified source, and avoid running remote installer commands blindly.

Risk: Write, destructive, and billed HaiGuanJia actions can change account data or incur charges.

Mitigation: Confirm the exact action, payload, target records, and expected effect with the user before executing state-changing or chargeable commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-hgj)
- [HaiGuanJia OpenAPI](https://openapi.hgj.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with oo CLI commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
