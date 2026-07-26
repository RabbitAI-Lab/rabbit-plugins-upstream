## Description: <br>
Systematic approach to finding, evaluating, and tracking GitHub bounties and open source opportunities <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lrg913427-dot](https://clawhub.ai/user/lrg913427-dot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and open-source contributors use this skill to find GitHub bounty opportunities, evaluate value and competition, track pull request status, and prepare bounty reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct actions through the user's GitHub account, including forks, commits, pull requests, comments, or local tracking notes. <br>
Mitigation: Keep bounty discovery read-only by default and require explicit confirmation before any fork, commit, pull request, comment, or local note write. <br>
Risk: The skill includes sensitive credential and mailbox workflows. <br>
Mitigation: Do not allow the agent to read local credential files, store tokens in /tmp, use a Gmail app password, delete mail, or otherwise handle credentials unless the user explicitly authorizes the exact action. <br>
Risk: The skill may lead to public posting of operational context or generated content. <br>
Mitigation: Review proposed PR bodies, comments, and reports before publication, and do not post session, system, or private context publicly. <br>
Risk: The artifact discusses workarounds for blocked security-tool patterns. <br>
Mitigation: Do not bypass security scanner blocks; use approved read-only command patterns and stop for review when a scanner blocks execution. <br>


## Reference(s): <br>
- [Bounty Hunting Examples](artifact/references/bounty-examples.md) <br>
- [Known Bounty Repos](artifact/references/known-bounty-repos.md) <br>
- [Confirmed Fake/Bot Bounty Repos](artifact/references/confirmed-fake-repos.md) <br>
- [Latest Bounty Scan Results](artifact/references/latest-bounty-scan-june-2026.md) <br>
- [Recent Bounty Examples](artifact/references/recent-bounty-examples.md) <br>
- [Dependency Issue Patterns](artifact/references/dependency-issue-patterns.md) <br>
- [PR Tracking and Follow-up Workflow](artifact/references/pr-tracking-workflow.md) <br>
- [CI Lint/Format Failure Fix Pattern](artifact/references/ci-lint-fix-pattern.md) <br>
- [Gmail IMAP PR Email Management](artifact/references/gmail-pr-email-management.md) <br>
- [Bounty Report Template](artifact/templates/bounty-report.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command, JSON, and report-template examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide read-only bounty searches, competition analysis, PR tracking, and report or note drafting; account-write actions require explicit confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
