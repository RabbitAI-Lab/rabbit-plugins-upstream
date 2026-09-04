## Description:

Coda API integration with managed OAuth for reading, creating, updating, and deleting Coda docs, pages, tables, rows, formulas, controls, permissions, and analytics through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to a Coda account through Maton, inspect Coda resources, and perform user-approved changes to docs, pages, tables, rows, permissions, formulas, controls, and analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Coda API access can modify docs, rows, permissions, sharing settings, analytics, and connected account state.

Mitigation: Default to read and list operations; require explicit user confirmation with resource identifiers and payload details before any write, delete, sharing, ACL, analytics, or connection change.

Risk: Maton or Coda credentials could be exposed if API keys or provider-issued tokens are printed, persisted, or passed through command lines.

Mitigation: Prefer OAuth through the Maton CLI and operating system credential store; never print, log, persist, or transmit credentials outside the intended Maton API host, and revoke unused connections.

Risk: Coda content returned by the API can include untrusted instructions or data that might influence follow-up actions.

Mitigation: Treat API responses as data, validate endpoint and recipient choices independently, and do not execute or interpolate returned content into shell commands.

## Reference(s):

- [ClawHub Coda skill page](https://clawhub.ai/byungkyu/skills/coda-api)
- [Maton homepage](https://maton.ai)
- [Coda API Documentation](https://coda.io/developers/apis/v1)
- [Coda API Postman Collection](https://www.postman.com/codaio/coda-workspace/collection/0vy7uxn/coda-api)
- [Coda API Python Library](https://codaio.readthedocs.io/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Community](https://community.maton.ai/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and Python or JavaScript code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may lead an agent to make Coda API calls through Maton; write, delete, sharing, ACL, analytics, and connection changes require explicit user confirmation.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata; artifact metadata lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
