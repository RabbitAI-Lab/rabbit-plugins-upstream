## Description: <br>
Access and query structured department knowledge for PLC models, coding standards, code templates, and device parameters to aid automation tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation engineers use this skill to ingest local manuals, code templates, CSV or Excel tables, and domain notes into a searchable knowledge base, then query it for PLC, WCS, industrial vision, code template, constraint, and device-parameter context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads user-selected local files into a persistent local knowledge store, which may capture secrets, personal data, or proprietary details if those files are ingested. <br>
Mitigation: Review source files before extraction and avoid ingesting confidential or regulated data unless the local storage location and access controls are appropriate. <br>
Risk: Retrieved domain knowledge may be stale or incomplete after source documents or engineering standards change. <br>
Mitigation: Refresh the knowledge store from current source files and verify generated automation guidance against authoritative project standards before use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/paudyyin/skills/tmp-domain-kit) <br>
- [Skill Manifest](artifact/SKILL.md) <br>
- [Knowledge Schema](artifact/schema/base.json) <br>
- [Automation Schema](artifact/schema/automation.json) <br>
- [WCS Schema](artifact/schema/wcs.json) <br>
- [Vision Schema](artifact/schema/vision.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text from CLI queries, with optional extracted JSONL knowledge records stored locally] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Query results are ranked by stored confidence and may include source paths, entity relationships, constraints, code templates, and best-practice context.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
