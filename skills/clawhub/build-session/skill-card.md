## Description: <br>
Facilitates focused autonomous sessions to build, create, or produce one concrete deliverable, then log and commit progress efficiently. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stevenartzt](https://clawhub.ai/user/stevenartzt) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to structure scheduled or autonomous work sessions around one concrete deliverable, with prompts for task selection, execution, logging, and optional Git follow-through. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill encourages autonomous repository edits, commits, and pushes, which can publish incorrect changes if used without review. <br>
Mitigation: Use it in an isolated repository or branch and require human review of diffs before commits or pushes. <br>
Risk: The suggested Git flow can stage more files than intended. <br>
Mitigation: Inspect changes before staging, avoid blind git add -A, and stage only the intended files. <br>
Risk: Autonomous build sessions can accidentally expose sensitive content during remote publication. <br>
Mitigation: Run secret checks before any push or remote publication. <br>


## Reference(s): <br>
- [Build Session on ClawHub](https://clawhub.ai/stevenartzt/skills/build-session) <br>
- [stevenartzt publisher profile](https://clawhub.ai/user/stevenartzt) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown instructions with shell and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce session logs, task selections, repository edits, Git status summaries, commits, or push commands depending on the agent session.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
