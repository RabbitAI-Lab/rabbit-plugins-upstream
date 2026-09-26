## Description:

Provides encoding, decoding, and data-format conversion guidance for Base64, URL encoding, hexadecimal data, Unicode, JWT payloads, hashes, and common serialization formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect, decode, encode, and convert common data formats while debugging API responses, request parameters, binary data, JWTs, file checksums, and serialized files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags unscoped API key, callback, and external API instructions that do not fit the stated local utility purpose.

Mitigation: Prefer local encoding and conversion commands, and use API keys, callback_url values, or remote API/curl flows only after confirming the endpoint and data-sharing intent.

Risk: JWTs, private API responses, and other encoded inputs can contain secrets even when the operation is only decoding or format conversion.

Mitigation: Do not process real secrets, JWTs, private API responses, or sensitive payloads through remote callback paths without separate confirmation.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON-shaped examples and local command-line workflows for encoding, decoding, hashing, and conversion tasks.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
