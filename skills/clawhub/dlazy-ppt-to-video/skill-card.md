## Description:

PPT to Video helps an agent turn presentations and other documents into hosted dLazy file-to-video workflows that parse content, outline a storyboard, prepare voiceover, build the video, and validate the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to route PPT, PowerPoint, Keynote, PDF, Word, Excel, or other document-to-video requests through dLazy's hosted file-to-video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, options, and attached local files are sent to dLazy's hosted API and media storage.

Mitigation: Use the skill only for documents that are appropriate to send to dLazy, and avoid attaching sensitive files unless that hosted processing is acceptable.

Risk: The skill name emphasizes PPT-to-video, while the artifact also describes broader document-to-video triggers.

Mitigation: Treat the skill as a document-to-video wrapper and confirm that a task's file types and requested output match the hosted file-to-video workflow.

Risk: Continuing the wrong project id could expose context from an unrelated dLazy project.

Mitigation: List projects first and continue only project ids the user recognizes.

Risk: A persistent global CLI install and stored API key may remain after use.

Mitigation: Use the pinned npx invocation when persistence is not desired, and rotate or remove the dLazy API key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ppt-to-video)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project ids, API-key setup steps, attached-file upload behavior, and hosted service responses.]

## Skill Version(s):

1.0.4 (source: server release evidence; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
