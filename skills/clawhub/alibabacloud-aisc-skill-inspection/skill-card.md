## Description: <br>
Submits Alibaba Cloud AISC Skill file security scans, polls task status, diagnoses API or upload failures, and interprets findings for malicious code, prompt injection, hardcoded credentials, sensitive data, and risky configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sdk-team](https://clawhub.ai/user/sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security reviewers use this skill to submit Skill package URLs to Alibaba Cloud AISC, poll scan tasks, and interpret security reports before choosing or deploying a Skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Alibaba Cloud credentials with aisc:CreateSkillFileCheck and aisc:ListSubTasks permissions. <br>
Mitigation: Configure credentials outside the conversation, grant only the required AISC permissions, and do not paste or log credential values. <br>
Risk: Skill download URLs are sent to Alibaba Cloud AISC and scan reports may be written locally. <br>
Mitigation: Submit only URLs intended for AISC scanning, preserve signed URLs exactly, and review local reports before sharing. <br>
Risk: The security evidence notes deterministic mock/evaluation outputs for certain inputs, so those responses are not proof of a live scan. <br>
Mitigation: Treat mock/evaluation cases as test behavior and rely on completed live AISC reports for real security decisions. <br>
Risk: Dependencies are version-ranged rather than pinned. <br>
Mitigation: Use a reviewed environment or lockfile for production use. <br>


## Reference(s): <br>
- [RAM Permissions](references/ram-policies.md) <br>
- [Result Interpretation Guide](references/result-interpretation-guide.md) <br>
- [Verification Methods](references/verification-method.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-aisc-skill-inspection) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with shell commands and JSON report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write ./check-report.json when scan commands use --output.] <br>

## Skill Version(s): <br>
0.0.1 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
