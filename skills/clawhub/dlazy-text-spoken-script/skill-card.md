## Description:

Guides agents to write seven-part short-video spoken scripts and also directs them through a dLazy image-generation workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to draft conversational, story-driven short-video scripts from a persona, audience pain point, or topic. Its instructions also cover image generation through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The image-generation instructions request terminal execution and installation of a global CLI beyond what spoken-script writing needs.

Mitigation: For script-only tasks, do not install or run the CLI; for image tasks, review the tool and approve each command before execution.

Risk: Using the dLazy service requires login or an API key and can send prompts or supplied media to external services.

Mitigation: Use dLazy only when the external workflow is intended; avoid sending sensitive content and review credential storage and upload scope first.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI source (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Well-paragraphed spoken script; image-generation guidance may include a command and result URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Seven-part script structure; colloquial delivery with concrete people, events, and details]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata; skill frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
