## Description:

This skill guides an agent through using dLazy's hosted file-to-video workflow to turn PDFs and other documents into explainer, report, courseware, or training videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can provide a PDF or other document and use the dLazy hosted agent to create an explainer, report, courseware, or training video, then continue work in a project session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags project listing and CLI authentication as behaviors not clearly aligned with the PDF-to-video purpose, and notes that a broad trigger may select the skill for ordinary report analysis.

Mitigation: Review the skill and CLI behavior before installation, confirm project listing and authentication are appropriate for the task, and narrow activation triggers to document-to-video requests.

Risk: Security analysis was partial because referenced paths or resources could not be resolved, so the available assessment is incomplete.

Mitigation: Review the unresolved CLI and referenced resources before installation and treat the security assessment as incomplete until they are checked.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository link listed in the skill documentation](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Video, Text, Guidance]

**Output Format:** [Generated video with streamed text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports project-based follow-up and optional document or image attachments. Requires a dLazy API key.]

## Skill Version(s):

1.0.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
