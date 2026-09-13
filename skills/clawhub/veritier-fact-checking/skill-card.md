## Description:

Veritier provides an Agent Trust Gate that can block unsupported tool calls and can also extract, verify, and validate claims or documents through MCP or REST.

This skill is ready for commercial/non-commercial use.

## Publisher:

[salomonhenao](https://clawhub.ai/user/salomonhenao)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this skill to gate tool calls against systems of record, verify factual claims, audit generated text, and validate suspicious documents before an agent acts or publishes an answer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some bundled examples may weaken the stated API-key boundary or webhook exposure posture.

Mitigation: Review before installing or running examples, use a dedicated Veritier test key for tests, and do not run the JavaScript integration test with an untrusted API_URL or a production key.

Risk: The Python webhook receiver example may be unsafe if exposed with broad binding or debug behavior.

Mitigation: Change the receiver to bind to 127.0.0.1 with debug disabled before exposing it beyond local testing.

Risk: Submitted content is sent to Veritier, and Claim Credentials may remain publicly reconstructable by ID for 400 days.

Mitigation: Avoid submitting sensitive content unless that retention and reconstruction behavior is acceptable, and treat Claim Credentials as signed workpapers rather than certificates of truth.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/salomonhenao/skills/veritier-fact-checking)
- [Veritier homepage](https://veritier.ai)
- [Hosted skill instructions](https://veritier.ai/skill.md)
- [Hosted examples README](https://veritier.ai/README.md)
- [Live OpenAPI specification](https://api.veritier.ai/openapi.json)
- [Interactive API documentation](https://api.veritier.ai/docs)
- [Hosted MCP endpoint](https://api.veritier.ai/mcp/)
- [API key dashboard](https://veritier.ai/dashboard)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration, shell commands, REST examples, and agent-readable tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns claim verdicts, confidence scores, explanations, source URLs, attestation decisions, and Claim Credential IDs or verify URLs.]

## Skill Version(s):

3.4.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
