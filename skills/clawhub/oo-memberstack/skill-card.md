## Description:

Operates Memberstack through an OOMOL-connected account for member lookup, listing, creation, updates, plan changes, deletion, and JWT verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Memberstack members through OOMOL's connector without handling raw Memberstack API tokens directly. It supports read, write, and destructive account-data workflows when the user approves the action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector can create, update, delete, and modify plan data in a Memberstack account.

Mitigation: Require explicit user approval for write and destructive actions, and confirm the target, payload, and expected effect before execution.

Risk: OOMOL's connector operates the connected Memberstack account with server-side credentials.

Mitigation: Install only when the user accepts OOMOL operating the account, and keep Memberstack scopes limited to the workflows the user intends to run.

Risk: First-time setup includes remote oo CLI install commands.

Mitigation: Prefer reviewing the official oo CLI installer or using a verified installation method before running remote install commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-memberstack)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Memberstack homepage](https://www.memberstack.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live oo connector schema before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
