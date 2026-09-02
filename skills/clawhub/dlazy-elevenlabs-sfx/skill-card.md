## Description:

ElevenLabs text-to-sound generation for creating 1-22 second sound effects from a prompt, including foley, ambience, alerts, and game SFX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy CLI for short sound-effect generation from text prompts. It supports configuring duration and prompt influence, running dry runs, polling asynchronous jobs, and saving generated assets locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and intentionally supplied files may be sent to dLazy's hosted service.

Mitigation: Avoid submitting confidential or unapproved content, and only provide files that are appropriate for processing by the hosted service.

Risk: Saved API keys can remain in the local CLI configuration until removed or revoked.

Mitigation: Use per-invocation DLAZY_API_KEY or npx for less persistent use, and rotate or revoke keys from the dLazy dashboard when access should change.

Risk: Generated outputs are hosted by dLazy.

Mitigation: Review sharing, retention, and distribution expectations before using hosted output URLs in downstream workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI can return hosted generated asset URLs or save generated assets locally when requested.]

## Skill Version(s):

1.3.10 (source: server release evidence; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
