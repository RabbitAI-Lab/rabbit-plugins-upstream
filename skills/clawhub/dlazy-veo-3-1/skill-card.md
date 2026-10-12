## Description:

Helps agents generate videos from text prompts, images, or existing video using Veo 3.1 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent in generating short videos from prompts, reference images, or existing video through dLazy's Veo 3.1 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party CLI executes code on the user's machine.

Mitigation: Review the pinned @dlazy/cli package and its source before installation.

Risk: API credentials may be stored locally or provided to the CLI.

Mitigation: Protect the dLazy API key and rotate or revoke it if exposed.

Risk: Prompts and selected local media are sent to dLazy's hosted service.

Mitigation: Share only prompts and media approved for third-party processing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media may be returned as a hosted URL or saved locally; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
