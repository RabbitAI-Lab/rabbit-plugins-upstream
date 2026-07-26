## Description: <br>
Technical GDPR compliance audit for data mapping, encryption verification, access control review, data retention analysis, DPIA templates, and cross-border transfer assessment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[1beekeeper](https://clawhub.ai/user/1beekeeper) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security engineers, and compliance teams use this skill to run technical GDPR checks across infrastructure and applications, then produce findings, scorecards, DPIA material, and remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad system scans can reveal PII locations, credential file paths, access-control details, and security weaknesses. <br>
Mitigation: Limit scans to approved systems and directories, protect generated reports with restrictive permissions, and treat audit outputs as confidential. <br>
Risk: Privileged checks can expose sensitive account, firewall, database, and host configuration details. <br>
Mitigation: Run privileged phases only when authorized and necessary, and use the least privilege needed for each audit phase. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/1beekeeper/skills/gdpr-security-auditor) <br>
- [ARGUS homepage](https://github.com/nousresearch/argus) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command blocks, JSON scorecard snippets, and report templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates audit findings, scorecard JSON, DPIA Markdown, and report guidance for authorized GDPR security reviews.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
