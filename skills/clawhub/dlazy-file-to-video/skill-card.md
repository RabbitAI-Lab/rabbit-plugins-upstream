## Description:

PPT to video, Word to video, Excel to video, PDF to video, document to video — parse, outline, storyboard, voiceover, build, validate. Use when the user gives a document and wants an explainer, report broadcast, courseware, or training video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can provide a presentation, document, or spreadsheet and use the dLazy file-to-video assistant to create an explainer, report, courseware, or training video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to dLazy services; the external CLI package and hosted backend were not audited in this review.

Mitigation: Upload only documents you are comfortable sharing with dLazy, confirm the intended organization and project, and review data-retention terms before sending sensitive material.

Risk: The CLI saves an API key in its local configuration when login or manual authentication is used.

Mitigation: Protect the saved API key and rotate or revoke it from the organization dashboard if needed.

## Reference(s):

- [dLazy CLI project page (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)

## Skill Output:

**Output Type(s):** [Video, Text, Shell commands]

**Output Format:** [Generated explainer, report, courseware, or training video with streamed text responses; CLI commands are shown as shell snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped sessions; optional local reference files are uploaded for processing.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
