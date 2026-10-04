## Description:

Adapts web novels into Chinese-language webtoon plot breakdowns and episode scripts, with optional image generation through dLazy's cloud CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and creators use this skill to turn supplied web-novel chapters into episode outlines and visual scripts, and may request images generated through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image generation invokes an external CLI and cloud service beyond the webtoon-writing task.

Mitigation: Install and use the dLazy CLI only if cloud image generation is intended; review the package before running it.

Risk: Login or manual key setup can persist a dLazy API key on the local machine.

Mitigation: Use a per-run DLAZY_API_KEY instead of saving a key when persistent credentials are unnecessary.

Risk: Providing local image, video, or audio paths can upload those files to dLazy-hosted services.

Mitigation: Only provide local media paths when the files are appropriate to upload.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI source referenced in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Image URLs]

**Output Format:** [Chinese-language conversational text and structured Markdown, with optional image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Episode outlines and scripts are returned in conversation; optional image results are hosted by dLazy.]

## Skill Version(s):

1.3.25 (source: ClawHub release; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
