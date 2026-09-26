## Description:

Guides agents through OKX CLI authentication, including site selection, OAuth device-flow login, API-key setup, re-authentication, logout, and okx-auth binary management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[numpy0001](https://clawhub.ai/user/numpy0001)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an OKX account to the OKX CLI, choose the correct OKX site, recover from authentication failures, and manage local authentication state. It is intended for account-authentication workflows before authenticated OKX trading, portfolio, earn, or bot skills are used.

### Deployment Geography for Use:

Global, with explicit site choices for Global, EEA, and US endpoints.

## Known Risks and Mitigations:

Risk: Financial account authentication can expose OKX API credentials or authorization details if sensitive values are entered into chat.

Mitigation: Enter OKX API credentials only through local CLI prompts, and avoid sharing API keys, secret keys, or passphrases in assistant messages.

Risk: Installing or updating the OKX CLI and okx-auth binary crosses package and binary trust boundaries.

Mitigation: Confirm the exact package version and trust boundary before installation, update, or binary repair steps.

Risk: Force-removing auth components can disrupt local OKX authentication.

Mitigation: Use removal only when explicitly intended, and reserve force removal for cases where the user has confirmed that disruption is acceptable.

## Reference(s):

- [OKX homepage](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/numpy0001/skills/okx-cex-auth)
- [Source skill artifact](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON parsing instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local OKX CLI access and user confirmation for site selection, OAuth completion, API-key replacement, and auth binary removal.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter reports 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
