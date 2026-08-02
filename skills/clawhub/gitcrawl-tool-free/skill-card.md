## Description: <br>
A lightweight repository issue and pull request archive search skill that helps agents query local GitHub archive data, check archive freshness, search by keyword, and inspect neighboring issue context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, open source contributors, and technical researchers use this skill to search cached GitHub issue and PR archives, inspect PR status, and review nearby discussion context for a single repository. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run gitcrawl and GitHub CLI commands that contact GitHub for live or sync operations. <br>
Mitigation: Run it only for repositories the user intends to query and review proposed commands before execution. <br>
Risk: GitHub tokens may be used for live queries or synchronization. <br>
Mitigation: Use least-privilege GitHub credentials and avoid exposing tokens in prompts, logs, or command output. <br>
Risk: Repository archive data is stored locally and may contain sensitive issue or pull request content. <br>
Mitigation: Periodically review or remove the local ~/.gitcrawl/archive cache when repository data is sensitive. <br>
Risk: Cached archive results may be stale. <br>
Mitigation: Check archive freshness before relying on results and verify live GitHub state before closing, merging, or making project decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/gitcrawl-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce GitHub issue or PR metadata, status summaries, local cache guidance, and command output interpretation.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
