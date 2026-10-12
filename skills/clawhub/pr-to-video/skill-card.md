## Description:

Turns a GitHub pull request into a narrated code-change explainer video using its diff, commits, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to explain a GitHub pull request as a short video, showing the change and its impact with source-grounded code examples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned HyperFrames tooling can update globally installed skills and install registry blocks.

Mitigation: Run in a sandbox and review and approve update and installation steps before execution.

Risk: The workflow accesses authenticated GitHub pull-request data and may use HeyGen credentials for audio.

Mitigation: Use appropriately scoped credentials and review the PR data and audio-provider access before running.

Risk: Rendering can start a local background preview server.

Mitigation: Review and approve preview and render steps, and stop the project preview server when finished.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/heygen-com/skills/pr-to-video)
- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Code vocabulary](references/code-vocabulary.md)
- [Motion language](references/motion-language.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Video files]

**Output Format:** [Markdown production plan, HTML frames, and MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video format and narration depend on the approved brief; the final render includes a contact sheet.]

## Skill Version(s):

1.0.49 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
