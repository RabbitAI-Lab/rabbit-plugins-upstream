## Description: <br>
Control AdGuard Home DNS filtering via HTTP API. Use when managing blocklists/allowlists, checking domain filtering status, toggling protection, or clearing DNS cache. Supports blocking/allowing domains, viewing statistics, and protecting/disabling DNS filtering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rowbotik](https://clawhub.ai/user/rowbotik) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and self-hosting administrators use this skill to manage AdGuard Home DNS filtering from an agent-assisted command-line workflow. It supports checking domain filtering status, changing allowlist and blocklist rules, viewing DNS statistics, toggling protection, and clearing DNS cache. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses AdGuard Home admin credentials, which can control DNS filtering for the configured network. <br>
Mitigation: Set ADGUARD_URL explicitly to the intended AdGuard Home host, keep credentials out of shared shell startup files, and provide credentials only in trusted sessions. <br>
Risk: The default and example URLs use HTTP or local-network endpoints, which can expose admin traffic if used on an untrusted network. <br>
Mitigation: Prefer HTTPS, a trusted local tunnel, or another protected management path before sending admin credentials or session cookies. <br>
Risk: Commands such as allow, block, toggle, and cache-clear can immediately change network-wide DNS behavior. <br>
Mitigation: Require explicit user approval and review the target domain or action before running any command that changes filtering policy or protection state. <br>


## Reference(s): <br>
- [AdGuard Home API Reference](references/api.md) <br>
- [Official AdGuard Home API documentation](https://github.com/AdguardTeam/AdGuardHome/wiki/API) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and command output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-supplied AdGuard Home URL, admin username, and admin password before live API commands can run.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
