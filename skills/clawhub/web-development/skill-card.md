## Description:

Guides implementation, debugging, deployment, and browser validation of web frontends, including React, Vue, Vite, and CloudBase integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to build and repair web frontends, integrate CloudBase when needed, and validate affected user flows in a browser.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication examples may allow a protected route to accept any supplied token as a valid login.

Mitigation: Verify tokens on the server before granting access; do not copy the example's client-set session cookie into production without safer session handling.

## Reference(s):

- [ClawHub web-development release](https://clawhub.ai/binggg/skills/web-development)
- [Framework guidance](frameworks.md)
- [Browser validation guidance](browser-testing.md)
- [CloudBase integration documentation](https://docs.cloudbase.net/integration/introduce.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include browser validation results and deployment steps.]

## Skill Version(s):

1.27.74 (source: ClawHub release; bundled frontmatter says 2.35.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
