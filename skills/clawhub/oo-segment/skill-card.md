## Description:

Operates Segment through an OOMOL-connected account by inspecting live connector schemas and running Segment Alias, Batch, Group, Identify, Page, Screen, and Track actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to send Segment analytics, identity, group, page, and screen events through OOMOL's Segment connector after checking each live action schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write Segment analytics, identity, and group data.

Mitigation: Require explicit user confirmation of the exact action, payload, and expected effect before running any Segment action.

Risk: The security summary says the skill describes itself as read/search oriented while supporting write actions.

Mitigation: Treat Alias, Batch, Group, Identify, Page, Screen, and Track as data-changing operations unless live schema and user intent prove otherwise.

Risk: The setup guidance includes remote script execution for installing the oo CLI.

Mitigation: Prefer a verified package-manager or manual installation path, and review installer contents before executing remote scripts.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/oomol/skills/oo-segment)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Segment homepage](https://segment.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Segment connector commands whose responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
