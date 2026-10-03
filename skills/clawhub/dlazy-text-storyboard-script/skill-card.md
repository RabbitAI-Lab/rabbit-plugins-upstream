## Description:

Creates detailed short-video storyboard scripts from themes, outlines, or supplied copy, with an optional dLazy image-generation workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and video production teams use this skill to turn themes, outlines, or existing copy into shot-by-shot short-video scripts with visual directions and spoken lines. An optional workflow offers image generation through dLazy after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional image workflow may install and invoke the dLazy CLI even though the skill is labeled a text storyboard generator.

Mitigation: Review the workflow before installing; use image generation only when it is explicitly wanted and confirmed.

Risk: dLazy CLI authentication stores an API key, and generation can send prompts or media to dLazy services and consume account resources.

Mitigation: Confirm the external service and costs are acceptable; avoid sensitive inputs and protect or revoke the API key as needed.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Markdown storyboard with video parameters, numbered shots, and optional image prompts or CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Spoken lines preserve supplied copy; image generation requires separate user confirmation.]

## Skill Version(s):

1.2.20 (source: ClawHub release metadata; embedded skill frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
