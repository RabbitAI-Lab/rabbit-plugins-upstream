## Description: <br>
JavaScript/TypeScript SDK guidance for inference.sh that helps agents install @inferencesh/sdk, run AI apps, build agents, use streaming, upload files, and integrate Node.js, React, Next.js, and browser applications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to integrate JavaScript or TypeScript applications with inference.sh, including app execution, streaming, file handling, sessions, agent workflows, tool builders, and frontend proxy patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can suggest npm, npx, node, yarn, and pnpm commands. <br>
Mitigation: Approve package and runtime commands case by case, and install only when intentionally working with @inferencesh/sdk. <br>
Risk: Credential examples may lead users to expose privileged API keys in frontend code. <br>
Mitigation: Keep real API keys server-side, use backend proxy patterns for browser applications, and avoid NEXT_PUBLIC variables for privileged keys. <br>
Risk: File upload and public file examples can expose sensitive data. <br>
Mitigation: Upload only files intended for the service and avoid public file settings for sensitive content. <br>
Risk: Tool execution, webhooks, browser automation, code execution, and model-triggered actions can perform sensitive operations. <br>
Mitigation: Use allowlists, input validation, and human approval around external calls and tool actions. <br>
Risk: Some calculator-style examples use eval-like behavior. <br>
Mitigation: Replace eval examples with a safe parser before adapting them into production tools. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/okaris/skills/javascript-sdk) <br>
- [inference.sh](https://inference.sh) <br>
- [JavaScript SDK Reference](https://inference.sh/docs/api/sdk-javascript) <br>
- [Agent SDK Overview](https://inference.sh/docs/api/agent-sdk) <br>
- [Tool Builder Reference](https://inference.sh/docs/api/agent-tools) <br>
- [Server Proxy Setup](https://inference.sh/docs/api/sdk/server-proxy) <br>
- [Authentication](https://inference.sh/docs/api/authentication) <br>
- [Streaming](https://inference.sh/docs/api/sdk/streaming) <br>
- [File Handling Reference](references/files.md) <br>
- [React Integration Reference](references/react-integration.md) <br>
- [Tool Builder Reference](references/tool-builder.md) <br>
- [TypeScript Reference](references/typescript.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with TypeScript, JavaScript, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Covers SDK installation, authentication, API calls, streaming, file uploads, sessions, agent patterns, tool builders, and frontend proxy setup.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
