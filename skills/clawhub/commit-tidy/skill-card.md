## Description: <br>
Analyze staged and committed Git changes and recommend split, squash, amend, staging, secret-scan, and commit-message strategies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering agents use this skill to keep Git commit history atomic, reviewable, and aligned with repository-specific commit rules. It helps plan split or squash strategies, draft structured commit messages, audit staged files, and apply safer history-rewrite workflows when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: History-rewrite or force-push guidance can disrupt shared or protected branches if applied without coordination. <br>
Mitigation: Use rewrite steps only on branches you own or after coordinating with collaborators, verify CI state, and prefer force-with-lease when a force push is required. <br>
Risk: Optional hook installation changes local commit behavior. <br>
Mitigation: Review any hook before enabling it and install it only when the pre-commit blocking behavior matches the repository workflow. <br>


## Reference(s): <br>
- [Commit Tidy on ClawHub](https://clawhub.ai/drumrobot/skills/commit-tidy) <br>
- [interactive-amend.md](artifact/interactive-amend.md) <br>
- [message-discipline.md](artifact/message-discipline.md) <br>
- [security-scan.md](artifact/security-scan.md) <br>
- [soft-reset-amend.md](artifact/soft-reset-amend.md) <br>
- [staging-discipline.md](artifact/staging-discipline.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and commit-message drafts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include split or squash recommendations, staged-file audits, rewrite procedures, and pre-commit security checks.] <br>

## Skill Version(s): <br>
0.4.3 (source: server release metadata and changelog, released 2026-07-16) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
