## Description: <br>
Scans agent skills with an automated scanner and a human review protocol to report risk levels and review guidance before installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security reviewers use this skill to scan agent skill directories or zip packages, interpret scanner exit codes, and prepare structured review reports before installing or approving skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scanned skill contents may be sent to skillscan.tokauth.com. <br>
Mitigation: Use the skill only for packages that may be shared with that service, or prefer a local-only and opt-in scanning workflow. <br>
Risk: Persistent device metadata may be stored and transmitted. <br>
Mitigation: Run the scanner only in environments where that metadata collection is acceptable, or require a version that avoids persistent identifiers and MAC collection. <br>
Risk: The scanner can update its own code from a remote manifest. <br>
Mitigation: Prefer signed or manually reviewed updates and disable unattended replacement before use in sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/skill-security-scan) <br>
- [Publisher profile](https://clawhub.ai/user/paudyyin) <br>
- [SkillScan remote scanning service](https://skillscan.tokauth.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown-style scanner reports, command output, exit codes, and risk recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scanner commands return exit codes 0-3 and may include risk levels, findings, and recommended installation actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
