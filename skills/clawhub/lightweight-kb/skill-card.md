## Description: <br>
Lightweight Knowledge Base is a local knowledge-base and task-management skill that uses JSON and Markdown storage for user profiles, task rhythms, knowledge indexing, and daily evolution workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[williamtie](https://clawhub.ai/user/williamtie) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to set up a local persistent knowledge base for user profiling, recurring task rhythms, searchable memory indexes, and task execution guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores and updates local profile, task, and knowledge-index data that may contain personal preferences or workflow details. <br>
Mitigation: Review or reset data/user_profile.json before use, and avoid storing API keys or sensitive personal details in indexed memory files. <br>
Risk: The bundled task rhythm data includes enabled recurring daily, weekly, and deep-dialogue tasks. <br>
Mitigation: Disable unwanted recurring tasks in data/task_rhythm.json before using the skill in an agent workflow. <br>
Risk: The local scripts create directories and update files in the OpenClaw workspace. <br>
Mitigation: Run the scripts only in the intended workspace and review generated or modified files after initialization and daily evolution runs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/williamtie/skills/lightweight-kb) <br>
- [Communication guide](references/communication.md) <br>
- [Task execution guide](references/task_guidelines.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON-backed local files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates and updates local JSON and Markdown knowledge-base files, task rhythm data, and status text.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
