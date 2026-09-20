## Description:

Generates dynamic videos from a first-frame image and prompt using Jimeng through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent invoke dLazy's Jimeng image-to-video CLI with a prompt, first-frame image, duration, wait/save options, and return generation results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the external dLazy CLI globally persists a third-party binary on the user's system.

Mitigation: Prefer the pinned `npx @dlazy/cli@1.2.3` invocation or review the external package before global installation.

Risk: Input images and prompts are sent to dLazy services for generation, and generated outputs are hosted by dLazy.

Mitigation: Only submit images and prompts suitable for upload to dLazy, and review applicable account and service policies before use.

Risk: Saved API keys can remain in the local dLazy CLI configuration.

Mitigation: Use `DLAZY_API_KEY` per run when persistent credentials are not desired, and rotate or revoke organization keys as needed.

Risk: The artifact examples use `--image` while the help text lists `--firstFrame`, creating command ambiguity.

Mitigation: Run `dlazy jimeng-i2v-first -h` before execution and use the flag names shown by the installed pinned CLI version.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI Homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON, Files]

**Output Format:** [Markdown guidance with CLI commands; the dLazy command returns JSON and hosted or downloaded media outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports dry run, async generateId polling, timeout control, and optional local save path.]

## Skill Version(s):

1.3.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
