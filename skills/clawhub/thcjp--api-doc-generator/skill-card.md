## Description: <br>
Api Doc Generator helps developers and engineering teams generate and govern API documentation from natural-language instructions, source-code scans, OpenAPI specs, exported documentation, mock servers, and team review workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to create and maintain API documentation, including OpenAPI specifications, Markdown docs, exported HTML/PDF/Swagger UI artifacts, mock-server setup, version diffs, and review workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for broad development-tool access, including reading API source code and writing generated documentation files. <br>
Mitigation: Review source and output paths before execution, limit scope to intended repositories, and inspect generated documentation before sharing it. <br>
Risk: The skill can propose running the api-doc CLI and starting local mock services. <br>
Mitigation: Confirm commands, ports, and target files before allowing execution, and run mock services in a local or sandboxed project environment. <br>
Risk: Team collaboration features may involve tokens or review-system access. <br>
Mitigation: Use restricted tokens, store them outside the repository, and verify Git remotes, reviewers, and token storage before enabling collaboration workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/api-doc-generator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured documentation guidance with inline JSON, YAML, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct an agent to write generated documentation files, export API specs, start local mock services, and prepare review or version-management commands.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata; artifact frontmatter says 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
