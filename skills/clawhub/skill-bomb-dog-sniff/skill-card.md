## Description: <br>
Scans OpenClaw skill directories for malicious patterns and can quarantine, audit, batch scan, or safely install skills based on risk scoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lvcidpsyche](https://clawhub.ai/user/lvcidpsyche) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and security reviewers use this skill to statically scan OpenClaw skills before installation, audit installed skills, and run batch or safe-install workflows that block risky releases by threshold. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is flagged suspicious because it ships runnable malware-like test fixtures. <br>
Mitigation: Review the fixtures before installation and prefer converting them into inert text fixtures or removing them for normal use. <br>
Risk: The safe-install workflow downloads code and can modify existing installed skills. <br>
Mitigation: Run safe-install in an isolated environment or dry-run mode first, then review scan output before allowing installation or overwrite. <br>
Risk: Static, pattern-based scanning may miss runtime-only behavior or novel attacks. <br>
Mitigation: Use the skill as a first-pass screening tool and combine it with manual review and other security checks for high-risk skills. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/lvcidpsyche/skills/skill-bomb-dog-sniff) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Console text or JSON scan reports with risk scores, findings, recommendations, and exit codes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Static analysis only; safe-install may download code and modify installed skill files when installation is allowed.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact declares 1.2.0 in SKILL.md and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
