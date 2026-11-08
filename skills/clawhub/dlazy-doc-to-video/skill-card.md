## Description:

doc to video, word to video, markdown to video, document to video — parse the document, outline, storyboard, voiceover, build, validate. Use when the user gives a Doc / Word / Markdown file and wants an explainer, report broadcast, or training video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and teams can turn Word, Markdown, and other documents into explainer, report, courseware, or training videos. The skill guides project-based requests to dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to dLazy's hosted service; attached files are uploaded to its media storage.

Mitigation: Upload only documents you are authorized to share, select the intended project, and review the service's data-retention terms.

Risk: The external CLI executable and hosted service were not verified by this artifact review.

Mitigation: Review the CLI and service before relying on them, and prefer device-code login over entering API keys in shell commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Video, Text, Guidance]

**Output Format:** [Generated video content with CLI text status and follow-up guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documents attached for processing are uploaded to dLazy media storage.]

## Skill Version(s):

1.0.35 (source: server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
