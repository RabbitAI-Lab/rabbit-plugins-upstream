## Description:

Intercom helps agents read, create, and update Intercom data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Support, operations, and developer teams use this skill to manage Intercom workspace data from an agent, including contacts, conversations, companies, articles, tickets, events, tags, and counts. It supports read workflows and user-confirmed write workflows such as creating or updating contacts and replying to conversations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded code directly.

Mitigation: Review installer steps before use and prefer a verified, versioned release or package manager with checksum or signature validation.

Risk: Intercom write actions can create or update contacts and close, reopen, or reply to conversations.

Mitigation: Require explicit approval for the exact payload and expected effect before running any write action.

## Reference(s):

- [Intercom homepage](https://www.intercom.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-intercom)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector actions; write actions require explicit user confirmation.]

## Skill Version(s):

1.0.4 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
