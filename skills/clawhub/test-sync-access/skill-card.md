## Description: <br>
GitCode AI Review Bot listens to PR events, checks compliance, auto-fixes titles, comments on issues, and syncs merged PRs with email notifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[changhui123456](https://clawhub.ai/user/changhui123456) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and repository maintainers use this skill to operate a GitCode pull request review bot that checks PR titles, descriptions, reviewers, code style, security patterns, branch names, and change size before commenting, editing titles, or syncing merged changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic repository changes and branch synchronization can affect protected branches or repository history if permissions are too broad. <br>
Mitigation: Deploy with a narrowly scoped GitCode token, explicit branch allowlists, and approval controls for branch sync operations. <br>
Risk: Automatic PR title edits, comments, and email notifications can create misleading or unwanted repository activity. <br>
Mitigation: Document controls for disabling or approving automatic title edits, comments, sync behavior, and notifications before use. <br>
Risk: Admin endpoints for skill reloads, manual triggers, and configuration visibility can expose high-impact controls. <br>
Mitigation: Protect admin endpoints, keep audit logs visible, and review access before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/changhui123456/skills/test-sync-access) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/changhui123456) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose repository actions such as PR title edits, comments, branch synchronization, and email notifications.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
