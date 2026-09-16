## Description:

Converts storyboard context into a canvas-ready video generation pipeline with shared source audio, scene image, cloned audio, and per-storyboard video elements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use this skill to turn storyboard entries, aspect ratio, and resolution into a JSON pipeline that can be drawn onto a canvas for dLazy-backed video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install and run the third-party @dlazy/cli package.

Mitigation: Prefer npx or a local sandboxed install, pin and verify the package version, and review the package source before use.

Risk: Using the skill requires a dLazy API key and may upload prompts or media to dLazy services.

Mitigation: Use only approved data, store the API key securely, and rotate or revoke the key when access is no longer needed.

Risk: Generation commands could be unsafe if assembled from untrusted prompt text.

Mitigation: Review generated commands before execution and avoid direct shell command construction from untrusted input.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON pipeline snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce canvas pipeline JSON and dLazy-hosted media URLs when generation commands are run.]

## Skill Version(s):

1.2.14 (source: server release metadata; artifact frontmatter states 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
