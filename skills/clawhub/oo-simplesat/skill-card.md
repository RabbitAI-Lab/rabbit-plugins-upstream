## Description:

Lets an agent read, search, create, and update Simplesat customers, surveys, questions, and responses through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operations teams use this skill to let agents work with Simplesat account data, including customer records, survey responses, questions, surveys, and event-based survey emails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer one-liners in first-time setup can execute unverified scripts.

Mitigation: Install the oo CLI through a verified, versioned method and do not let agents run installer one-liners automatically.

Risk: Write actions can change Simplesat state by creating or updating customers or scheduling survey emails.

Mitigation: Confirm the exact payload and effect with the user before running actions tagged as write, and inspect the live schema first.

Risk: Inline connector payloads can be malformed or unsafe when values come from users or external systems.

Mitigation: Prefer @file JSON payloads for connector calls that include user-supplied or externally sourced values.

## Reference(s):

- [Simplesat homepage](https://www.simplesat.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-simplesat)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agents should inspect live action schemas before constructing payloads; state-changing actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
