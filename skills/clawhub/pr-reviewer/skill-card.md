## Description: <br>
Automated GitHub PR code review with diff analysis, lint integration, structured reports, and checks for security issues, error handling gaps, test coverage, and code style problems across Go, Python, and JavaScript/TypeScript. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[briancolinger](https://clawhub.ai/user/briancolinger) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and maintainers use this skill to review GitHub pull requests, generate markdown review reports, optionally post findings as PR comments, and track review state. It is suited for repository workflows that need automated checks for security patterns, error handling, style, lint results, and test coverage signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crafted pull request filenames may influence local Python execution during review. <br>
Mitigation: Avoid running the skill on untrusted PRs until filename handling passes file lists through stdin, JSON, or arguments instead of embedding them in Python source. <br>
Risk: Overprivileged GitHub credentials can widen the impact of PR reading or comment posting. <br>
Mitigation: Use least-privilege GitHub credentials and review generated reports before posting them to pull requests. <br>
Risk: Review state and report outputs can be written to unintended locations if paths are configured carelessly. <br>
Mitigation: Keep PR_REVIEW_STATE and PR_REVIEW_OUTDIR inside the repository or a dedicated data directory. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/briancolinger/skills/pr-reviewer) <br>
- [Publisher profile](https://clawhub.ai/user/briancolinger) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown reports, JSON status summaries, terminal text, and optional GitHub PR comments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes review state to PR_REVIEW_STATE and markdown reports to PR_REVIEW_OUTDIR; uses gh, python3, and optional golangci-lint or ruff when available.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
