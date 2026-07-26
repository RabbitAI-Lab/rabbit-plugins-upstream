## Description: <br>
仓库归档搜索 helps agents search GitHub issue and pull request archives with local cache checks, keyword queries, neighbor issue lookups, and optional GitHub CLI commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, open source contributors, and technical researchers use this skill to inspect repository issue and pull request history, check archive freshness, and verify PR or issue status before acting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may prompt an agent to run gitcrawl sync or live GitHub CLI queries that access the network and repository data. <br>
Mitigation: Confirm before running sync or live GitHub queries, and prefer cache-first searches when current data is not required. <br>
Risk: GitHub credentials can be exposed if tokens are pasted into prompts, commands, or logs. <br>
Mitigation: Use gh auth login or a scoped token provided through the environment, and avoid printing secrets. <br>
Risk: Local archive results can be stale. <br>
Mitigation: Check freshness with gitcrawl doctor and verify with live GitHub CLI output before acting on repository state. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/gitcrawl-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce gitcrawl and GitHub CLI commands, cache freshness checks, and JSON result interpretation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
