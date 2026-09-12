## Description:

Guides agents through OKX CLI authentication, including site selection, OAuth device authorization, API-key checks, login status, logout, and auth binary management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to connect an OKX account for authenticated OKX CLI workflows, recover from expired sessions, check login status, and manage the auth helper binary. It supports both OAuth device authorization and API-key configuration decision points before using related OKX trading, portfolio, earn, or bot skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles authentication for a high-impact exchange account and may lead users toward unsafe credential entry.

Mitigation: Prefer OAuth device authorization or local CLI credential entry, and do not paste OKX API keys, secret keys, passphrases, refresh tokens, or session tokens into chat.

Risk: The skill depends on installing and running the OKX CLI and auth helper binary through an under-verified executable path.

Mitigation: Use a pinned, reviewed CLI version where possible and verify the package or source through OKX documentation or organizational controls before installation.

## Reference(s):

- [OKX homepage](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-auth)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces step-by-step authentication instructions and user-facing prompts; does not itself return credentials.]

## Skill Version(s):

1.4.6 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
