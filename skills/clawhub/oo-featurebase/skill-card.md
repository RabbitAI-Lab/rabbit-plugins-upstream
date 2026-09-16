## Description:

Featurebase helps agents manage Featurebase boards, posts, and contacts through the OOMOL-connected oo CLI and featurebase connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Product, support, and operations teams can use this skill through an agent to read Featurebase boards, posts, and contacts, and to manage feedback records when changes are explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path may ask an agent to run remote install scripts for the oo CLI.

Mitigation: Review the installer first or install the oo CLI through a trusted official method before enabling the skill.

Risk: The skill can create, update, upsert, or delete Featurebase records.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before any write or destructive action.

Risk: Connector schemas may change over time and stale payloads could fail or affect the wrong fields.

Mitigation: Fetch the live connector schema before constructing each action payload.

## Reference(s):

- [Featurebase homepage](https://www.featurebase.app/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-featurebase)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions may return JSON data from Featurebase through the oo CLI.]

## Skill Version(s):

1.0.2 (source: evidence release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
