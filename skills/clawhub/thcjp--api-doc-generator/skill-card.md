## Description: <br>
Api Doc Generator is a professional API documentation workflow for development teams that helps generate and govern API documentation with code scanning, multi-format export, version management, mock integration, team review, GraphQL schema generation, custom templates, and bilingual documentation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to generate and maintain API documentation from natural language or selected code repositories. It supports OpenAPI and Markdown generation, document export, version comparison, mock-server workflows, and team review processes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read selected source directories and generate documentation from repository contents. <br>
Mitigation: Run it only on intentionally scoped paths and avoid including secrets or sensitive internal data in prompts or generated documentation. <br>
Risk: The skill proposes or runs API documentation CLI commands for scanning, export, mock, Git, and collaboration workflows. <br>
Mitigation: Review commands and output locations before execution, and use least-privilege collaboration tokens stored outside the repository. <br>
Risk: Generated API documentation, scan reports, and type inferences can be incomplete or inaccurate. <br>
Mitigation: Review generated OpenAPI specifications, scan reports, diffs, and exported documentation before relying on them in development or customer-facing workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/api-doc-generator) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with JSON, YAML, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce OpenAPI specifications, generated documentation, scan reports, diff summaries, mock-server commands, and export guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter matches) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
