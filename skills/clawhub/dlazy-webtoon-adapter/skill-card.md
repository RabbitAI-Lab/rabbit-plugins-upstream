## Description:

Adapts web novel material into Chinese webtoon drama plans and episode scripts, with optional dLazy CLI image-generation support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, content teams, and developers use this skill to turn web novel chapters or revision notes into genre selection, plot breakdowns, tagged episodes, and per-episode Chinese webtoon scripts. When image generation is requested, it can guide use of the dLazy cloud CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send prompts, novel text, local media, and generated outputs through dLazy cloud services.

Mitigation: Avoid sensitive unpublished chapters or private media unless cloud upload to dLazy services is acceptable for the use case.

Risk: The skill encourages global CLI installation and supports stored API credentials.

Mitigation: Prefer npx or a per-run DLAZY_API_KEY where practical, review the npm package, and rotate or revoke credentials from the dLazy dashboard when needed.

Risk: The artifact combines a text adaptation workflow with image-generation execution guidance and contains version conflicts.

Mitigation: Confirm the intended scope before use and treat image generation as a separate optional workflow unless the publisher clarifies the combined behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI GitHub repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown and structured Chinese prose with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require npm or npx, dLazy API credentials, and cloud uploads through dLazy services when image-generation commands are used.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
