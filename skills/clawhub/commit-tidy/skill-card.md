## Description: <br>
Analyze staged and committed Git changes and recommend split, squash, staging, security-scan, or commit-message strategy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to inspect Git changes, decide whether to split or squash commits, draft reviewable commit messages, and apply commit hygiene checks before publishing repository history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled commit review trigger can prompt a separate review agent after commits for the current repository path and commit SHA. <br>
Mitigation: Do not register the bundled post-commit hook unless that behavior is desired; inspect the hook and scope it to repositories where automated commit review prompts are acceptable. <br>
Risk: The skill can recommend history-rewriting workflows such as amend, rebase, soft reset, and force-push preparation. <br>
Mitigation: Review the proposed Git commands before execution, confirm the target branch and commit range, and follow local CI or force-push approval rules. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/commit-tidy) <br>
- [Publisher Profile](https://clawhub.ai/user/drumrobot) <br>
- [CHANGELOG.md](artifact/CHANGELOG.md) <br>
- [Hunk Split](artifact/hunk-split.md) <br>
- [Interactive Amend](artifact/interactive-amend.md) <br>
- [Message Discipline](artifact/message-discipline.md) <br>
- [Security Scan](artifact/security-scan.md) <br>
- [Soft Reset Amend](artifact/soft-reset-amend.md) <br>
- [Staging Discipline](artifact/staging-discipline.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and commit message drafts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Git commands, staged-file groupings, split or squash recommendations, and commit subject/body drafts.] <br>

## Skill Version(s): <br>
0.5.0 (source: server release metadata and changelog, released 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
