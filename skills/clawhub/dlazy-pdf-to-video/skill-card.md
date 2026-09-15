## Description:

pdf to video, pdf to explainer video, pdf to presentation video - parse the PDF, outline, storyboard, voiceover, build, validate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn PDFs and other documents into explainer, report, courseware, or training videos through the dLazy file-to-video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm CLI and dLazy services.

Mitigation: Install only if you trust dLazy and @dlazy/cli; prefer npx or another contained environment when you do not want a global binary.

Risk: User-selected local files may be uploaded to dLazy media storage.

Mitigation: Avoid uploading sensitive documents unless dLazy's terms and data handling fit the use case.

Risk: The dLazy API key may be saved in local CLI configuration.

Mitigation: Use environment-scoped credentials where appropriate and rotate or revoke the API key when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)
- [dlazyai publisher profile](https://clawhub.ai/user/dlazyai)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with inline shell commands and streamed CLI text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require dLazy authentication and may upload user-selected local files to dLazy services.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter says 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
