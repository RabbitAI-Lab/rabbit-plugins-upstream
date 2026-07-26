## Description: <br>
Reviews code changes against Android, iOS, and general engineering rules, including local diffs, commits, branch comparisons, and remote pull request URLs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[timeaground](https://clawhub.ai/user/timeaground) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to review proposed code changes before merge, with platform-aware findings, severity ratings, and concrete fix suggestions. It is especially suited for Android, iOS, general software, security-focused, and agent-skill review workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads repository diffs and nearby code context, which may include sensitive implementation details. <br>
Mitigation: Install and run it only in repositories where assistant access to the targeted diff and surrounding code is acceptable. <br>
Risk: Optional HTML report generation writes files under .code-reviews/, may update .gitignore, and can open a browser. <br>
Mitigation: Request report generation only after reviewing and accepting those local side effects. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/timeaground/skills/pro-code-reviewer) <br>
- [README](artifact/README.md) <br>
- [General review rules](artifact/references/review-general.md) <br>
- [Android review rules](artifact/references/review-android.md) <br>
- [iOS review rules](artifact/references/review-ios.md) <br>
- [Agent skill security review rules](artifact/references/review-skill-vetter.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown review findings with optional standalone HTML report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings are grouped by P0, P1, and P2 severity; optional reports are written under .code-reviews/.] <br>

## Skill Version(s): <br>
1.2.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
