## Description:

Helps operators set up JFTech smart stores, manage cameras and AI inspection plans, review patrol records, and generate visual reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jftech](https://clawhub.ai/user/jftech)

### License/Terms of Use:

MIT-0

## Use Case:

Store operators and developers use this skill to onboard cameras, manage authorized AI patrol plans, inspect records, and share HTML reports across JFTech smart stores.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Store, device, and patrol-plan deletion can take effect without a confirmation or dry run.

Mitigation: Review targets before deletion, restrict account permissions, and treat delete commands as irreversible.

Risk: API credentials may grant access to live smart-store resources at the configured endpoint.

Mitigation: Use dedicated, limited-scope credentials where available and verify JF_ENDPOINT points to the intended JF API host.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/jftech/skills/jf-smart-store-inspection)
- [Smart store API reference](references/api-reference.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, HTML reports]

**Output Format:** [Text and shell commands; JSON configuration and records; interactive HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include inspection statistics and linked camera snapshots.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
