## Description:

Kuaidi100 (kuaidi100.com) supports Kuaidi100 requests involving reading, creating, and updating logistics and pickup-order data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run Kuaidi100 logistics workflows through an OOMOL-connected account, including tracking, carrier detection, delivery estimates, pickup-order quotes, order creation, order lookup, and cancellation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that can execute local code.

Mitigation: Review installation instructions before use; prefer an official package manager or a pinned, verified installer for the oo CLI.

Risk: Some Kuaidi100 actions create, cancel, quote, or query pickup orders and can affect account state or billing.

Mitigation: Confirm create, cancel, and other write payloads with the user before running connector actions.

## Reference(s):

- [Kuaidi100 homepage](https://www.kuaidi100.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kuaidi100)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON with data and meta.executionId when run with --json.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
