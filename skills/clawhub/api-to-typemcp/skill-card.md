## Description: <br>
Use when a user wants to turn an API URL, OpenAPI/Swagger file or link, Swagger UI, or Markdown/HTML API documentation into a standalone TypeMCP MCP project through the type-mcp-api-cli. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sjungwon03](https://clawhub.ai/user/sjungwon03) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to turn supplied API documentation into a maintainable TypeMCP MCP project while preserving approval, verification, and publication gates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may run code-generation tooling, npm checks, and GitHub publication steps. <br>
Mitigation: Require explicit approval for generation, live authenticated tests, and publication; review the generated project and destination repository first. <br>
Risk: The skill depends on a referenced CLI compatibility policy and trusted CLI selection. <br>
Mitigation: Verify the CLI compatibility policy exists in the workspace and stop if no supported CLI release is enabled. <br>
Risk: API sources or generated files may contain credentials or private specification details. <br>
Mitigation: Use environment-variable references, redact likely credentials, scan staged files for secrets, and avoid committing downloaded private specifications. <br>


## Reference(s): <br>
- [Api To Typemcp ClawHub page](https://clawhub.ai/sjungwon03/skills/api-to-typemcp) <br>
- [CLI compatibility policy](../../docs/guides/cli-compatibility.md) <br>
- [Security and publication policy](../../docs/guides/security-and-publication.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, generated project files, manifests, approval receipts, verification results, and publication instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated project output is gated by manifest approval, contained verification, secret scrubbing, and final publication confirmation.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
