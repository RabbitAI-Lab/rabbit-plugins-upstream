## Description: <br>
Autonomous multi-client Linux server security management via SSH MCP, with nightly audits, CVE checks, guarded remediation, confirmation queues, and email reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cyber-bye](https://clawhub.ai/user/cyber-bye) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to run recurring Linux server security audits across client fleets, collect findings, and prepare guarded remediation actions. It is intended for environments where SSH MCP access, server profiles, reporting destinations, and approval workflows are configured before use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform recurring root-level SSH administration across multiple client servers. <br>
Mitigation: Install only where that access model is intended, configure least-privilege accounts where possible, and verify server profiles before enabling recurring audits. <br>
Risk: Automatic write actions and broad approval patterns can affect production systems. <br>
Mitigation: Disable automatic write actions until tested, restrict or remove bulk approval such as APPROVE ALL, and keep firewall, package, SSH, PAM, and service changes behind explicit confirmation. <br>
Risk: Package inventories, audit reports, backups, and email alerts may contain sensitive operational data. <br>
Mitigation: Review email recipients, decide whether package inventory may be sent to external CVE services, and set retention and access controls for generated reports and backups. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/cyber-bye/skills/linux-security-guardian) <br>
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) <br>
- [OSV.dev API documentation](https://google.github.io/osv.dev/) <br>
- [NVD API documentation](https://nvd.nist.gov/developers/start-here) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, finding files, pending-action records, audit logs, shell commands, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces per-client and per-server audit outputs; some remediation actions require explicit owner confirmation.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
