## Description:

Generates coherent transition videos from a first frame, last frame, and prompt using Jimeng through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate transition videos from supplied first and last frame images through dLazy's hosted Jimeng workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Invoking the skill can upload selected media files and prompts to dLazy-hosted services.

Mitigation: Use only content approved for dLazy processing and storage, and review the service terms before sending sensitive media.

Risk: Generation requests may consume dLazy credits.

Mitigation: Use dry-run or cost-estimation behavior when available and confirm account balance before long or repeated runs.

Risk: The artifact examples appear inconsistent with the documented firstFrame and lastFrame CLI flags.

Mitigation: Run `dlazy jimeng-i2v-first-tail -h` and follow the live help output before invoking the generation command.

Risk: Global installation persists the dLazy CLI on the local system.

Mitigation: Use the pinned `npx @dlazy/cli@1.2.3` option when a non-persistent invocation is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, json, guidance]

**Output Format:** [Markdown instructions with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return completed media URLs or an asynchronous task identifier; local media paths can be uploaded to dLazy storage when invoked.]

## Skill Version(s):

1.3.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
