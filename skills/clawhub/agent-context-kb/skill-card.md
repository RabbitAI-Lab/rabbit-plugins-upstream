## Description: <br>
Manage and explain a repository-local `.agent-kb/` knowledge base for coding agents, including initialization, upgrades, validation, note capture, compilation, trimming, and stats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lesliebiubiubiu](https://clawhub.ai/user/lesliebiubiubiu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to set up and maintain project memory in `.agent-kb/`, preserve durable repository knowledge, and report KB usage and churn. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify `.agent-kb/`, create a nested KB git repository, and run local git commands. <br>
Mitigation: Run it only in the intended repository, review generated KB changes, and confirm versioning mode before initialization. <br>
Risk: The `stats` workflow can read local Claude and Codex transcript stores and store derived KB activity metadata. <br>
Mitigation: Use `stats --no-backfill`, `--no-backfill-claude`, or `--no-backfill-codex` unless transcript-based analytics are intended. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/lesliebiubiubiu/agent-context-kb-skill/tree/main/skills/agent-context-kb) <br>
- [ClawHub skill page](https://clawhub.ai/lesliebiubiubiu/skills/agent-context-kb) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown text with shell command examples and local file updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or modify `.agent-kb/` files and print ASCII stats charts.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
