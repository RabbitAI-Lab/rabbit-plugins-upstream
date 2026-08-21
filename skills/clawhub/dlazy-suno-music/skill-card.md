## Description:

Generates Suno-style music from prompts, with inspiration and custom lyric modes and options for vocal or instrumental output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Suno music generation workflow from an agent, creating songs from prompts with configurable style, lyric, vocal, and asynchronous execution options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any user-provided media are sent to dLazy hosted services, and generated outputs are hosted by dLazy.

Mitigation: Use only content appropriate for dLazy cloud processing and review dLazy service terms before sending sensitive prompts or media.

Risk: The dLazy API key may be saved in the local CLI configuration unless an environment variable is used instead.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Generation can fail because of missing authentication, insufficient credits, service errors, or safety-policy rejections.

Mitigation: Surface returned error codes to the user, verify authentication before retrying, and use documented recharge or API-key flows when those specific errors occur.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned as hosted output URLs; asynchronous runs may return a task identifier for later polling.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
