## Description: <br>
Provides local CCPA/CPRA compliance checks, risk assessment, and document/report generation for organizations handling California consumer data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwumit](https://clawhub.ai/user/wwumit) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers, compliance teams, and privacy practitioners use this skill to run local CCPA/CPRA self-checks, consumer-rights and opt-out checks, risk assessments, and draft compliance reports for businesses serving California consumers. <br>

### Deployment Geography for Use: <br>
Global, for CCPA/CPRA compliance work involving California consumers. <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs local Python compliance scripts in the user's environment. <br>
Mitigation: Review the scripts before use, run them in a controlled workspace, and install only if local code execution is acceptable. <br>
Risk: Generated compliance reports could be mistaken for legal advice or formal compliance certification. <br>
Mitigation: Treat reports as internal guidance, verify current CCPA/CPRA requirements, and consult qualified counsel for material compliance decisions. <br>
Risk: Cross-jurisdiction commands reference a sibling compliance_core module outside this artifact. <br>
Mitigation: Review or trust the sibling compliance_core module before using cross-jurisdiction commands; use the standalone CCPA scripts when that module is unavailable. <br>


## Reference(s): <br>
- [CCPA/CPRA Law Summary](references/ccpa-law.md) <br>
- [Security Check Guide](SECURITY_CHECK_GUIDE.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/wwumit/skills/ccpa-compliance) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text guidance with optional JSON, Markdown, HTML, and CSV reports from local scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports are intended as internal compliance guidance and not legal advice.] <br>

## Skill Version(s): <br>
1.0.5 (source: package.json, README.md, evidence.release.version, target metadata; released 2026-07-05 in README.md and CHANGELOG.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
