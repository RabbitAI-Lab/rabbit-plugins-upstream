## Description: <br>
合并检查工具(免费版) helps developers evaluate whether a single GitHub pull request is likely to be merged by analyzing PR data, CI status, review state, and PR hygiene. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and open source contributors use this skill to inspect one pull request before or during review and produce merge-likelihood guidance with risks, strengths, and recommended next steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can query GitHub PR and repository information available through the user's gh CLI login, including private repository data when the user has access. <br>
Mitigation: Use it only with repositories and PRs the agent is allowed to inspect, and avoid running it from a gh session with broader access than needed. <br>
Risk: Generated reports may include private comments, reviews, branch details, or author history from GitHub. <br>
Mitigation: Review reports before sharing and remove repository-private or personally sensitive details. <br>
Risk: Merge-likelihood scoring is advisory and can be affected by repository norms, maintainer preferences, missing data, or API limits. <br>
Mitigation: Treat the score as a review aid, verify important findings against the PR, and rely on maintainer feedback for final decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/merge-check-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown report with JSON PR data and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Focused on one pull request per run; reports are advisory and depend on available GitHub data.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
