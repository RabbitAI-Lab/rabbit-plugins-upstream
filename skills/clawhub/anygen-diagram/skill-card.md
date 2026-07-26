## Description: <br>
Anygen Diagram helps enterprise teams generate diagrams from natural-language or structured descriptions using AnyGen CLI and API workflows, with support for batch generation, templates, team asset workflows, and PNG, SVG, PDF, or Markdown outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical writers, product teams, and enterprise documentation teams use this skill to produce and manage architecture diagrams, process diagrams, organization charts, and product-flow visuals from text, structured inputs, or batch specifications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Diagram prompts and source documents may be sent to AnyGen's remote service. <br>
Mitigation: Redact confidential architecture, PRD, customer, or internal process details before submission unless the organization has approved AnyGen for that data. <br>
Risk: Generated files may overwrite existing local diagram or template assets. <br>
Mitigation: Review output paths such as ./diagrams/ and ./templates/ before running generation or asset-management commands. <br>
Risk: The skill expects an AnyGen API key for normal operation. <br>
Mitigation: Store ANYGEN_API_KEY with the organization's normal secret-management process and avoid committing credentials to repositories. <br>


## Reference(s): <br>
- [AnyGen homepage](https://skillhub.cn) <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/anygen-diagram) <br>
- [AnyGen diagrams API endpoint](https://api.anygen.io/v1/diagrams) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands, API examples, JSON examples, and generated diagram file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or update local diagram and template files such as ./diagrams/ and ./templates/.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
