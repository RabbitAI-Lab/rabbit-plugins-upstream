## Description:

Use when users need to implement, integrate, debug, build, deploy, or validate a Web frontend after the product direction is already clear, especially for React, Vue, Vite, browser flows, or CloudBase Web integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement, debug, validate, and deploy browser-based Web frontends and static sites. It is especially oriented toward React, Vue, Vite, browser-flow checks, and CloudBase Web integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication examples could lead an agent to implement auth bypasses or expose session tokens.

Mitigation: Review and correct auth examples before allowing reuse in an application; require server-side token or session verification and avoid JavaScript-readable bearer-token cookies.

Risk: Credentialed cross-origin requests may be configured with overly broad trusted origins.

Mitigation: Use explicit trusted CORS origins for credentialed requests instead of permissive wildcard origins.

## Reference(s):

- [CloudBase integration documentation](https://docs.cloudbase.net/integration/introduce/index.md)
- [ClawHub skill page](https://clawhub.ai/binggg/skills/web-development)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline code blocks and implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include validation steps, browser-check notes, routing guidance, and CloudBase integration configuration.]

## Skill Version(s):

1.27.47 (source: ClawHub release evidence; artifact frontmatter reports 2.33.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
