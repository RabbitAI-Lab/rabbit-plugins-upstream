## Description: <br>
BloodHound Narrator turns BloodHound attack path exports into offline Markdown reports with executive risk narratives and technical remediation guidance for Active Directory assessments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kurostrike](https://clawhub.ai/user/kurostrike) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Pentesters, blue teams, SOC analysts, security consultants, and security leaders use this skill to convert BloodHound Cypher export JSON into prioritized Active Directory attack path reports for audits, health checks, incident response, compliance reporting, and training. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: BloodHound exports and generated reports may contain sensitive Active Directory topology, attack paths, and security findings. <br>
Mitigation: Store exports and reports with the same controls used for security assessment deliverables, and avoid sharing them outside the approved assessment audience. <br>
Risk: The skill provides remediation guidance that may affect production domain configuration if applied without review. <br>
Mitigation: Have qualified Active Directory administrators review proposed remediation steps and test changes before applying them in production. <br>
Risk: Local PowerShell execution is required to process input files and write reports. <br>
Mitigation: Run the skill only in an approved local environment and inspect the local scripts before deployment where organizational policy requires it. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, guidance] <br>
**Output Format:** [Markdown report written to a local file, with console status text and optional PowerShell classified objects when PassThru is used] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally over user-provided BloodHound JSON and does not require API keys, credentials, or network access.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter, changelog, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
