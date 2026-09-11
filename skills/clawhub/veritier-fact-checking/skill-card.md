## Description:

Veritier gives agents an API and MCP trust gate for fact-checking claims, validating documents, and fail-closed attestation before sensitive tool calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[salomonhenao](https://clawhub.ai/user/salomonhenao)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to check claims, audit generated text, validate untrusted documents, and gate tool calls against external systems of record before acting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release was flagged as suspicious because installation and example-code paths require review before use.

Mitigation: Install only from a reviewed local copy or pinned, verified release, and scan the skill before deployment.

Risk: The skill requires a Veritier API key and sends it as bearer authentication.

Mitigation: Use a dedicated key with minimal account privileges and send it only to https://api.veritier.ai.

Risk: Example test and webhook paths can be unsafe if pointed at untrusted destinations or exposed broadly.

Mitigation: Prefer vt_test_ keys for tests, avoid overriding API_URL unless the destination is trusted, and keep the Python webhook receiver off public debug deployments.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/salomonhenao/skills/veritier-fact-checking)
- [Veritier website](https://veritier.ai)
- [Veritier documentation](https://veritier.ai/docs)
- [Veritier dashboard](https://veritier.ai/dashboard)
- [MCP endpoint](https://api.veritier.ai/mcp/)
- [Skill source](https://veritier.ai/skill.md)
- [Examples README](https://veritier.ai/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, and Python or JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API request examples, MCP configuration, verification summaries, document-validation guidance, and gate decisions.]

## Skill Version(s):

3.4.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
