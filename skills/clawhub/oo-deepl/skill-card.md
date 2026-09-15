## Description:

DeepL (deepl.com). Use this skill for ANY DeepL request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate DeepL through an OOMOL-connected account, including checking API usage, listing supported languages, and translating one or more text items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Review the oo CLI installation path first and prefer a trusted, versioned, verifiable installer source.

Risk: Text submitted for translation may include confidential content processed by OOMOL and DeepL.

Mitigation: Avoid submitting confidential text unless the user is comfortable with OOMOL and DeepL processing it.

## Reference(s):

- [ClawHub DeepL Skill](https://clawhub.ai/oomol/skills/oo-deepl)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [DeepL Homepage](https://www.deepl.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence release version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
