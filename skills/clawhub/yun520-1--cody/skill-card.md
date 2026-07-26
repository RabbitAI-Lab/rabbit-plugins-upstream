## Description: <br>
Cody reviews Git diffs, pasted code, files, and GitHub or GitLab pull requests, then produces structured Chinese review reports covering bugs, security, performance, readability, type safety, error handling, and tests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yun520-1](https://clawhub.ai/user/yun520-1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use Cody to inspect code changes, pasted snippets, or PR/MR diffs and receive actionable Chinese code-review findings. It is suited for local review workflows and PR checks across Python, JavaScript/TypeScript, Java, Go, and Rust. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read local repository diffs, which may contain proprietary source code or secrets. <br>
Mitigation: Use it only in repositories where code-review disclosure is acceptable, and inspect diffs for sensitive material before sharing or storing generated reports. <br>
Risk: The PR/MR helper can use GitHub or GitLab tokens to fetch remote diffs, including GitLab URLs on arbitrary hosts. <br>
Mitigation: Run PR/MR fetching only for trusted repositories and hosts, and avoid exposing GITHUB_TOKEN or GITLAB_TOKEN unless token use is intended for that review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yun520-1/skills/cody) <br>
- [Publisher profile](https://clawhub.ai/user/yun520-1) <br>
- [Review dimensions](references/review-dimensions.md) <br>
- [Severity guide](references/severity-guide.md) <br>
- [Report template](references/report-template.md) <br>
- [Python review rules](references/languages/python.md) <br>
- [JavaScript and TypeScript review rules](references/languages/javascript.md) <br>
- [Java review rules](references/languages/java.md) <br>
- [Go review rules](references/languages/go.md) <br>
- [Rust review rules](references/languages/rust.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, html, shell commands, guidance] <br>
**Output Format:** [Chinese Markdown by default, with optional JSON or HTML reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include severity modes, review categories, actionable recommendations, and line references when available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
