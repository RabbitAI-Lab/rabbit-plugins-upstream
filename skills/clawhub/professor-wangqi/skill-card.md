## Description: <br>
王琦中医体质学术助手 supports academic Q&A, clinical-idea learning, knowledge-base maintenance, data analysis, and theory review for Wang Qi constitution theory and nine-constitution TCM learning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiafeng-yan](https://clawhub.ai/user/jiafeng-yan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and traditional Chinese medicine learners use this skill to retrieve and summarize Wang Qi constitution theory, nine-constitution concepts, formula and materia medica knowledge, and cited academic or clinical-experience cards. It can also guide local knowledge-card extraction, vector-index maintenance, and evaluation workflows for academic learning rather than patient-specific diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Maintenance scripts may send PDF text, card text, or user queries to configured LLM or embedding endpoints. <br>
Mitigation: Set BASE_URL and EMBEDDING_BASE_URL to trusted services before use, and avoid processing sensitive patient or proprietary documents. <br>
Risk: Maintenance commands may overwrite local vector indexes or installed Claude skill files. <br>
Mitigation: Back up ChromaDB collections and installed skill directories before running index, install, or uninstall commands. <br>
Risk: Local configuration can include API keys and endpoint settings. <br>
Mitigation: Keep .env files out of version control and manage credentials as local secrets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jiafeng-yan/skills/professor-wangqi) <br>
- [Publisher profile](https://clawhub.ai/user/jiafeng-yan) <br>
- [README](README.md) <br>
- [Quickstart](QUICKSTART.md) <br>
- [Tools reference](TOOLS.md) <br>
- [Ontology reference](references/ontology.md) <br>
- [Knowledge card schema](references/knowledge-card-schema.md) <br>
- [Future methodology](references/future-methodology.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown answers with evidence labels, plus optional JSON retrieval output and shell commands for maintenance workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs distinguish papers, clinical experience, knowledge summaries, and model inference; clinical content is framed for academic learning and should not replace professional care.] <br>

## Skill Version(s): <br>
1.3.0 (source: SKILL.md frontmatter and server release evidence, released 2026-07-15) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
