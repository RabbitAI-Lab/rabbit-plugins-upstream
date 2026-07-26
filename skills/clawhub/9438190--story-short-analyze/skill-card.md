## Description: <br>
Analyzes short-form Chinese web fiction by breaking down story core, structure, emotional arc, twists, writing techniques, character functions, reusable patterns, and quality checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[9438190](https://clawhub.ai/user/9438190) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and creative-writing teams use this skill to produce structured critique of legally available short fiction, including plot beats, emotional hooks, twist mechanics, character roles, reusable writing patterns, and downstream metadata for later writing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill saves a local copy of user-provided story text and generated analysis under `拆文库/{书名}/`. <br>
Mitigation: Use it only with story files you intend the agent to read and store locally, and review the generated directory before sharing or committing outputs. <br>
Risk: The skill is designed to read user-provided file paths for source material. <br>
Mitigation: Provide explicit paths only to intended story files and prefer explicit commands such as `/story-short-analyze`. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/9438190/skills/story-short-analyze) <br>
- [Publisher profile](https://clawhub.ai/user/9438190) <br>
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [Output contract](references/output-contract.md) <br>
- [Output templates](references/output-templates.md) <br>
- [Material decomposition](references/material-decomposition.md) <br>
- [Quality checklist](references/quality-checklist.md) <br>
- [Genre catalog](references/genre-catalog.md) <br>
- [Anti-AI writing guide](references/anti-ai-writing.md) <br>
- [Banned words](references/banned-words.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown analysis files with JSON metadata] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local analysis outputs under a story-specific directory, including source backup, reports, plot-node notes, technique notes, and _meta.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence; artifact frontmatter says 3.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
