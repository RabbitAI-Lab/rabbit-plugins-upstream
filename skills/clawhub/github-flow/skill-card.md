## Description: <br>
Github Flow guides agents through GitHub issue, pull request, review, merge, dependency, authentication, and publication workflows using GitHub CLI-first procedures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering agents use this skill to convert plans into GitHub issues and PRs, manage review and merge flows, enforce public-repository hygiene, and handle GitHub CLI authentication and scope checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents through high-impact GitHub actions, including token refreshes, public posting, force-pushes, direct branch pushes, and merges. <br>
Mitigation: Install only where agent-managed GitHub workflows are intended, and require explicit user confirmation before token refreshes, public posts, force-pushes, direct master pushes, or merges. <br>
Risk: Hardcoded account mappings and scope rules can cause work to run under the wrong GitHub identity or with broader access than expected. <br>
Mitigation: Replace the documented accounts and scope rules with the user's own policy, then verify gh CLI identity, repository owner, and token scope before live operations. <br>
Risk: Home-directory and cache assumptions can affect how credentials or local workflow state are reused between agent runs. <br>
Mitigation: Review local credential storage, cache dependencies, and gh CLI state before enabling the skill in shared or sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/github-flow) <br>
- [Publisher profile](https://clawhub.ai/user/drumrobot) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and GitHub CLI/API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local GitHub repository context and configured gh CLI credentials for live GitHub operations.] <br>

## Skill Version(s): <br>
0.7.0 (source: server release metadata and CHANGELOG, released 2026-07-23) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
