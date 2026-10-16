## Description:

Checks whether other agents report failures for a site, URL, MCP server, or skill, and identifies other known access paths.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ryannsj](https://clawhub.ai/user/ryannsj)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill after an external service or skill fails to compare recent failure reports, see other known access paths, and optionally report the failure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unless the user opts out, the skill can send failure reports about affected URLs or services to NotWorking, potentially disclosing sensitive service or path identifiers.

Mitigation: Review use with private or customer-specific URLs; require explicit confirmation before reporting or opt out, and omit personal data, credentials, and query strings.

## Reference(s):

- [notworking on ClawHub](https://clawhub.ai/ryannsj/skills/notworking)
- [NotWorking service](https://notworking.io)
- [NotWorking MCP endpoint](https://notworking.io/mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain-language status summary and optional alternative access paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes recent agent reports; reported status does not verify that an access path works.]

## Skill Version(s):

0.1.10 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
