## Description:

Twilio lets agents inspect Twilio connector schemas and run account, call, message, and usage-record actions through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Twilio accounts from an agent, including reading account, call, message, and usage records and initiating outbound calls or SMS/MMS messages after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path asks users to execute a remote installer directly in a shell.

Mitigation: Prefer an official, verifiable installer path and inspect or verify the downloaded installer before running it.

Risk: Twilio write actions can send messages, create calls, and incur account impact.

Mitigation: Confirm the exact action, payload, recipient, and expected effect with the user before executing write actions.

## Reference(s):

- [Twilio skill page](https://clawhub.ai/oomol/skills/oo-twilio)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Twilio homepage](https://www.twilio.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI schema and run commands, JSON request payloads, and returned connector data with execution metadata.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
