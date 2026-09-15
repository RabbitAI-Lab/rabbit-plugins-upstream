## Description:

Operates Twilio through an OOMOL-connected oo CLI connector for reading account data and creating outbound calls or messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Twilio connector schemas, fetch Twilio account, call, message, and usage data, and send messages or create outbound calls through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Twilio activity is routed through OOMOL as a third-party service.

Mitigation: Review the skill before installing and use it only when routing Twilio work through OOMOL is acceptable.

Risk: First-time setup references remote installer commands for the oo CLI.

Mitigation: Prefer a verified or package-manager install path, and inspect installer commands before running them.

Risk: Write actions can send messages, create calls, affect accounts, and incur costs.

Mitigation: Approve write actions only after checking phone numbers, message content, call parameters, account impact, and possible cost.

## Reference(s):

- [Twilio homepage](https://www.twilio.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-twilio)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on live Twilio connector schemas and oo CLI JSON responses.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
