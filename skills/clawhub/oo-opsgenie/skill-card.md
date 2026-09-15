## Description:

Opsgenie skill for reading, creating, and updating alerts through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect live Opsgenie connector schemas and run alert workflows such as list, fetch, create, acknowledge, close, and request-status checks through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes remote shell installer commands for the oo CLI.

Mitigation: Use a safer, verified oo CLI installation method before installing or updating the CLI.

Risk: Opsgenie alert actions can change operational alert state, including acknowledge, close, and create workflows.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running state-changing actions.

Risk: A connected Opsgenie API key may grant broader access than the skill needs.

Mitigation: Limit the Opsgenie API key to the scopes and teams this skill is intended to manage.

## Reference(s):

- [ClawHub Opsgenie Skill](https://clawhub.ai/oomol/skills/oo-opsgenie)
- [Opsgenie Homepage](https://www.atlassian.com/software/opsgenie)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; state-changing actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
