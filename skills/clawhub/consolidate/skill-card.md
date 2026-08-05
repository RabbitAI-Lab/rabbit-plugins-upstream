## Description: <br>
Consolidate and respond to external PR and issue feedback by gathering AI reviews, classifying findings, posting review summaries and formal reviews, and tracking deferred items. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and maintainers use this skill to consolidate CodeRabbit, GitHub Copilot, human, and internal review feedback on pull requests or issues, decide which findings to fix or reject, publish review artifacts, and register deferred follow-up work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically publish formal reviews and review summaries to GitHub. <br>
Mitigation: Use explicit interactive invocation for public or shared repositories so drafted review artifacts are approved before posting. <br>
Risk: The skill can edit PR metadata, create issue comments, and maintain deferred-review tracking. <br>
Mitigation: Review the PR body edit, issue creation, and deferred tracking behavior before use in repositories where these records are sensitive. <br>
Risk: The skill includes narrow staging-promotion push behavior for conflict fixes. <br>
Mitigation: Confirm the repository and branch state before allowing workflows that may push conflict-resolution changes. <br>


## Reference(s): <br>
- [Consolidate on ClawHub](https://clawhub.ai/drumrobot/skills/consolidate) <br>
- [README](README.md) <br>
- [SKILL.md](SKILL.md) <br>
- [CHANGELOG](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown review summaries, formal review text, status updates, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce GitHub review comments, issue comments, PR metadata updates, deferred tracking entries, and local draft files when interactive review is used.] <br>

## Skill Version(s): <br>
0.5.0 (source: frontmatter, release evidence, CHANGELOG released 2026-08-03) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
