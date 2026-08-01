## Description: <br>
Reviews pull requests with scope validation, requirements compliance, and line comments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to review GitHub or GitLab pull and merge requests against the stated scope, validate version and hygiene requirements, classify findings, and generate review reports or comments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may interact with GitHub or GitLab to post PR comments, submit review summaries, or create backlog issues. <br>
Mitigation: Review platform commands before execution, use least-privilege tokens, and require confirmation before posting comments or creating issues. <br>
Risk: The skill includes under-disclosed external posting of PR-scoped insights to GitHub Discussions. <br>
Mitigation: Disable or remove the Discussions insight module unless publishing review findings outside the PR is explicitly intended. <br>
Risk: The skill can retain selected review findings through knowledge capture. <br>
Mitigation: Use no-capture or confirmation-required mode for sensitive repositories and review captured content before storage. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-pr-review) <br>
- [Publisher profile](https://clawhub.ai/user/athola) <br>
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown review reports, inline review comments, issue text, and command guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose platform API commands for PR comments, backlog issues, and review summaries.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
