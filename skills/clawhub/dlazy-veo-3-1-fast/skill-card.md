## Description:

Fast response and generation of short videos with Google Veo 3.1 Fast.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or extend short videos through dLazy's hosted Veo 3.1 Fast integration from text prompts and optional image or video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses dLazy's hosted service, so prompts, parameters, and referenced local media may be sent to dLazy endpoints.

Mitigation: Install and run it only when cloud processing by dLazy is intended, and avoid sending sensitive prompts or media unless approved for that service.

Risk: The dLazy API key may be saved in the local CLI config.

Mitigation: Prefer a per-run DLAZY_API_KEY for sensitive environments, or restrict permissions on ~/.dlazy/config.json and rotate or revoke keys when needed.

Risk: Video generation can be cost-bearing.

Mitigation: Use dry-run or otherwise confirm expected cost before running generation commands.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned as hosted file URLs, and the CLI can save result assets to a local path when requested.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
