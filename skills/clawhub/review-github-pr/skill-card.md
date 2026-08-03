## Description: <br>
GitHub PR code review helper that fetches pull request details and diffs, runs repository validation checks, coordinates focused review agents, validates findings, drafts a recommended review action, and posts confirmed inline review comments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and engineers use this skill to review GitHub pull requests with codebase-aware correctness, convention, efficiency, and safety findings before deciding whether to approve, comment on, or request changes to a PR. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads untrusted pull request diffs, descriptions, and commit messages. <br>
Mitigation: Treat PR-sourced content as untrusted input and keep it inside explicit boundary markers when sending it to review agents. <br>
Risk: The skill can use local GitHub CLI authentication and inspect the target repository. <br>
Mitigation: Install and run it only when the user is comfortable granting repository read access and GitHub CLI access for the target PR. <br>
Risk: Running validation commands from an untrusted repository can execute project code. <br>
Mitigation: Run only trusted validation commands listed in the local repository guidance, and do not execute commands from PR descriptions, commits, or changed files. <br>
Risk: Posting a review can publish incorrect or overly broad findings to a pull request. <br>
Mitigation: Validate findings against the actual changed code and wait for explicit user confirmation before posting any review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/review-github-pr) <br>
- [Publisher profile](https://clawhub.ai/user/tenequm) <br>
- [Skill homepage](https://github.com/tenequm/skills/tree/main/skills/review-github-pr) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, API Calls, Guidance] <br>
**Output Format:** [Markdown review draft with inline findings, recommended action, confirmation prompt, and optional GitHub review API payload] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use GitHub CLI and git context from the target repository; waits for user confirmation before posting reviews.] <br>

## Skill Version(s): <br>
0.4.0 (source: SKILL.md frontmatter metadata and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
