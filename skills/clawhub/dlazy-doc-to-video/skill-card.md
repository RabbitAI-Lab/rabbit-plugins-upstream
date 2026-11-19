## Description:

doc to video, word to video, markdown to video, document to video — parse the document, outline, storyboard, voiceover, build, validate. Use when the user gives a Doc / Word / Markdown file and wants an explainer, report broadcast, or training video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and teams use this skill to turn Word, Markdown, and other documents into explainer, report, courseware, or training videos through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires account authentication and can list organization projects, which the security analysis flagged as potentially outside the document-to-video task.

Mitigation: Review these steps before installing, and authenticate with the intended dLazy organization only when project access is needed.

Risk: Documents attached to a request are uploaded to dLazy media storage for processing.

Mitigation: Attach only files approved for processing by the dLazy service.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video files, Guidance]

**Output Format:** [Generated explainer, report, courseware, or training video with conversational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; attached files are uploaded to dLazy media storage for processing.]

## Skill Version(s):

1.0.40 (source: server-resolved release metadata; artifact frontmatter lists 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
