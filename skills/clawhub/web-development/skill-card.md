## Description:

Guides agents through implementing, debugging, deploying, and validating web frontends, including React, Vue, Vite, browser flows, and CloudBase integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to make scoped frontend changes, integrate CloudBase when needed, and check user-visible flows in a browser.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication examples may allow fake tokens to access protected routes.

Mitigation: Do not use the protected-route or AuthGuard snippets as production authentication; validate tokens or sessions server-side before returning protected data or setting request.user.

## Reference(s):

- [ClawHub web-development skill release](https://clawhub.ai/binggg/skills/web-development)
- [CloudBase integration documentation](https://docs.cloudbase.net/integration/introduce.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include implementation changes and browser-validation results.]

## Skill Version(s):

1.27.67 (source: ClawHub release metadata; artifact frontmatter says 2.35.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
