## Description:

Helps adapt web novels into webtoon plot breakdowns and episode scripts, with an optional image-generation workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and creators use this skill to turn web-novel chapters into episode outlines and visual scripts. An additional workflow offers image generation through dLazy after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to dLazy, and supplied media files may be uploaded to its service.

Mitigation: Share only material approved for third-party processing and review media paths before use.

Risk: Using the CLI requires an API key stored locally or supplied through an environment variable.

Mitigation: Protect the key, avoid including it in prompts or logs, and rotate it if exposed.

Risk: The skill combines webtoon writing with image-generation commands, and its embedded versions and installation guidance differ from the published release.

Mitigation: Review the package and intended workflow before installation; confirm each generation command before execution.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI source (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown conversation responses with structured outlines, scripts, and optional image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation requires confirmation before each command.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
