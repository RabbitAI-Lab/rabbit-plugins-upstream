## Description: <br>
Comprehensive security auditing for Clawdbot deployments. Scans for exposed credentials, open ports, weak configs, and vulnerabilities. Auto-fix mode included. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chandrasekar-r](https://clawhub.ai/user/chandrasekar-r) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to audit Clawdbot deployments before release or on a recurring schedule, checking credentials, exposed ports, configuration security, file permissions, Docker settings, Git exposure, and recent commit messages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audit reports can reveal local file paths and security posture. <br>
Mitigation: Treat reports as sensitive and share them only with trusted reviewers or systems. <br>
Risk: The optional --fix mode can change permissions on .env, JSON, key, and PEM files under /root/clawd and create a .gitignore file. <br>
Mitigation: Run the report-only audit first and use --fix only after reviewing expected backups, permissions, and service behavior. <br>


## Reference(s): <br>
- [Security Audit on ClawHub](https://clawhub.ai/chandrasekar-r/skills/security-audit) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Console audit report or JSON report with command-line usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Report-only by default; the optional --fix mode can change local file permissions and create a .gitignore file.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
