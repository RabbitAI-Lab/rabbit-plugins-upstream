## Description:

Use when users need to implement, integrate, debug, build, deploy, or validate a Web frontend after the product direction is already clear, especially for React, Vue, Vite, browser flows, or CloudBase Web integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement, debug, build, deploy, and validate Web frontends and static sites, especially React, Vue, Vite, browser validation, routing, and CloudBase Web integration work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CloudBase authentication examples may be copied into production without real server-side token validation.

Mitigation: Require backend token validation or an equivalent trusted server-side session check before using generated auth code in production.

Risk: Generated examples may store bearer tokens in JavaScript-readable cookies.

Mitigation: Prefer HttpOnly, Secure, SameSite server-set session cookies or an equivalent backend session pattern.

Risk: Credentialed CORS examples may be deployed with an overly broad origin policy.

Mitigation: Configure credentialed CORS with an explicit trusted-origin allowlist before deployment.

## Reference(s):

- [Web Development skill page](https://clawhub.ai/binggg/skills/web-development)
- [Framework Guidance](frameworks.md)
- [Browser Validation](browser-testing.md)
- [CloudBase integration documentation](https://docs.cloudbase.net/integration/introduce.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code blocks, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include browser-validation checklists, build and deployment steps, and CloudBase integration guidance.]

## Skill Version(s):

1.27.54 (source: server release metadata; artifact frontmatter reports 2.34.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
