## Description:

Use this skill for Telnyx requests that read, create, or update account data through an OOMOL-connected Telnyx account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Telnyx connector schemas, read Telnyx messaging resources, and send SMS or MMS messages through an OOMOL-connected Telnyx account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include commands that execute remote installer scripts.

Mitigation: Use an official, pinned, verifiable installer when available, or inspect and verify the downloaded script before execution.

Risk: The send_message action can send real SMS or MMS messages through the connected Telnyx account.

Mitigation: Confirm the exact send_message payload and intended effect with the user before running the write action.

## Reference(s):

- [ClawHub Telnyx skill](https://clawhub.ai/oomol/skills/oo-telnyx)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Telnyx homepage](https://telnyx.com/)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
