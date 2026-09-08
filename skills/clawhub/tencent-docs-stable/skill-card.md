## Description:

Stable write path for Tencent Docs when the MCP connector fails, covering failure classification, credential self-check, one retry, direct JSON-RPC fallback, chunking, and read-back verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to recover failed Tencent Docs write, upload, push, or paragraph insertion workflows. It is intended for connector failures such as no_token, timeouts, validation errors, rate limits, or long-content truncation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document content may be sent through a direct JSON-RPC fallback using configured Tencent Docs or MCP credentials when the normal connector fails.

Mitigation: Use the fallback only with a trusted MCP gateway configuration and content appropriate for Tencent Docs; resolve endpoints and credentials from trusted runtime configuration.

Risk: Credential values could be exposed if token self-check output includes secrets.

Mitigation: Verify only that the credential source exists and is non-empty; never print, log, or embed token values.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Short Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the failure class, remediation used, verification result, and document link.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
