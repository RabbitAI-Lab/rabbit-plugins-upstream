## Description:

CommPeak helps agents operate CommPeak TextPeak streams through the OOMOL oo CLI to inspect schemas, retrieve messaging resources, and send SMS messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with CommPeak TextPeak account resources through an OOMOL-connected account, including listing streams, domains, messages, and senders. With user confirmation for write actions, it can send SMS messages through TextPeak streams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can run an unverified remote installer directly in a shell.

Mitigation: Review the installer path before installation and prefer a pinned or signed oo CLI release with checksum verification.

Risk: The send_sms action can send messages that affect recipients and account usage.

Mitigation: Approve SMS-sending actions only after checking the exact recipients, message body, stream, and expected account impact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-commpeak)
- [CommPeak homepage](https://www.commpeak.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [CommPeak connection page](https://console.oomol.com/app-connections?provider=commpeak)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI command results containing connector data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
