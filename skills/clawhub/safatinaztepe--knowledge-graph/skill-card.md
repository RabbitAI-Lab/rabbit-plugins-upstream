## Description: <br>
Maintain Clawdbot's compounding knowledge graph under life/areas/** by adding/superseding atomic facts (items.json), regenerating entity summaries (summary.md), and keeping IDs consistent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[safatinaztepe](https://clawhub.ai/user/safatinaztepe) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to make deterministic updates to a local file-based knowledge graph by adding facts, superseding stale facts, and regenerating entity summaries without manually editing JSON. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes local knowledge-graph files under life/areas/**, which can affect important personal or project records. <br>
Mitigation: Review or back up those files before use, and prefer releases that explicitly declare file read/write scope. <br>


## Reference(s): <br>
- [Knowledge Graph skill page](https://clawhub.ai/safatinaztepe/skills/knowledge-graph) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Markdown, Configuration] <br>
**Output Format:** [Markdown guidance with shell command examples and file updates to JSON and Markdown knowledge-graph files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Updates workspace-local life/areas/** items.json and summary.md files through the bundled Python script.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
