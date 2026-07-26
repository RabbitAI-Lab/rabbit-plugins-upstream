## Description: <br>
Set up and use Bitwarden CLI (bw). Use when installing the CLI, authenticating (login/unlock), or reading secrets from your vault. Supports email/password, API key, and SSO authentication methods. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[startupbros](https://clawhub.ai/user/startupbros) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and other external users use this skill to install and operate the Bitwarden CLI for vault authentication, secret retrieval, synchronization, and account/session management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Vault session keys and exported secrets can be exposed through shared shells, logs, command history, or copied environment variables. <br>
Mitigation: Use the skill for specific vault tasks, avoid pasting or exporting long-lived secrets in shared shells, keep commands inside a dedicated session, and unset sensitive environment variables after use. <br>
Risk: Create or edit commands can modify the wrong vault item when names are ambiguous or item IDs are not verified. <br>
Mitigation: Verify item IDs before any create or edit command and prefer read-only commands unless a vault mutation is explicitly intended. <br>
Risk: An unlocked vault session can remain usable after the task is complete. <br>
Mitigation: Run bw lock or bw logout when finished with vault operations. <br>
Risk: Using an unofficial or unexpected CLI binary could expose vault credentials. <br>
Mitigation: Install only the official Bitwarden CLI using the documented npm, Homebrew, Chocolatey, Snap, or Bitwarden download sources. <br>


## Reference(s): <br>
- [Bitwarden CLI Documentation](https://bitwarden.com/help/cli/) <br>
- [Get Started Guide](references/get-started.md) <br>
- [CLI Examples](references/cli-examples.md) <br>
- [Bitwarden Downloads](https://bitwarden.com/download/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash, PowerShell, and JSON command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance for installing, authenticating, configuring, and using the bw CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
