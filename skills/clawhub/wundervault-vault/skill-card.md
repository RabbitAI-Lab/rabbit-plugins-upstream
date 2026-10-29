## Description:

Use the owner's API keys, SSH keys, wallets and signing keys without ever holding them. A Wundervault broker on this computer makes web calls, SSH commands, x402 payments and signatures for you and returns the result with the secret removed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snoweman](https://clawhub.ai/user/snoweman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can use an owner's approved API credentials, SSH access, wallets, and signing keys through the local Wundervault broker for web requests, server operations, x402 payments, and signatures, while the broker withholds secret values.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized broker operations can still change systems or spend funds.

Mitigation: Grant only the credentials and permissions needed, require owner approval for sensitive access, and set payment limits.

Risk: Agents running under the same operating-system account may be able to read one another's broker token files.

Mitigation: Run agents with different trust levels under separate operating-system accounts or on separate computers.

Risk: Installing the broker requires administrator privileges.

Mitigation: Verify the version 2 package and inspect the installer before running administrator commands.

## Reference(s):

- [Wundervault Vault release on ClawHub](https://clawhub.ai/snoweman/skills/wundervault-vault)
- [Wundervault MCP tool reference](https://wundervault.com/mcp)
- [Wundervault installation and upgrade guide](https://wundervault.com/install)
- [Wundervault limitations](https://wundervault.com/limitations)
- [Wundervault security verification information](https://wundervault.com/verify)

## Skill Output:

**Output Type(s):** [API responses, SSH operation results, Payment authorization headers, Digital signatures, Guidance]

**Output Format:** [Structured tool results and text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Secret values are withheld; results may include service responses, command output, payment headers, signatures, public keys, or algorithms.]

## Skill Version(s):

2.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
