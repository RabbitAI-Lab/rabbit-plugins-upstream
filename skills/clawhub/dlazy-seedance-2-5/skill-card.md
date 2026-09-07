## Description:

ByteDance's next-generation video model: up to 30 seconds per clip with native 4K, substantially better instruction following and long-form narrative, multi-modal references, and first/last frame control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Seedance 2.5 video generation from an agent, providing prompts and optional image, video, audio, or first/last-frame references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a pinned third-party npm CLI.

Mitigation: Review the linked dLazy CLI source or npm package before installation, and prefer npx or an isolated environment when a persistent global install is unnecessary.

Risk: Prompts, parameters, and selected local media are sent to dLazy hosted endpoints.

Mitigation: Use only prompts and media that are appropriate to upload to dLazy, and avoid passing sensitive or restricted files.

Risk: The dLazy API key may be stored in the local CLI config or supplied through an environment variable.

Mitigation: Limit key exposure, rotate or revoke the key when access is no longer needed, and revoke it immediately if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files]

**Output Format:** [JSON result envelope with generated media URLs or async task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May download generated media assets when --save is used; async mode returns a generateId for polling.]

## Skill Version(s):

1.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
