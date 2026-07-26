## Description: <br>
iOS HealthKit data sync CLI commands and patterns for working with the healthsync CLI, fetching Apple Health data, pairing iOS devices over a local network, and understanding mTLS certificate pinning, Keychain storage, and audit logging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mneves75](https://clawhub.ai/user/mneves75) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and engineers use this skill for guidance on syncing Apple HealthKit data from an iPhone to a Mac with the healthsync CLI. It helps agents provide pairing commands, data fetch examples, troubleshooting steps, and security architecture explanations for local-network HealthKit workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Health data, terminal output, JSON or CSV exports, clipboard QR payloads, and logs may contain private health information. <br>
Mitigation: Use the skill only with healthsync workflows you control, protect exported files and logs as private health information, and avoid sharing QR payloads or fetched data. <br>
Risk: Pairing or fetching over an untrusted local network could expose sensitive device or health-data workflows. <br>
Mitigation: Pair only trusted devices on trusted local networks and confirm certificate pinning behavior before fetching data. <br>
Risk: The skill documents an external CLI workflow but does not itself verify the installed healthsync CLI. <br>
Mitigation: Verify the external CLI and its source separately before using it with Apple Health data. <br>


## Reference(s): <br>
- [CLI Reference](references/CLI-REFERENCE.md) <br>
- [Security Patterns](references/SECURITY.md) <br>
- [Architecture](references/ARCHITECTURE.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include CSV or JSON output examples for HealthKit data fetches.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
