## Description:

Generate digital human broadcast videos from a portrait image and audio or text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to generate digital human presenter videos from a portrait and audio or text through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the external CLI package executes software fetched from npm.

Mitigation: Review the package and its source before installation.

Risk: Portraits, audio, and prompts supplied to the skill are sent to dLazy's hosted service.

Mitigation: Submit only media and prompts you are comfortable sharing with the service.

Risk: The CLI may save an API key in local configuration.

Mitigation: Use the per-invocation DLAZY_API_KEY environment variable if you do not want a locally saved key.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI source (listed in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Text guidance with shell commands; generation results are JSON with media URLs or an asynchronous task ID.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media can be downloaded locally with the CLI's save option.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
