## Description:

Provides guidance for using the inference.sh JavaScript/TypeScript SDK to build AI apps, run models, manage files and sessions, stream results, and integrate agents in Node.js, React, Next.js, and browser apps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okaris](https://clawhub.ai/user/okaris)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill when integrating @inferencesh/sdk into JavaScript or TypeScript applications, including Node.js, React, Next.js, browser clients, and agent workflows. It provides implementation guidance, code examples, and configuration patterns for SDK installation, authentication, streaming, file handling, server proxies, tools, and sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can suggest npm, npx, yarn, pnpm, or node commands.

Mitigation: Require explicit approval and review command intent before execution.

Risk: Copyable examples can expose API keys or create unsafe proxy endpoints.

Mitigation: Keep API keys server-only and add authentication, authorization, rate limits, and allowlists to proxy endpoints.

Risk: Tool handler examples may include eval-based execution.

Mitigation: Do not copy eval-based handlers; replace them with allowlisted operations or a safe parser.

Risk: File uploads, webhooks, browser automation, and saved chat history can transfer or retain sensitive data.

Mitigation: Avoid public uploads unless intentional and review data handling, retention, and access controls before use.

## Reference(s):

- [Agent Patterns](references/agent-patterns.md)
- [Tool Builder Reference](references/tool-builder.md)
- [Server Proxy Setup](references/server-proxy.md)
- [Streaming Reference](references/streaming.md)
- [File Handling Reference](references/files.md)
- [Sessions Reference](references/sessions.md)
- [TypeScript Reference](references/typescript.md)
- [React Integration Reference](references/react-integration.md)
- [JavaScript SDK Reference](https://inference.sh/docs/api/sdk-javascript)
- [Agent SDK Overview](https://inference.sh/docs/api/agent-sdk)
- [Tool Builder Reference](https://inference.sh/docs/api/agent-tools)
- [Server Proxy Setup](https://inference.sh/docs/api/sdk/server-proxy)
- [Authentication](https://inference.sh/docs/api/authentication)
- [Streaming](https://inference.sh/docs/api/sdk/streaming)
- [File Uploads](https://inference.sh/docs/api/sdk/files)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with TypeScript, JavaScript, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include npm, yarn, pnpm, or node command suggestions and SDK code snippets.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
