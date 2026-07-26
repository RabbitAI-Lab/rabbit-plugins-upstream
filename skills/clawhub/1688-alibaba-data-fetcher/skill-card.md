## Description: <br>
1688卖家工作台数据抓取：原生聊天用MEDIA、飞书必须用message；登录必须同回合内持续poll。 <br>

This skill is for research and development only. <br>

## Publisher: <br>
[howerlin0329](https://clawhub.ai/user/howerlin0329) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators and agents use this skill to collect authenticated 1688 seller workbench and business-advisor metrics, generate a daily operations report, and optionally push the report to Feishu. The workflow is intended for controlled technical use with the account owner's authorization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive 1688 seller analytics through broad browser-extension access. <br>
Mitigation: Install only for authorized accounts, narrow extension host permissions to required 1688 domains, and clear local extension and report data when no longer needed. <br>
Risk: Wildcard external extension connectivity can allow untrusted callers to request collected data. <br>
Mitigation: Restrict externally_connectable IDs to trusted callers before deployment. <br>
Risk: Feishu credentials and recurring outbound reporting can expose reports to unintended recipients. <br>
Mitigation: Keep Feishu secrets out of shared workspaces, verify the target chat ID, and disable or explicitly approve any scheduled reporting job. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/howerlin0329/skills/1688-alibaba-data-fetcher) <br>
- [Plugin Agent Guide](plugin/AGENT_GUIDE.md) <br>
- [Plugin README](plugin/README.md) <br>
- [Feishu Message Content Documentation](https://open.feishu.cn/document/server-docs/im-v1/message-content-description/create_json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, JSON data files, QR-code image files, Feishu post messages, and shell-command status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Report data is generated from plugin-collected 1688 data; model-authored content is limited to diagnostic and task-list sections.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
