## Description:

Cochrane lets an agent search and read Cochrane review data through OOMOL's oo CLI and cochrane connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve Cochrane review metadata, document roles, translations, and version history through an OOMOL-connected Cochrane account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires OOMOL's oo CLI and an OOMOL-connected Cochrane account.

Mitigation: Install only when comfortable using OOMOL's oo CLI and connecting a Cochrane account through OOMOL.

Risk: The trigger wording is broader than the listed read-oriented actions.

Mitigation: Use it for Cochrane review data tasks and inspect the live connector schema before constructing each payload.

Risk: Future connector actions could add write or destructive capabilities.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions, and require explicit approval for destructive actions.

## Reference(s):

- [Cochrane homepage](https://www.cochrane.org)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cochrane)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON connector payloads or responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before running actions; listed actions are read-oriented.]

## Skill Version(s):

1.0.0 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
