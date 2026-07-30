## Description: <br>
OpenClaw security hardening skill. Seven strategies from Zheng Tan & Lin 2026. Layers: audit, rule injection, guides. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiaozheng-jc](https://clawhub.ai/user/xiaozheng-jc) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use Aegis4All to audit OpenClaw configurations, add confirmation-focused security rules, and consult high-risk operation guides for safer OpenClaw use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect local OpenClaw configuration and skill files during audits. <br>
Mitigation: Install it only when you want a local OpenClaw hardening assistant, and review scan results before acting on recommendations. <br>
Risk: Rule injection can modify persistent agent guidance files after confirmation. <br>
Mitigation: Review the proposed target file and diff before confirming injection, update, or removal. <br>
Risk: Some guides include high-risk account migration, backup, or rollback steps. <br>
Mitigation: Follow manual-only guidance carefully, verify backup paths before deletion commands, and consider re-authenticating or rotating tokens after migration. <br>


## Reference(s): <br>
- [Understanding and mitigating the risks of OpenClaw for non-technical users](https://arxiv.org/abs/2606.11007) <br>
- [Aegis4All High-Risk Operation Guides](artifact/guides/security-guide.md) <br>
- [Aegis4All Behavior Rules](artifact/rules/inject.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, prioritized recommendations, inline shell commands, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only audit mode for security checks; rule injection modifies persistent guidance files only after user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
