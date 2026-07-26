## Description: <br>
Comprehensive Gandi domain registrar integration for domain and DNS management, including domain listing, availability checks, DNS record changes, email forwarding, SSL status checks, DNS snapshots, bulk zone updates, and domain expiration monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrisagiddings](https://clawhub.ai/user/chrisagiddings) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and domain administrators use this skill to inspect and manage Gandi domains, DNS records, email forwarding, SSL status, snapshots, and selected registrar workflows from an agent-assisted environment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write-capable Gandi tokens can modify registrar, DNS, and email-forwarding resources. <br>
Mitigation: Use separate read-only and write tokens, grant only the scopes required for the task, and rotate or delete unused tokens. <br>
Risk: DNS and email commands can break websites, mail delivery, or routing when incorrect values are applied. <br>
Mitigation: Review commands before execution, test on non-production domains when possible, and avoid --force unless the change has already been verified. <br>
Risk: Bulk DNS and snapshot restore workflows can replace complete DNS zones. <br>
Mitigation: Create DNS snapshots before changes and verify the target domain, snapshot, and input records before running bulk or restore operations. <br>
Risk: Credentials may be exposed if copied into shell profiles, logs, or shared files. <br>
Mitigation: Prefer secret-management workflows or a 0600 token file, and do not print, commit, or share Personal Access Tokens. <br>


## Reference(s): <br>
- [Gandi Skill Page](https://clawhub.ai/chrisagiddings/skills/gandi-skill) <br>
- [Setup Guide](references/setup.md) <br>
- [Authentication](references/authentication.md) <br>
- [Gandi API Overview](references/api-overview.md) <br>
- [Domain Management API](references/domains.md) <br>
- [LiveDNS Management API](references/livedns.md) <br>
- [Scripts Reference](SCRIPTS.md) <br>
- [Gandi Personal Access Tokens](https://admin.gandi.net/organizations/account/pat) <br>
- [Gandi API](https://api.gandi.net) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide execution of Node.js scripts that call Gandi APIs and read credentials from GANDI_API_TOKEN or ~/.config/gandi/api_token.] <br>

## Skill Version(s): <br>
0.2.7 (source: server release, openclaw metadata, and changelog, released 2026-02-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
