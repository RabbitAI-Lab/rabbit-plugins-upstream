## Description:

Encoding & Formats helps agents encode, decode, inspect, and convert data across Base64, URL encoding, hex, Unicode, JWT, hashing, checksum, JSON, MessagePack, and protobuf wire formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gitgoodordietrying](https://clawhub.ai/user/gitgoodordietrying)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill when they need command-line examples and code snippets to encode, decode, inspect, hash, checksum, or convert data formats during API, configuration, or file analysis work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A reusable quick decode script example is unsafe with crafted URL-decoding input.

Mitigation: Review or replace the script before use, and pass URL-decoding input to Python through argv or stdin instead of interpolating it into Python source.

Risk: Decoded secrets or JWT contents may be exposed through agent output, logs, or shared transcripts.

Mitigation: Avoid decoding real secrets or JWTs unless the user controls where the decoded output goes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gitgoodordietrying/skills/encoding-formats)
- [Publisher Profile](https://clawhub.ai/user/gitgoodordietrying)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local CLI tools including base64, python3, openssl, and xxd.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
