## Description:

Use this skill for OKX Outcomes YES/NO event-contract markets via the okx-outcomes binary, including market discovery, account views, order workflows, CTF actions, setup, authentication, and wallet binding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to operate OKX Outcomes event markets from an agent, including browsing markets, checking balances and positions, preparing trades, and completing setup or authentication flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide financial trading actions that use local OAuth and signing-key access.

Mitigation: Require a dry-run preview, verify order details, and proceed with write actions only after the user gives the required confirmation.

Risk: The release includes an unverified raw curl-to-shell installer path for the outcomes binary.

Mitigation: Prefer the versioned npm package or a signed, versioned release with checksum verification before installing the CLI.

Risk: A signing private key could be exposed if entered into chat or passed directly to commands.

Mitigation: Do not accept private keys in chat; use the setup and keyring flow, and tell the user to revoke or rotate any pasted key.

## Reference(s):

- [OKX](https://www.okx.com)
- [OKX Outcomes CLI Releases](https://github.com/okx/outcomes-cli/releases)
- [OKX Outcomes CLI Reference](https://github.com/okx/outcomes-cli/blob/main/docs/cli-reference.md)
- [Setup & Authentication](references/setup-auth.md)
- [Data / Search Commands](references/data-commands.md)
- [Account Commands](references/account-commands.md)
- [CLOB Commands](references/clob-commands.md)
- [CTF Commands](references/ctf-commands.md)
- [Cross-Command Workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run trade previews, setup prompts, and explicit user confirmation gates for write actions.]

## Skill Version(s):

1.4.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
