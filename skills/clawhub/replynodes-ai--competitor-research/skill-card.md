## Description:

Builds sourced, read-only competitor comparisons from verified public company domains, app listings, and community signals while flagging unknowns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, product teams, and developers use this skill to compare named competitors, identify alternatives, and assess market positioning using cited public evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Competitor names, domains, URLs, and research queries may be sent to ReplyNodes services.

Mitigation: Use anonymous routes for public research where possible and avoid submitting confidential information.

Risk: An exposed API key could allow unauthorized use of authenticated routes.

Mitigation: Keep the API key in a secret store; never paste it into chat or commit it.

Risk: Running an unreviewed installation command could execute unexpected code.

Mitigation: Inspect or pin the installation source before running the npx example.

## Reference(s):

- [ReplyNodes capabilities and OpenAPI](https://api.replynodes.com/v1/capabilities)
- [ReplyNodes authentication](https://docs.replynodes.com/docs/auth)
- [ReplyNodes MCP endpoint](https://mcp.replynodes.com/mcp)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown comparison with source citations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source URLs and retrieval times; flags uncertain or unsupported claims.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
