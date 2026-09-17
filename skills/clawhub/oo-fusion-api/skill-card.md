## Description:

OOMOL Fusion API lets agents use the OOMOL fusion-api connector through the oo CLI to inspect schemas and run image, audio, video, OCR, document, file-upload, and web-content actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to work with OOMOL Fusion API workflows through schema-checked oo CLI calls, including media generation and editing, speech and OCR processing, document conversion, file uploads, and web-content retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute code that was not reviewed with the skill release.

Mitigation: Install the oo CLI only through a trusted, verifiable path and do not let an agent automatically run curl|bash or irm|iex setup commands.

Risk: Some actions upload or process private content, generate media, change OOMOL data, delete data, or consume credits.

Mitigation: Review the live action schema before each call and require user confirmation for private-content, upload, generation, state-changing, destructive, or credit-consuming actions.

Risk: Safety labels may understate the effect of some actions that process or generate user content.

Mitigation: Base confirmation requirements on the action name, schema, payload, and expected effect rather than relying only on write or destructive tags.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fusion-api)
- [OOMOL Fusion API homepage](https://www.oomol.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON payloads, and JSON responses from the oo CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions should inspect the live connector schema before sending payloads and should preserve execution IDs from JSON responses.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
