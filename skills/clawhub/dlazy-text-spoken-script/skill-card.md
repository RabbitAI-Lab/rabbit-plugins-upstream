## Description:

Guides agents to write conversational, story-driven short-video spoken scripts using a seven-step structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to draft spoken scripts for short videos, character stories, and personal-brand viewpoints. The artifact also includes optional instructions to generate images through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A spoken-script request may trigger installation and execution of a third-party image-generation CLI.

Mitigation: Review the skill before installing; use a text-only version unless dLazy image generation is specifically desired.

Risk: dLazy authentication stores an API key locally, and prompts or supplied media may be sent to dLazy services.

Mitigation: Use only an authorized account, protect credentials, and avoid sending confidential prompts or files.

Risk: Optional image-generation requests may consume account quota.

Mitigation: Confirm intended image generation and quota use before invoking the CLI.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI source (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Plain text or Markdown, with optional shell commands for image generation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Spoken scripts follow seven story beats; image-generation instructions may return hosted image URLs.]

## Skill Version(s):

1.3.33 (source: ClawHub server release; embedded skill frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
