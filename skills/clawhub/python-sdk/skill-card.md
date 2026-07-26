## Description: <br>
Python SDK guidance for inference.sh that helps developers run AI apps, stream results, upload files, manage sessions, and build agents with sync or async Python code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers use this skill to integrate inference.sh from Python, including app execution, streaming, file handling, stateful sessions, and agent/tool workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can suggest local Python commands and examples that execute tools or code. <br>
Mitigation: Review generated commands and tool handlers before running them, and require human approval for sensitive local operations. <br>
Risk: Examples may send prompts, files, API keys, webhook payloads, or generated data to inference.sh or configured external services. <br>
Mitigation: Use only intended data, keep API and webhook secrets protected, and avoid public uploads for sensitive content. <br>
Risk: Some examples demonstrate unsafe patterns such as eval-style calculation or unvalidated tool execution. <br>
Mitigation: Treat those snippets as illustrative only and replace them with validated, least-privilege production handlers. <br>


## Reference(s): <br>
- [Python SDK Reference](https://inference.sh/docs/api/sdk-python) <br>
- [Agent SDK Overview](https://inference.sh/docs/api/agent-sdk) <br>
- [Tool Builder Reference](https://inference.sh/docs/api/agent-tools) <br>
- [Authentication](https://inference.sh/docs/api/authentication) <br>
- [Streaming](https://inference.sh/docs/api/sdk/streaming) <br>
- [File Uploads](https://inference.sh/docs/api/sdk/files) <br>
- [Agent Patterns](references/agent-patterns.md) <br>
- [Async Patterns Reference](references/async-patterns.md) <br>
- [File Handling Reference](references/files.md) <br>
- [Sessions Reference](references/sessions.md) <br>
- [Streaming Reference](references/streaming.md) <br>
- [Tool Builder Reference](references/tool-builder.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with Python and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include SDK setup steps, API usage examples, agent patterns, streaming handlers, file upload flows, and security notes.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
