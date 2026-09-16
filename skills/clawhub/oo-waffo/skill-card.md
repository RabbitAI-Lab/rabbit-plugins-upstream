## Description:

Waffo Pancake (waffo.ai) helps agents read, create, and update Waffo Pancake resources through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to operate Waffo Pancake accounts through OOMOL, including checkout sessions, stores, products, subscriptions, orders, payments, and refunds. The skill supports both read workflows and state-changing account operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path asks users to execute a remote oo CLI installer.

Mitigation: Prefer a signed or package-manager installation, or inspect and verify the installer before running it.

Risk: Write actions can create stores and products, publish products, cancel subscriptions, or request refunds.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect before approving any write action.

## Reference(s):

- [Waffo Pancake homepage](https://www.waffo.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-waffo)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from connector actions are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
