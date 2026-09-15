## Description:

Guides agents through OKX CLI authentication, including OAuth device flow setup, API-key detection, re-authentication, logout, and auth-binary troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an OKX account to the OKX CLI, recover from authentication failures, and manage the local OKX auth binary. It is intended for authentication setup before using OKX trading, portfolio, earn, or bot workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may expose OKX API keys, secret keys, passphrases, OAuth tokens, or recovery material in chat.

Mitigation: Do not paste credentials into chat; use the local OKX CLI prompt or OAuth device flow.

Risk: The release relies on globally installed or downloaded OKX auth tooling with unclear integrity guarantees.

Mitigation: Prefer a pinned CLI install and verify the package and auth-binary provenance where possible before use.

Risk: The OKX CLI auth binary and some authentication state persist locally.

Mitigation: Review local persistence expectations and remove or log out of auth tooling when it is no longer needed.

## Reference(s):

- [OKX Homepage](https://www.okx.com)
- [ClawHub Skill Page](https://clawhub.ai/searchworld/skills/okx-cex-auth)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and authentication guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts users to choose an OKX site and keeps credential handling in the local OKX CLI or OAuth device flow.]

## Skill Version(s):

1.4.7 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
