## Description:

编码格式工具 helps agents encode, decode, inspect, and convert Base64, URL-encoded text, hex, Unicode, JWT payloads, hashes, and common serialization formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to have an agent decode API responses, encode HTTP request parameters, inspect binary or text encodings, analyze JWT payloads, calculate hashes, and convert common serialization formats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to run local shell commands on user-provided files or encoded payloads.

Mitigation: Review commands before execution and run them in a constrained workspace with least-privilege file access.

Risk: JWTs, API keys, files, callback URLs, and encoded payloads may contain sensitive data.

Mitigation: Use local-only processing where possible and provide secrets only when explicitly needed for the requested task.

Risk: The artifact includes unclear external API, callback, and API-key behavior.

Mitigation: Avoid external callbacks or API use until the publisher documents intended endpoints and data handling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/encoding-formats)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, and structured JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local command suggestions for encoding, decoding, hashing, and format conversion.]

## Skill Version(s):

1.0.0 (source: evidence release metadata; artifact frontmatter declares 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
