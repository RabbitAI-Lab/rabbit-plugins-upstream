## Description:

doc to video, word to video, markdown to video, document to video — parse the document, outline, storyboard, voiceover, build, validate. Use when the user gives a Doc / Word / Markdown file and wants an explainer, report broadcast, or training video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can provide a Word, Markdown, or other document and request an explainer, report, courseware, or training video through the file-to-video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to the dLazy API, and attached local files are uploaded to dLazy media storage.

Mitigation: Only submit documents approved for this service, and review dLazy's terms before use.

Risk: Using the CLI requires an API key, and project listing accesses the signed-in organization's projects.

Mitigation: Use an authorized organization account and rotate or revoke its key through the dLazy dashboard when needed.

Risk: The security review reports medium confidence and partial inspection because some referenced paths were missing; it also notes unusual whitespace.

Mitigation: Review the available referenced material and whitespace before installation; the scan does not establish that all referenced material was inspected.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)

## Skill Output:

**Output Type(s):** [Video, Files, Text]

**Output Format:** [Generated video project assets and streamed CLI text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based workflow; attached input files are uploaded before use.]

## Skill Version(s):

1.0.36 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
