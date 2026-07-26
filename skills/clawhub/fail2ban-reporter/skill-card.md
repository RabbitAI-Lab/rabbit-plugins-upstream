## Description: <br>
Auto-report fail2ban banned IPs to AbuseIPDB, check IP reputation, and provide fail2ban reporting stats for server security monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jestersimpps](https://clawhub.ai/user/jestersimpps) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
System administrators and developers use this skill to report fail2ban-banned IP addresses to AbuseIPDB, check suspicious IP reputation, and enable or remove automatic fail2ban reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Auto-reporting can leave root-run fail2ban executing a script from a user-writable skill directory. <br>
Mitigation: Install the reporting script into a root-owned, non-writable path before enabling the fail2ban action. <br>
Risk: The skill sends banned IP addresses and abuse comments to AbuseIPDB, a third-party service. <br>
Mitigation: Confirm that the operating environment permits sharing this security telemetry before enabling reporting. <br>
Risk: The security verdict is suspicious and requires review before installation. <br>
Mitigation: Review the scripts and configuration changes carefully before running install.sh or enabling auto-reporting. <br>


## Reference(s): <br>
- [AbuseIPDB API Reference](references/abuseipdb-api.md) <br>
- [AbuseIPDB API Key](https://www.abuseipdb.com/account/api) <br>
- [AbuseIPDB API](https://api.abuseipdb.com/api/v2) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown with inline shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires fail2ban, curl, jq, and an AbuseIPDB API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
