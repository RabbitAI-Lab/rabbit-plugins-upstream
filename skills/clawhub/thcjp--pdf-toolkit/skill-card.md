## Description:

PDF工具包（专业版） provides agent-facing workflow guidance and example commands or code for PDF creation, editing, conversion, merging, splitting, compression, encryption, watermarking, OCR, and batch processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, document operations teams, and external agent users can use this skill to guide PDF handling workflows such as extracting content, combining files, adding watermarks, encrypting outputs, and preparing batch-processing steps. The release should be treated as guidance and example material rather than a fully verified PDF processing implementation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to read and write local PDF files and run commands for PDF tooling.

Mitigation: Use a controlled working directory, review proposed commands before execution, and limit access to files needed for the task.

Risk: The artifact advertises pro, API, security, OCR, and conversion capabilities that are not verified by the security evidence.

Mitigation: Treat those capabilities as unverified guidance unless a trusted implementation or integration is present and tested.

Risk: PDF inputs and audit logs may contain sensitive information.

Mitigation: Avoid sensitive PDFs unless logs and outputs are protected, and do not provide API keys unless a specific trusted integration requires them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/pdf-toolkit)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, YAML configuration, and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to read and write local PDF files and run PDF tooling commands.]

## Skill Version(s):

1.0.0 (source: server evidence release.version and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
