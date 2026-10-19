## Description:

Turns themes, outlines, or structured copy into shot-by-shot short-video storyboard scripts with scene direction and spoken lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to turn supplied copy into a filming plan with individual shots, camera direction, and spoken script.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Despite its text-only storyboard purpose, the skill also directs use of an external image-generation CLI.

Mitigation: Review the skill before installation and require explicit user confirmation before installing or running the CLI; use text-only drafting when image generation is not requested.

Risk: CLI use may store an API key locally, send prompts or referenced media to dLazy services, and consume account quota.

Mitigation: Confirm the intended data and account before CLI use; avoid sharing sensitive material and review potential quota costs.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI source referenced in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown storyboard with video parameters and shot-by-shot filming notes and spoken lines]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves supplied copy in the spoken lines; defaults to a 9:16 aspect ratio and 720p resolution when unspecified.]

## Skill Version(s):

1.2.27 (source: server release metadata; artifact frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
