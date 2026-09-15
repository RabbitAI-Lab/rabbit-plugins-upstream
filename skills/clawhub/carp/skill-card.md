## Description:

Manage a local CARP interface for ADILOS trust setup, queue polling, encrypted agent-to-agent requests, menus, results, answers, CABEZON customer workflow, and secure commerce/escrow workflows through local or LAN CARP endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bitsanity](https://clawhub.ai/user/bitsanity)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use CARP to configure local or LAN ADILOS/CARP agents, verify trust setup, process queues, and manage encrypted CABEZON requests, results, escrow, and commerce workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cryptographic identity and private key material may be exposed during deployment or troubleshooting.

Mitigation: Use a dedicated unprivileged account, keep private keys out of web-writable areas, and never print, log, commit, or return private keys.

Risk: Mutable npm dependencies can change runtime behavior after installation.

Mitigation: Pin and audit npm dependencies with a lockfile before installing or operating the CARP interface.

Risk: Hourly monitoring can create persistent background operation.

Mitigation: Do not enable the cron monitor unless persistent operation is explicitly intended and an uninstall plan exists.

Risk: Trust, ACL, escrow, or blockchain actions can affect real counterparties or value.

Mitigation: Require exact user approval before any ACL change, escrow action, or blockchain transaction.

Risk: Unauthenticated or insufficiently pinned transport can weaken trust setup.

Mitigation: Prefer authenticated transport or independently pinned service identities before challenge/response, registration, or ACL changes.

## Reference(s):

- [CARP ClawHub Release](https://clawhub.ai/bitsanity/skills/carp)
- [agent-crvp Reference Implementation](https://github.com/bitsanity/agent-crvp)
- [CABEZON Concierge](https://github.com/bitsanity/cabezon)
- [Nautilus Registrar](https://github.com/bitsanity/nautilus)
- [clawface Escrower](https://github.com/bitsanity/clawface)
- [glassfish Reputation](https://github.com/bitsanity/glassfish)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational safety checks for keys, trust setup, queue processing, ACL changes, and commerce actions.]

## Skill Version(s):

1.0.4 (source: server release evidence; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
