## Description: <br>
Huawei Cloud Skill Creator guides an agent through a six-phase pipeline for gathering requirements, researching Huawei Cloud CLI/SDK/API options, generating skill files, preparing tests, running verification, and performing cleanup and compliance checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to scaffold Huawei Cloud operational skills with documented requirements, verified CLI/SDK/API paths, IAM guidance, test artifacts, and compliance checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads Huawei Cloud credentials and can run live cloud tests. <br>
Mitigation: Use an isolated development environment, a non-production Huawei Cloud account, least-privilege credentials, and budget or quota guards. <br>
Risk: Generated test files may contain command strings that an agent executes. <br>
Mitigation: Inspect templates/test-vars.json and require dry-run or per-command confirmation before live create, update, or delete tests. <br>
Risk: Credential handling can expose AK/SK secrets if users paste them into chat or scripts. <br>
Mitigation: Use explicit environment variables or profiles, avoid pasting secrets into chat, and keep hardcoded credentials out of generated documents and scripts. <br>
Risk: Broad IAM or billing permissions could expand the impact of mistaken commands. <br>
Mitigation: Remove unrelated IAM and billing permissions and use the least-privilege policies documented for the generated skill. <br>
Risk: The security evidence marks the release as suspicious due to live cloud execution and credential access. <br>
Mitigation: Review before installing, avoid --insecure, and run the provided security audit guidance before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-skill-creator) <br>
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html) <br>
- [Huawei Cloud SDK Center](https://console.huaweicloud.com/apiexplorer/#/sdkcenter) <br>
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [API Paths](references/api-paths.md) <br>
- [BSS SDK Notes](references/bss-sdk-notes.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [Dataflow Diagram](references/dataflow-diagram.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Related Commands](references/related-commands.md) <br>
- [Security Audit Guide](references/security-audit-guide.md) <br>
- [Test Report](references/test-report.md) <br>
- [Verification Method](references/verification-method.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code blocks, shell commands, and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a complete skill directory structure with SKILL.md, references, scripts, and templates for agent use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter says 2.1.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
