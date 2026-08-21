## Description:

Installs and configures the native Unlimited-OCR plugin for DeepSeek Harness through the DSH Settings GUI for long-document OCR and document-to-Markdown workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aidenwu0209](https://clawhub.ai/user/aidenwu0209)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to install, configure, verify, and troubleshoot Unlimited-OCR in DeepSeek Harness with Baidu Cloud or a local OpenAI-compatible service. It supports GUI setup for OCR over PDFs, OFD, Office files, text, scanned images, tables, formulas, and reading order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup installs a plugin from a referenced GitHub repository and uses DeepSeek Harness tooling.

Mitigation: Confirm trust in the referenced plugin and DSH tooling before installation.

Risk: OCR provider configuration may involve API keys or remote services.

Mitigation: Enter API keys only through DSH Credentials and review provider choices before connecting cloud or remote OCR services.

Risk: The workflow starts a local web server during setup.

Mitigation: Expect the local server, verify the real Web URL responds, and confirm the Unlimited-OCR Settings panel is visible before reporting success.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aidenwu0209/skills/dsh-unlimited-ocr-skill-setup)
- [Publisher profile](https://clawhub.ai/user/aidenwu0209)
- [Project homepage](https://github.com/Aidenwu0209/dsh-Unlimited-OCR-Skill)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown]

**Output Format:** [Markdown with inline shell commands and setup checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports prerequisite versions, commands run, local web URL, provider status, and values still required from the user.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
