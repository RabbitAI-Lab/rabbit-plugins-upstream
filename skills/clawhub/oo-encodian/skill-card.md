## Description:

Encodian connector for agents to run PDF actions through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Encodian action schemas and run PDF compression, page extraction, text extraction, encryption, and unlocking actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path and safety scoping need review before installation.

Mitigation: Review the oo CLI installation source before using this skill and avoid running remote install scripts directly.

Risk: Sensitive PDFs may be sent to Encodian by actions that process document content.

Mitigation: Confirm before sending sensitive PDFs, including for actions the skill labels as untagged or read-like.

Risk: Write actions can change Encodian state or document protection behavior.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write.

## Reference(s):

- [ClawHub Encodian Skill](https://clawhub.ai/oomol/skills/oo-encodian)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Encodian homepage](https://www.encodian.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Encodian connector JSON responses, including base64 PDF content or extracted text, depending on the selected action.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
