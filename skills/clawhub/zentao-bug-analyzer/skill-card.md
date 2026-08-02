## Description: <br>
Analyzes Zentao bug reports by parsing bug links, classifying modules, locating branches and commits, reviewing attachments, logs, comments, and local code, then producing reports and optional Zentao comments and Feishu notifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yeah526](https://clawhub.ai/user/yeah526) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and QA engineers use this skill to triage Zentao defects, correlate bug evidence with logs and local source history, and prepare a root-cause report. It can publish that report back to Zentao and notify the assigned user through Feishu when configured. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores Zentao credentials locally and uses them to open an authenticated browser session. <br>
Mitigation: Use a least-privilege Zentao account, keep the configuration file out of source control and backups, and clean up browser sessions after each run. <br>
Risk: The skill can access private bug attachments, logs, and local code repositories during analysis. <br>
Mitigation: Run it only in approved repositories or isolated worktrees and restrict input bug data to cases the operator is authorized to inspect. <br>
Risk: The workflow may publish comments to live Zentao bugs by default. <br>
Mitigation: Set auto_comment to false unless automatic posting is explicitly intended, and review generated reports before enabling live posting. <br>
Risk: The workflow may run git checkout, submodule update, and worktree cleanup commands in local repositories. <br>
Mitigation: Use dedicated worktrees or disposable workspaces for analysis so checkout and cleanup operations do not disrupt unrelated work. <br>


## Reference(s): <br>
- [Zentao API Reference](references/zentao-api-reference.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/yeah526/skills/zentao-bug-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, HTML bug comments, Feishu notification text, local files, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create per-bug report, comment, attachment, frame, and time-metadata files under a local bugs directory.] <br>

## Skill Version(s): <br>
1.1.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
