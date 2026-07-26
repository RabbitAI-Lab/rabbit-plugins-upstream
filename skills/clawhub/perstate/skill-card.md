## Description: <br>
Perstate provides a git-native remote knowledge graph that lets agents and individuals save, recall, branch, inspect, and visualize persistent state. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fanzhidongyzby](https://clawhub.ai/user/fanzhidongyzby) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agent operators, and individuals use Perstate to maintain persistent memory as a git-backed markdown knowledge graph. It supports saving conversation-derived insights, searching and traversing stored knowledge, branching memory states, viewing graph structure, and pruning stale local state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist conversation-derived knowledge locally and to a git repository using the user's git credentials. <br>
Mitigation: Use a dedicated private repository, avoid saving secrets or regulated data, prefer explicit /perstate commands over automatic save behavior, and review generated changes before commit or push when possible. <br>
Risk: The graph viewer can contact third-party CDNs when opened. <br>
Mitigation: Open the viewer only in environments where those external network requests are acceptable, or review and adapt the generated HTML before use. <br>


## Reference(s): <br>
- [ClawHub Perstate listing](https://clawhub.ai/fanzhidongyzby/skills/perstate) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with shell command output and markdown/YAML knowledge graph files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local configuration, git worktrees, markdown entity and relation files, commits, pushes, and an optional HTML graph view.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
