## Description:

OCR.space lets an agent extract text from images and retrieve OCR.space conversion statistics through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run OCR.space OCR tasks, including extracting text from public image URLs or uploaded Base64 image files and checking monthly conversion statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes an unverified internet installer for the oo CLI.

Mitigation: Review installation before use, install the CLI from a trusted versioned source, verify checksums or signatures when available, and do not allow an agent to run the installer automatically.

Risk: OCR actions depend on a local oo CLI session and a connected OCR.space account.

Mitigation: Run first-time authentication or connection steps only after a matching command failure, and keep raw OCR.space credentials out of agent-visible prompts and files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ocrspace)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OCR.space homepage](https://ocr.space)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches the live connector schema before constructing action payloads; returns normalized OCR page results and execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
