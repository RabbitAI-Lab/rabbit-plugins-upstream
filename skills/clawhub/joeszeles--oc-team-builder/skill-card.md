## Description: <br>
Discover, compose, and activate specialist teams from three rosters: OpenClaw Core, Agency Division specialists, and a Research Lab for autonomous experiment loops. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[JoeSzeles](https://clawhub.ai/user/JoeSzeles) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, project leads, and agent operators use this skill to browse specialist rosters, generate team proposals, activate agent definitions, prepare QA review checklists, and run metric-driven experiment workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The experiment workflow can run shell commands and modify repository state. <br>
Mitigation: Use a sandbox, disposable branch, or test copy of the project; review run commands and in-scope file settings before execution. <br>
Risk: Autonomous experiment loops may continue without sufficient supervision. <br>
Mitigation: Set explicit runtime and cost limits and avoid running the loop unattended on important repositories. <br>
Risk: Agent definitions or direct file paths can load untrusted content. <br>
Mitigation: Use trusted roster files and review any arbitrary --file input before activation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/JoeSzeles/oc-team-builder) <br>
- [Publisher Profile](https://clawhub.ai/user/JoeSzeles) <br>
- [Karpathy autoresearch](https://github.com/karpathy/autoresearch) <br>
- [PLANNER.md](references/PLANNER.md) <br>
- [REVIEWER.md](references/REVIEWER.md) <br>
- [TEAM-RESEARCH.md](references/TEAM-RESEARCH.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, plain text, JSON roster output, and shell command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Some scripts can write proposal, review, ledger, or log files when output paths or experiment directories are provided.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
