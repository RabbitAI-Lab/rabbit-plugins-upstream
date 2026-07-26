## Description: <br>
Automates scanning configured mailboxes for invoice emails, parsing PDF, OFD, or XML invoices, and forwarding standardized invoice summaries and attachments to designated finance or admin recipients. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Employees, finance teams, administrators, and developers use this skill to configure mailbox invoice forwarding workflows, preview candidate invoices, and run or schedule forwarding after recipient and rule review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill needs sensitive mailbox read and send access for invoice forwarding. <br>
Mitigation: Install it only for mailboxes approved for this workflow, prefer interactive secret entry or environment/secret-manager injection, and keep authorization codes out of shared chat, logs, and configuration files. <br>
Risk: Incorrect forwarding rules or recipients could send invoice data to the wrong destination. <br>
Mitigation: Review recipients and run a dry-run scan before enabling run mode or scheduled execution. <br>
Risk: Downloading invoice links can broaden the set of external URLs contacted during scans. <br>
Mitigation: Set trusted link_domains for expected invoice providers and rely on the skill's invoice-format gate before forwarding downloaded content. <br>
Risk: Dependency installation can modify the active Python environment. <br>
Mitigation: Use check --install-deps only in environments where pip changes are acceptable, or install optional PDF dependencies manually in a controlled environment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/songhonglei/skills/invoice-auto-forward) <br>
- [Skill Instructions](SKILL.md) <br>
- [Configuration Example](references/config.example.json) <br>
- [Troubleshooting Guide](references/troubleshooting.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce mailbox scan previews, setup/check/run command output summaries, and configuration guidance for local secret and schedule files.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
