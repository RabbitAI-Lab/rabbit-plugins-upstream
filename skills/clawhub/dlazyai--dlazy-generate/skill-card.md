## Description:

Selects dLazy CLI models to generate images, video, and audio from user requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to select and run dLazy image, video, and audio generation commands for their requested media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied local media are sent to dLazy's hosted service.

Mitigation: Only submit prompts and media you are comfortable sharing with dLazy.

Risk: CLI authentication can persist an API key in local configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials if persistent storage is undesirable.

Risk: Installing the CLI introduces a third-party package dependency.

Mitigation: Review the pinned npm package and linked CLI source before installing.

## Reference(s):

- [dLazy CLI source (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned through hosted URLs.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata; bundled skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
