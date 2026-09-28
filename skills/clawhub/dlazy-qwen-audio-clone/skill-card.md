## Description:

Guides agents in cloning a speaker's voice from a clean audio sample for later text-to-speech use through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to provide an authorized voice sample and create a custom voice for later text-to-speech requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples may be uploaded to dLazy's hosted service without clear consent, retention, or deletion guidance.

Mitigation: Upload samples only with the speaker's clear permission, and review dLazy's terms for retention, deletion, and permitted use of cloned voices.

Risk: Logging in can store an API key locally.

Mitigation: Protect the local key, review the CLI's credential handling, and rotate or revoke the key if exposure is suspected.

Risk: Mismatched command examples and output schema may mislead users or agents.

Mitigation: Check the CLI help and actual response before invoking cloning or relying on returned fields.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documented response examples are inconsistent; verify actual voice-cloning results and asynchronous task fields before reuse.]

## Skill Version(s):

1.3.21 (source: ClawHub release evidence; skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
