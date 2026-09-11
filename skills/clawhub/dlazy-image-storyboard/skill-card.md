## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict plan-first, render-later flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, designers, educators, and production teams use this skill to convert creative briefs into structured storyboard plans, character references, panel prompts, and delivery guidance. It supports cinematic, advertising, short-video, educational, and comic-style narrative storyboard workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm CLI that can receive prompts, API keys, and selected media files.

Mitigation: Use npx or an isolated environment, review the referenced CLI package before use, and only provide content that is appropriate for dLazy's cloud service.

Risk: Local API keys may persist in the dLazy CLI configuration after setup.

Mitigation: Rotate or revoke the dLazy API key when access is no longer needed, and prefer per-run environment variables when avoiding persistent configuration is important.

Risk: Server-resolved import provenance is unavailable for this release.

Mitigation: Treat ownership as the server-resolved ClawHub publisher only and confirm the package/source relationship before broader deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with bulleted workflow plans, storyboard prompts, inline shell commands, generated image URLs, and final storyboard delivery guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation at workflow gates before image generation commands are run.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
