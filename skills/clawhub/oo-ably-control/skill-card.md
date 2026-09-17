## Description:

Ably Control (ably.com). Use this skill for ANY Ably Control request: reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Ably Control resources through an OOMOL-connected oo CLI workflow, including apps, API keys, queues, account details, statistics, and resource metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, revoke, and delete Ably Control resources.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

Risk: Security evidence reports a raw Ably Control token action.

Mitigation: Do not ask the agent to retrieve or display current account credentials.

Risk: Security evidence reports unverified remote installer execution in setup guidance.

Mitigation: Prefer a verified, pinned installation method for the oo CLI before use.

## Reference(s):

- [Ably Control homepage](https://ably.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ably-control)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run oo CLI commands that return JSON responses from Ably Control connector actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
