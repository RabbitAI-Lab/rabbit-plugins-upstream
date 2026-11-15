## Description:

Suno music generation model. Supports inspiration mode (auto lyrics) and custom mode (manual lyrics), generating music with or without vocals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate Suno music from a prompt, with automatically generated or custom lyrics and optional vocals or instrumental output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires installing the pinned dLazy CLI and signing in, and the security review could not establish how the login flow supports music generation.

Mitigation: Review the CLI project and its authentication flow before installing or signing in; use an API key that can be rotated or revoked.

Risk: Prompts and any supplied local media are sent to dLazy-hosted services for generation; the security evidence is incomplete because some referenced items were unavailable.

Mitigation: Avoid sending sensitive prompts or media, and review the service terms and data handling practices before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio files, JSON, Shell commands]

**Output Format:** [Generated audio asset URL in a JSON response, with an optional downloaded audio file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can generate music with vocals or as instrumentals; asynchronous requests may initially return a task identifier.]

## Skill Version(s):

1.3.39 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
