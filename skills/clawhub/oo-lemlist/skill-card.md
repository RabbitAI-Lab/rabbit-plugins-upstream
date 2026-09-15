## Description:

Helps an agent read lemlist campaign, lead, and team data through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and operations users can ask an agent to inspect lemlist campaigns, campaign leads, and team information from a connected OOMOL account. The skill is intended for read-oriented lemlist workflows that need live connector schemas before each action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Install the oo CLI through a trusted, pinned, and verifiable channel before using the skill.

Risk: Future lemlist connector actions may write to or destructively change account data.

Mitigation: Require explicit user confirmation of the exact action, target, and JSON payload before allowing any write or destructive action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lemlist)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [lemlist homepage](https://www.lemlist.com)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
