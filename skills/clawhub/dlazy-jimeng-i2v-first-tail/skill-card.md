## Description:

Guides agents to generate transition videos from a first and last image using Jimeng through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short transition videos between two supplied frames through dLazy's hosted Jimeng service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted prompts and selected media are sent to dLazy's hosted service.

Mitigation: Confirm that the material is appropriate to share with dLazy before submitting it.

Risk: Using the third-party CLI involves package trust and API-key handling.

Mitigation: Review the pinned package or source before installation; use DLAZY_API_KEY if you prefer not to save a key locally.

Risk: Documented example flags and output type may be inaccurate.

Mitigation: Check the CLI help and actual result before relying on examples or processing outputs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source linked in skill metadata (not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with CLI commands and result descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return hosted result URLs or an asynchronous task ID; example output and flags in the skill may be inaccurate.]

## Skill Version(s):

1.3.22 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
