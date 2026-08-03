## Description: <br>
Generates structured PRDs and review checklists from brief Chinese or English product requirements, with optional UML diagrams, JSON export, and multi-role review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shylamb-token](https://clawhub.ai/user/shylamb-token) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product managers, product teams, developers, and QA reviewers use this skill to expand a concise product requirement into a structured PRD, review checklist, and optional diagram or JSON export for downstream planning and validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated PRDs and review checklists can include assumptions or inferred requirements that are not validated by stakeholders. <br>
Mitigation: Review generated PRD content with product, engineering, QA, and security stakeholders before using it as implementation guidance. <br>
Risk: Export and long-output modes can create Markdown, JSON, or diagram files in the workspace. <br>
Mitigation: Review requested filenames and target paths before allowing file output, especially in workspaces that contain important documents. <br>
Risk: JSON exports or diagram files may be consumed by downstream systems such as CI, Notion, or Jira. <br>
Mitigation: Validate generated structured output before importing it into downstream planning or automation systems. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shylamb-token/skills/prd-autogen-and-review) <br>
- [Publisher profile](https://clawhub.ai/user/shylamb-token) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, code, configuration, guidance] <br>
**Output Format:** [Markdown PRD and review checklist, with optional SVG/HTML UML diagram and JSON export.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create Markdown, JSON, or diagram files in the workspace when export or file-output modes are requested.] <br>

## Skill Version(s): <br>
1.5.0 (source: release evidence and artifact version notes) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
