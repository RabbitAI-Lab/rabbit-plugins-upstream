## Description:

Guides the design of short-lived, revocable authorization for AI agents using a local credential broker that keeps secrets out of model context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); all rights reserved (documentation and methodology)

## Use Case:

Developers and engineers use this skill to plan time-limited, scoped, auditable access for AI agents or local applications without placing saved credentials in model context. The included local broker is a prototype, not a production-safe credential manager.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The prototype's access controls can expose saved passwords too broadly.

Mitigation: Before using real vaults, separate administrator and delegated permissions, enforce token scopes, and restrict who can issue or fulfill tokens.

Risk: The broker PIN can leak through URLs or output.

Mitigation: Remove PIN-in-URL and PIN-in-output behavior before handling real credentials.

Risk: Running the included prototype against real vaults could compromise credentials.

Mitigation: Review the skill before installation or execution and treat the broker as a prototype until its access controls and PIN handling are corrected.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/authz-code-design)
- [Local broker architecture diagram](artifact/references/broker-arch.svg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown with code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Design guidance for short-lived tokens, credential isolation, audit, and revocation.]

## Skill Version(s):

1.1.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
