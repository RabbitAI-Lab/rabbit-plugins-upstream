## Description:

Use when authenticating or authorizing requests to any Mailtrap API, including choosing the auth header, token scope, safe token storage, and resolving the Mailtrap account_id before writing or generating API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mailtrap](https://clawhub.ai/user/mailtrap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to generate Mailtrap API requests that apply the correct authorization header, token scope, secret handling pattern, and account_id resolution approach. It is also useful when debugging 401 or 403 responses caused by authorization or scope mistakes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated examples may expose Mailtrap API tokens if users paste literal secrets into chat, source files, command-line flags, or generated code.

Mitigation: Use scoped tokens from environment variables or secret stores, never echo literal secrets, and rotate any token that is pasted or committed.

Risk: Using the wrong Mailtrap token scope or mixing sandbox and live sending tokens can cause authorization failures or unintended live email sends.

Mitigation: Provision narrowly scoped tokens, keep sandbox and live tokens separate, and verify account access levels before write operations.

Risk: Hardcoded account_id values can target the wrong Mailtrap account when scripts move between users, teams, or environments.

Mitigation: Resolve account_id from the Accounts API at runtime and pass it through MAILTRAP_ACCOUNT_ID.

## Reference(s):

- [Mailtrap API Tokens](https://mailtrap.io/api-tokens)
- [Mailtrap API tokens documentation](https://docs.mailtrap.io/email-api-smtp/setup/api-tokens.md)
- [Mailtrap Accounts API](https://docs.mailtrap.io/developers/account-management/accounts)
- [ClawHub skill page](https://clawhub.ai/mailtrap/skills/authorizing-api-requests)
- [ClawHub publisher profile](https://clawhub.ai/user/mailtrap)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline code, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses environment variable placeholders for secrets and account identifiers.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
