## Description: <br>
Extracts hierarchical knowledge graph nodes from PDF or Word documents, annotates node types and semantic relationships, and prepares CSV or Excel outputs for course-platform import. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flyboat403](https://clawhub.ai/user/flyboat403) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, educators, and course-content operators use this skill to turn PDF or Word curriculum documents into structured knowledge-node data with hierarchy, node type, prerequisites, related concepts, tags, descriptions, and objectives. The generated CSV and Excel outputs are intended for import into knowledge graph or online course systems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The quality-check workflow may modify generated JSON files while correcting hierarchy, category, relation, or objective issues. <br>
Mitigation: Review the resulting diff or keep a backup before accepting generated knowledge graph outputs, especially when accuracy matters. <br>
Risk: Incorrect node hierarchy, relationship references, or fixed-column formatting can cause downstream course-platform import failures or misleading knowledge structures. <br>
Mitigation: Run the documented validation checks and inspect the CSV or Excel output before importing it into production course systems. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/flyboat403/knowledge-graph-extraction-skill) <br>
- [ClawHub skill page](https://clawhub.ai/flyboat403/skills/knowledge-graph-extraction-skill) <br>
- [Extraction prompt reference](artifact/references/extraction-prompt.md) <br>
- [Output format reference](artifact/references/output-format.md) <br>
- [Quality check prompt reference](artifact/references/quality-check-prompt.md) <br>
- [Relation prompt reference](artifact/references/relation-prompt.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, CSV, Excel files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON knowledge-node structures, and CSV or Excel file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs follow fixed column and hierarchy constraints for course-platform import; generated JSON may be edited during quality checks.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
