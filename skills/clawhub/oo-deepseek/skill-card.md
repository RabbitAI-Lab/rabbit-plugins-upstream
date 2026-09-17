## Description:

DeepSeek lets agents operate DeepSeek through an OOMOL-connected account with the oo CLI for chat and message creation, model listing, and balance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run DeepSeek connector actions through OOMOL, including creating chat completions or Anthropic-compatible messages, checking account balance, and listing available models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to execute remote installer scripts in a shell.

Mitigation: Install the oo CLI from a verified, version-pinned, checksum- or signature-validated source, and do not allow an agent to run remote install scripts automatically.

Risk: The skill can create DeepSeek messages and chat completions through write actions.

Mitigation: Inspect the live action schema and confirm the exact JSON payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub DeepSeek Skill](https://clawhub.ai/oomol/skills/oo-deepseek)
- [DeepSeek Platform](https://platform.deepseek.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agents should inspect the live connector schema before submitting JSON payloads and confirm write actions before execution.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
