## Description:

BoldSign helps agents read, create, and update BoldSign data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate a connected BoldSign account: inspect live action schemas, list documents and templates, read details, check API credits, and send signature requests from templates after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands.

Mitigation: Treat oo CLI setup as a manual installation step, review the official installer source, or use a safer pinned or package-manager installation path.

Risk: Sending a document from a template changes BoldSign account state.

Mitigation: Confirm the exact send-document payload and expected effect with the user before execution.

## Reference(s):

- [ClawHub BoldSign Skill](https://clawhub.ai/oomol/skills/oo-boldsign)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [BoldSign](https://boldsign.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action runs can return JSON objects from the oo CLI; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: evidence release.version and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
