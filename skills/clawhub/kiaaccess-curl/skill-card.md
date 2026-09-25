## Description:

Query and command a Kia vehicle directly with curl against the Kia Owners API (api.owners.kia.com), without running the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and technically comfortable Kia owners use this skill for one-off shell-based vehicle status checks, location reads, EV charging checks, and remote commands such as lock, unlock, climate start, and charging control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shell examples handle Kia account credentials, refresh tokens, vehicle location, and remote vehicle controls, and the security evidence notes use of predictable temporary files.

Mitigation: Install only for an authorized vehicle owner, run commands in a private shell environment, replace fixed /tmp paths with an owner-only mktemp directory, and treat the saved rmtoken like a password.

Risk: Remote commands affect a real vehicle, while accepted API responses do not by themselves prove the command completed.

Mitigation: Review each command before execution and verify results with a follow-up vehicle status read rather than relying only on HTTP 200 or statusCode 0.

Risk: Repeated rejected login attempts can trigger account protections that break shell-based login.

Mitigation: Do not loop failed authentication attempts; correct the credential or account input before trying again.

## Reference(s):

- [Ready-to-run requests](artifact/references/requests.md)
- [Kia Owners API endpoint](https://api.owners.kia.com/apigw/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and jq code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command snippets and operational guidance for direct curl calls; it does not run the API calls by itself.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
