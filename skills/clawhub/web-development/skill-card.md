## Description:

Use when users need to implement, integrate, debug, build, deploy, or validate a Web frontend after the product direction is already clear, especially for React, Vue, Vite, browser flows, or CloudBase Web integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement, debug, build, deploy, and validate Web frontends or static sites, especially when working with React, Vue, Vite, browser workflows, or CloudBase Web integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication examples may lead an agent to create protected routes that accept fake tokens or rely on JavaScript-readable bearer-token cookies.

Mitigation: Require real server-side token verification before any protected operation and review or patch authentication examples before production use.

Risk: Deployment and tooling guidance can change CloudBase resources.

Mitigation: Require explicit environment confirmation, build verification, and deployment-gate checks before applying CloudBase hosting or deployment changes.

## Reference(s):

- [CloudBase integration documentation](https://docs.cloudbase.net/integration/introduce.md)
- [CloudBase JavaScript SDK CDN](https://static.cloudbase.net/cloudbase-js-sdk/latest/cloudbase.full.js)
- [Browser Validation](artifact/browser-testing.md)
- [Framework Guidance](artifact/frameworks.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code blocks and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include implementation steps, verification checks, browser validation guidance, and CloudBase configuration notes.]

## Skill Version(s):

1.27.56 (source: server release metadata; artifact frontmatter lists 2.34.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
