## Description:

Winston AI (gowinston.ai). Use this skill for ANY Winston AI request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run Winston AI checks through an OOMOL-connected account. It supports AI text detection, plagiarism checks, text similarity comparison, and claim fact-checking for text, public document URLs, or public website URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote shell installer commands for the oo CLI.

Mitigation: Review the installer path before use and prefer verified official packages or documentation with checksum or signature verification.

Risk: Submitted text, public document URLs, or website URLs may be processed by OOMOL and Winston AI as external services.

Mitigation: Avoid sending confidential, regulated, credential-bearing, or proprietary text unless external processing by OOMOL and Winston AI is acceptable.

## Reference(s):

- [Winston AI homepage](https://gowinston.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Winston AI skill page](https://clawhub.ai/oomol/skills/oo-winston-ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
