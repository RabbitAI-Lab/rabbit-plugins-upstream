## Description:

Generate high-quality cinematic effects videos with Google Veo 3.1, supporting text-to-video and image-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate cinematic videos through the dLazy CLI and hosted Veo 3.1 API, using text prompts and optional image or video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media inputs may be sent to the dLazy hosted service for generation.

Mitigation: Use the service only with data appropriate for third-party processing, and review the dLazy terms before sending sensitive media or prompts.

Risk: The CLI can store an API key locally and requests may consume account credits.

Mitigation: Prefer `npx @dlazy/cli@1.2.3` or `--dry-run` for initial review, rotate or revoke API keys from the dashboard when needed, and monitor credit usage.

Risk: Documentation examples contain minor inconsistencies that may cause invocation errors.

Mitigation: Run `dlazy veo-3.1 -h` and verify current CLI options before executing generation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy CLI metadata source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown guidance with shell commands and JSON CLI output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media URLs may be returned by the hosted API; asynchronous runs can return a task identifier for polling.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
