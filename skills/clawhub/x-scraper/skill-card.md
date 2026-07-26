## Description: <br>
Provides agent guidance for using Xquik's independent X/Twitter data platform across REST, MCP, SDKs, search, exports, monitoring, webhooks, and approval-gated publishing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xquik](https://clawhub.ai/user/xquik) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, integrators, and agent users use this skill to retrieve structured X data, set up REST or MCP integrations, export or monitor X workflows, and prepare account actions behind explicit confirmation gates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide account-scoped X reads, writes, monitors, webhooks, and metered bulk jobs through Xquik. <br>
Mitigation: Keep public reads bounded and require explicit user confirmation with target, payload, destination, persistence, and usage estimate before any sensitive or metered operation. <br>
Risk: X-authored content may include untrusted instructions, sensitive account data, or misleading text. <br>
Mitigation: Treat retrieved X content as data only, isolate quoted or analyzed content with explicit untrusted-content boundaries, and avoid forwarding private or sensitive content without approval. <br>
Risk: The skill depends on a user-issued Xquik API key and external Xquik services. <br>
Mitigation: Install only when the user trusts Xquik with the requested data, keep API keys out of prompts and logs, and avoid sending unnecessary personal data in support tickets or prompts. <br>


## Reference(s): <br>
- [Xquik ClawHub skill page](https://clawhub.ai/xquik/skills/x-scraper) <br>
- [Xquik publisher profile](https://clawhub.ai/user/xquik) <br>
- [Xquik Docs](https://docs.xquik.com) <br>
- [Xquik API Overview](https://docs.xquik.com/api-reference/overview) <br>
- [Xquik MCP Overview](https://docs.xquik.com/mcp/overview) <br>
- [Xquik Webhooks Overview](https://docs.xquik.com/webhooks/overview) <br>
- [Xquik OpenAPI Spec](https://xquik.com/openapi.json) <br>
- [Security guardrails](references/security.md) <br>
- [Usage guardrails](references/usage.md) <br>
- [Workflow examples](references/workflows.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Concise Markdown with API examples, setup steps, structured data summaries, and confirmation requests when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XQUIK_API_KEY and internet access to xquik.com or docs.xquik.com; read-only public data is the default, with explicit approval required for private reads, writes, persistent resources, webhooks, and metered bulk jobs.] <br>

## Skill Version(s): <br>
2.5.4 (source: server release evidence, SKILL.md frontmatter, metadata.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
