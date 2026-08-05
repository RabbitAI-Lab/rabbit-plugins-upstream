## Description: <br>
GitHub issue and pull request workflow automation for agents, covering issue creation, PR bodies, reviews, dependency tracking, CI and merge gates, account handling, push guards, and public-repository sanitization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering agents use this skill to turn plans, research, and implementation work into GitHub issues, pull requests, reviews, comments, dependency links, and guarded merge or publish flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead an agent to create or edit GitHub issues and pull requests, post comments or reviews, push branches, request reviewers, and merge changes. <br>
Mitigation: Install it only for repositories where the agent should have GitHub write authority, and review proposed issue, PR, review, push, and merge actions before allowing them to run. <br>
Risk: The workflow relies on broad GitHub permissions and account switching, which can cause actions to run under the wrong identity or with more access than intended. <br>
Mitigation: Use scoped GitHub accounts, verify the active account and required scopes before write operations, and prefer command-scoped token use for account-specific commands. <br>
Risk: Public repository content can accidentally include personal data, internal paths, or sensitive operational details. <br>
Mitigation: Run the skill's public-repository sanitization checks before publishing issue bodies, PR bodies, comments, or review text. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/github-flow) <br>
- [Skill overview](artifact/SKILL.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>
- [Authentication and scope guidance](artifact/auth-scope.md) <br>
- [PR workflow guidance](artifact/pr.md) <br>
- [Merge gates](artifact/merge.md) <br>
- [Push guards](artifact/push-guards.md) <br>
- [Public repository sanitization](artifact/sanitize.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, code snippets, and occasional JSON or API payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct an agent to operate GitHub issues, pull requests, reviews, branches, and merges through the GitHub CLI and local helper scripts.] <br>

## Skill Version(s): <br>
0.8.0 (source: server release metadata and CHANGELOG.md, released 2026-08-03) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
