## Description: <br>
baml-codegen helps agents generate complete BAML source files, tests, clients, and framework integrations for type-safe LLM extraction, classification, RAG, and agent workflows from natural language requirements. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[killerapp](https://clawhub.ai/user/killerapp) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and engineers use this skill to turn application requirements into BAML schemas, functions, client configuration, tests, and integration snippets. It is suited for structured extraction, classification, RAG, multimodal input handling, and agent workflow scaffolding. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated BAML, tests, and integration snippets may introduce incorrect behavior if accepted without review. <br>
Mitigation: Review generated diffs before running, committing, or deploying the output. <br>
Risk: BAML generation may execute local post-generation hooks such as formatter commands. <br>
Mitigation: Inspect any on_generate hook before running baml-cli generate. <br>
Risk: The skill can rely on MCP servers for documentation and examples. <br>
Mitigation: Use trusted MCP servers and fall back to cached reference material when live sources are unavailable. <br>
Risk: Prompts and generated workflows may route sensitive data through external model providers. <br>
Mitigation: Avoid processing sensitive or regulated data unless consent, redaction, and provider controls are in place. <br>


## Reference(s): <br>
- [BAML Reference Guide for AI Agents](references/BAML-REFERENCE-SOURCE.md) <br>
- [BAML Pattern Library](references/patterns.md) <br>
- [BAML Types and Schemas Reference](references/types-and-schemas.md) <br>
- [Validation Patterns Reference](references/validation.md) <br>
- [Provider Configuration Reference](references/providers.md) <br>
- [MCP Interface and Query Strategy](references/mcp-interface.md) <br>
- [Python and BAML Reference](references/languages-python.md) <br>
- [TypeScript and BAML Reference](references/languages-typescript.md) <br>
- [LangGraph and BAML Integration Reference](references/frameworks-langgraph.md) <br>
- [BoundaryML BAML releases](https://github.com/BoundaryML/baml/releases) <br>
- [BAML VS Code extension](https://marketplace.visualstudio.com/items?itemName=boundary.baml-extension) <br>


## Skill Output: <br>
**Output Type(s):** [code, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with BAML, Python, TypeScript, and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include generated .baml files, tests, framework integration snippets, pattern metadata, token counts, and cost estimates.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
