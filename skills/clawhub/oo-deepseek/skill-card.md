## Description:

DeepSeek (platform.deepseek.com). Use this skill for ANY DeepSeek request: reading, creating, and updating data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate DeepSeek through OOMOL's connector, including chat completions, Anthropic-compatible messages, balance checks, and model listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run a remote oo CLI installation script.

Mitigation: Install only if comfortable using OOMOL as the intermediary, and verify the installer or use OOMOL's documented installation flow before running it.

Risk: Write actions can create DeepSeek messages or completions through the connected account.

Mitigation: Review payloads and confirm user intent before approving write actions.

## Reference(s):

- [DeepSeek homepage](https://platform.deepseek.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-deepseek)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI and returns connector responses with data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
