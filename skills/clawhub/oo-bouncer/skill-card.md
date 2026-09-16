## Description:

Bouncer (usebouncer.com). Use this skill for Bouncer requests that read, create, update, or delete data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to verify email addresses and domains, manage Bouncer batch and toxicity-list jobs, and check Bouncer credit balances through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes pipe-to-shell installer examples that can create local execution risk.

Mitigation: Prefer a verified package or inspect and verify the installer before running it.

Risk: Inline shell JSON payloads can be malformed or expose sensitive values in command history.

Mitigation: Prefer passing JSON payloads through a file and validate the action schema before execution.

Risk: Write and destructive Bouncer actions can create, finish, or delete service-side jobs and stored results.

Mitigation: Confirm the exact payload, target, and effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Bouncer Skill](https://clawhub.ai/oomol/skills/oo-bouncer)
- [Bouncer Homepage](https://www.usebouncer.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts the agent to inspect live action schemas before building payloads and to request confirmation for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
