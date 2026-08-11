## Description:

Local stdlib-only proxy that adapts OpenAI Chat Completions to/from the Responses API so OpenAI-compatible agent clients can use Responses-API-only models such as OpenCode Go gpt-5.6-luna.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andypeng09](https://clawhub.ai/user/andypeng09)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to run a local protocol bridge that lets OpenAI-compatible clients send Chat Completions requests to Responses API-only upstream models. It provides setup guidance, client configuration examples, and a Python proxy for streaming, tool calls, reasoning content, and multimodal input conversion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local proxy can store sensitive prompt and upstream request data in debug files beside the script.

Mitigation: Avoid confidential prompts unless logging is disabled or modified; after troubleshooting, remove proxy-requests.log, proxy-last-request.json, proxy-last-upstream.json, and proxy-last-error.txt.

Risk: Conversation data is forwarded to the configured upstream Responses API endpoint.

Mitigation: Keep the proxy bound to localhost, configure OPENCODE_UPSTREAM deliberately, and use it only with upstream services whose data handling you accept.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/ANDYPENG09/opencode-responses-bridge-skill)
- [ClawHub skill page](https://clawhub.ai/andypeng09/skills/opencode-responses-bridge-skill)
- [Protocol mapping reference](references/protocol-mapping.md)
- [ClawHub metadata homepage](https://github.com/ANDYPENG09/opencode-responses-bridge-skill)
- [Default Responses API upstream endpoint](https://opencode.ai/zen/go/v1/responses)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples, shell commands, and Python proxy files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local proxy scripts and client setup examples for Windows, macOS, and Linux.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
