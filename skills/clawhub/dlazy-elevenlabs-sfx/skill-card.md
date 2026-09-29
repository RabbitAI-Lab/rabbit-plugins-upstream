## Description:

Generates short sound effects from text descriptions for foley, ambience, alerts, and games using a hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and other users generate short foley, ambience, alert, and game sound effects from text prompts through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running the external dLazy CLI adds a third-party dependency.

Mitigation: Review the pinned @dlazy/cli package before installation.

Risk: The CLI can persist an API key in local configuration.

Mitigation: Use DLAZY_API_KEY per invocation if you do not want the key stored locally.

Risk: Prompts and any explicitly supplied media files are sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive prompts or media unless that transfer is acceptable.

## Reference(s):

- [Published skill on ClawHub](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Audio asset links]

**Output Format:** [Markdown instructions with bash examples; CLI results are JSON with hosted asset URLs or asynchronous task IDs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requests 1–22-second sound effects; the CLI can save returned assets locally.]

## Skill Version(s):

1.3.22 (source: server release metadata; bundled skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
