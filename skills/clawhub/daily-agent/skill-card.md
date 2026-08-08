## Description: <br>
Schedules and coordinates long-running agent tasks after routing by skill-router, including complexity assessment, sub-agent delegation, Hat-system orchestration, and closeout checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agent operators and developers use this skill to classify complex requests, choose an execution route, delegate work to sub-agents, and run closeout checks for long-running workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is a broad workflow orchestrator that can store user memory, run local scripts, create skills, and commit files automatically. <br>
Mitigation: Review or disable the profile observer, memory writes, git commit step, skill creation flow, and host script hooks before installation. <br>
Risk: Automatic persistence and execution paths can expose sensitive personal, business, or credential-bearing workspace material. <br>
Mitigation: Use only in workspaces where persistence and execution are constrained, and avoid sensitive workspaces unless those paths are reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/daily-agent) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with optional code, shell command, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May delegate work, propose or run local scripts, create files, and record memory when installed in a capable agent environment.] <br>

## Skill Version(s): <br>
2.18.0 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
