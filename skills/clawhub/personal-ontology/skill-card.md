## Description: <br>
Help users build and maintain a Personal Ontology - a Palantir-style graph of Objects (identity, beliefs, predictions, goals) and Links (relationships between them) that enables AI-driven decision-making and life alignment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[levineam](https://clawhub.ai/user/levineam) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to extract, organize, review, and maintain a personal knowledge graph of beliefs, predictions, goals, projects, and relationships from markdown notes. It supports decision-making, prioritization, alignment checks, and optional daily review workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and summarize sensitive personal notes, including beliefs, goals, predictions, and quotes. <br>
Mitigation: Limit the folder scope before bootstrap or daily scans, exclude private journals or archives when needed, and install only where this access is acceptable. <br>
Risk: Extracted personal ontology entries could persist sensitive or inaccurate interpretations in local files. <br>
Mitigation: Require review before every file write, keep candidate updates in the suggestions queue, and edit or delete ontology and state files as needed. <br>
Risk: Automated scans can surface conflicts, orphans, or stale predictions from personal data in ways that may be overbroad. <br>
Mitigation: Use the artifact's review flow for accept, edit, or skip decisions and keep passive scans narrow, periodic, and user-confirmed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/levineam/skills/personal-ontology) <br>
- [README](artifact/README.md) <br>
- [Setup guide](artifact/SETUP.md) <br>
- [Bootstrap extraction workflow](artifact/bootstrap.md) <br>
- [Object categorization heuristics](artifact/heuristics.md) <br>
- [Guided prompts](artifact/prompts.md) <br>
- [Ontology renderer script](artifact/scripts/render-ontology.js) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional shell commands, ontology files, suggestion queues, and Mermaid graph output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may propose ontology updates, create or update markdown files after user review, and render Mermaid, ASCII, or SVG graph views from local ontology files.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
