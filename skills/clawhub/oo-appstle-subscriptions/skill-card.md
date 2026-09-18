## Description:

Enables agents to read Appstle Subscriptions customer and subscription contract data through OOMOL's appstle_subscriptions connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Appstle customer subscription records, subscription contract details, and valid subscription contract IDs from an OOMOL-connected Appstle account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path recommends live remote installer commands, including pipe-to-shell execution.

Mitigation: Prefer a verified package or separately download, inspect, and verify the installer before execution.

Risk: Future connector actions could change or delete Appstle data if write or destructive actions are added.

Mitigation: Require explicit user confirmation of the exact payload and effect before running any write or destructive connector action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-appstle-subscriptions)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Appstle Subscriptions homepage](https://appstle.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live connector schemas before running read actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
