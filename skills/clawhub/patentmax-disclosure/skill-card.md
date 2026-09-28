## Description:

Turns R&D materials or an early invention idea into a PatentMax technical-disclosure workflow for generating Word disclosure documents and review notes with a PatentMax API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, invention teams, and patent teams use the skill to prepare PatentMax technical disclosure generation jobs from project materials or early invention ideas, then retrieve disclosure and review-note Word documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected invention materials are uploaded to PatentMax and may include sensitive unfiled patent information.

Mitigation: Minimize submitted files and confirm the upload is allowed under the user's confidentiality policy before running paid create or ideas commands.

Risk: PATENTMAX_API_KEY is required for paid API calls.

Mitigation: Store the key as a secret, avoid pasting it into prompts or committed files, and rotate it if exposure is suspected.

Risk: PATENTMAX_BASE_URL can redirect API traffic to a non-default endpoint.

Mitigation: Leave PATENTMAX_BASE_URL unset unless the endpoint is fully trusted.

Risk: Downloaded Word output paths are chosen by the user or agent.

Mitigation: Use safe output filenames and avoid overwriting important local documents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ip930/skills/patentmax-disclosure)
- [Publisher profile](https://clawhub.ai/user/ip930)
- [PatentMax API console](https://api.ip930.com)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [Materials guide](references/materials-guide.md)
- [Workflow](references/workflow.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command results; generated artifacts are Word .docx files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces PatentMax API jobs for idea directions, technical disclosure documents, review notes, status checks, cancellation, and downloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
