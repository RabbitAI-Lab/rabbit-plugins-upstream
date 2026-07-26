## Description: <br>
Developer oversight and AI agent coaching for viewing project status across repositories, syncing GitHub data, and analyzing agents.md against commit patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[infantlab](https://clawhub.ai/user/infantlab) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering teams use this skill to track status across configured repositories, sync repository activity through existing CLI authentication, and get suggested improvements to agent instruction files based on commit patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads configured repositories using the user's existing CLI login and stores repository activity plus agent-instruction snapshots locally under ~/.god-mode. <br>
Mitigation: Install only when this access and local caching are acceptable; review configured projects and local data handling before use. <br>
Risk: Agent analysis may expose private agents.md content or commit-message details in shared terminal output or captured logs. <br>
Mitigation: Avoid running agent analysis in shared terminals or logs when repositories contain private operational details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/infantlab/skills/god-mode) <br>
- [GitHub CLI documentation](https://cli.github.com/) <br>
- [Configuration example](artifact/config.example.yaml) <br>
- [Agent analysis prompt](artifact/prompts/agent-analysis.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [CLI text and optional JSON, with Markdown guidance and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires gh, sqlite3, and jq; repository activity and agent-instruction snapshots are cached locally under ~/.god-mode.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
