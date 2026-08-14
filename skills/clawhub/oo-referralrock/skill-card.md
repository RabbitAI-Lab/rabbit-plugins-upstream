## Description:

Referral Rock (referralrock.com). Use this skill for Referral Rock requests that search and read connected account data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect Referral Rock programs, members, referrals, and member statistics through an OOMOL-connected account. It is intended for read and search workflows, with setup guidance only when authentication or connector access is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can read and search data from the connected Referral Rock account.

Mitigation: Install and enable the skill only for accounts where this read access is intended.

Risk: First-time setup may require installing the oo CLI and connecting Referral Rock with an API key.

Mitigation: Complete setup deliberately using the intended OOMOL account and Referral Rock credentials, and retry setup only after an authentication or connection error.

Risk: Connector schemas and available actions can change over time.

Mitigation: Fetch the live action schema before constructing a payload and review any state-changing payload with the user before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-referralrock)
- [Referral Rock Homepage](https://referralrock.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, API Calls, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Referral Rock actions are described as safe to run directly; state-changing action categories require user confirmation if present.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
