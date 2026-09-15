## Description:

Operates Keen IO through OOMOL's oo CLI to publish JSON events and run count or sum queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to work with a connected Keen IO account: publishing events, counting events over a timeframe, and summing numeric event properties.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may run an unverified remote installer script for the oo CLI.

Mitigation: Install the oo CLI from a verified, pinned, or package-manager source before using the skill.

Risk: The `add_event` action can write new event data to a Keen IO collection.

Mitigation: Confirm the exact collection, payload, and expected effect with the user before running write actions.

## Reference(s):

- [Keen IO homepage](https://keen.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Keen IO skill listing](https://clawhub.ai/oomol/skills/oo-keen-io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
