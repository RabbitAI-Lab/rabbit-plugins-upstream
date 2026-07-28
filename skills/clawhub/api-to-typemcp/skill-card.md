## Description: <br>
Turns supplied local API sources into a TypeMCP project with manifest review, digest-bound approval, and generated-project verification gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sjungwon03](https://clawhub.ai/user/sjungwon03) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to turn supplied local OpenAPI, Swagger, Swagger UI, Markdown, or HTML API references into a TypeMCP stdio MCP server project. It is intended for workflows where the generated manifest is reviewed and explicitly approved before code generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated projects install and execute package dependencies during verification, and the security evidence flags limited containment plus inconsistent dependency disclosures. <br>
Mitigation: Review generated dependency ranges, add a lockfile or audit step where practical, and run verification in a container or similarly isolated workspace. <br>
Risk: API specifications or reference documents may contain secrets or sensitive operational details. <br>
Mitigation: Do not place secrets in supplied specs or documentation fields; review the secret-free manifest before approval and generation. <br>
Risk: Generated MCP tools can represent mutating upstream API operations. <br>
Mitigation: Enable protected-write operations only by exact operation ID when mutation is intended, and keep the default deny behavior for unreviewed write operations. <br>
Risk: A generated project may reflect incomplete or incorrect API documentation. <br>
Mitigation: Inspect the manifest first, confirm the canonical digest, and regenerate only after the reviewed manifest matches the intended local source. <br>


## Reference(s): <br>
- [TypeMCP Runtime Contract](references/type-mcp-runtime.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Generated TypeScript project files, JSON manifests, Markdown guidance, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated projects target local stdio MCP use and include policy tests plus a secret-free manifest copy.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
