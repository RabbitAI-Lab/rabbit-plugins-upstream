## Description:

Instantly.ai lets agents manage Instantly.ai campaigns and leads through the OOMOL-connected oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to list or retrieve Instantly.ai campaigns and leads, inspect live action schemas, and create leads after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes direct remote installer commands for the oo CLI.

Mitigation: Install oo through a verified, versioned, checksum- or signature-checked release path before using the skill.

Risk: The create_lead action changes Instantly.ai account data.

Mitigation: Confirm the exact lead-creation payload and expected effect with the user before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-instantly-ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Instantly.ai Homepage](https://instantly.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas and JSON responses; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
