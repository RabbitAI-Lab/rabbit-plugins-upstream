## Description: <br>
Provides local GDPR compliance checks, DPIA support, data-subject-rights review, cross-border-transfer review, and report generation for organizations assessing EU/EEA data-protection obligations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwumit](https://clawhub.ai/user/wwumit) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, compliance teams, and privacy operations staff use this skill to run local GDPR-oriented checks and generate draft compliance reports or templates. Outputs are compliance aids and should be reviewed by qualified legal or data-protection professionals before business reliance. <br>

### Deployment Geography for Use: <br>
European Union, European Economic Area, and United Kingdom <br>

## Known Risks and Mitigations: <br>
Risk: Generated reports may contain personal, confidential, or sensitive business information. <br>
Mitigation: Run the skill in a virtual environment, avoid entering unnecessary sensitive data, and review reports before sharing them. <br>
Risk: The skill provides compliance aids, not legal advice or regulatory approval. <br>
Mitigation: Use outputs as drafts for internal review and consult qualified legal or data-protection professionals for material GDPR decisions. <br>
Risk: The security-check script runs local helper commands. <br>
Mitigation: Review commands before execution and run checks in an isolated or virtual environment with appropriate permissions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wwumit/skills/gdpr-compliance) <br>
- [GDPR regulation reference](references/gdpr-regulation.md) <br>
- [Security check guide](SECURITY_CHECK_GUIDE.md) <br>
- [README](README.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance and local report files in JSON, Markdown, HTML, or CSV] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally; generated reports may contain business or compliance information and should be reviewed before sharing.] <br>

## Skill Version(s): <br>
1.1.0 (source: server evidence, package.json, changelog, and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
