## Description: <br>
Mandatory guardrail skill for system-level code modifications, with rules, checklists, verification steps, and rollback guidance for safer desktop and packaging changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loodiu](https://clawhub.ai/user/loodiu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill before system-level code changes to check whether they are modifying source rather than build output, using official build paths, preserving rollback options, and verifying each change batch. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes guidance around process-closing, build, deployment, login, and publishing commands that could affect a user's local environment if followed without review. <br>
Mitigation: Treat those commands as manual guidance, confirm user intent, and review the exact target process, files, and rollback plan before execution. <br>
Risk: Strong mandatory wording could be mistaken for blanket permission to modify system-level files. <br>
Mitigation: Require explicit user intent before system-level changes and prefer source edits, official build scripts, and step-by-step verification. <br>


## Reference(s): <br>
- [Safety Programming Checklist on ClawHub](https://clawhub.ai/loodiu/skills/safety-programming-checklist) <br>
- [Hermes Desktop Architecture Reference](references/hermes-desktop-architecture.md) <br>
- [Hermes Desktop Tray Pull Request](https://github.com/NousResearch/hermes-agent/pull/63064) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with checklists, tables, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; no executable skill code was found in the release evidence.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
