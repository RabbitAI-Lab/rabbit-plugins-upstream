## Description:

Nusii Proposals (nusii.com) is used for Nusii Proposals requests, including reading, creating, and updating data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate a connected Nusii Proposals account through OOMOL, including reading account, client, proposal, template, theme, and user data. With user confirmation for state-changing actions, it can create clients and proposals, update or archive proposals, and send proposals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends one-line remote installers that immediately execute local code.

Mitigation: Review installation steps before running them, and avoid the documented remote installers unless the OOMOL installer source has been independently trusted and verified.

Risk: Write actions can change Nusii Proposals state by creating clients or proposals, updating proposals, archiving proposals, or sending proposals.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged as write.

## Reference(s):

- [Nusii Proposals homepage](https://nusii.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nusii-proposals)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; connector responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
