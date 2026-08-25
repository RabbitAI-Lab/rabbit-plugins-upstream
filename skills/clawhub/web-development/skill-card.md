## Description:

Use when users need to implement, integrate, debug, build, deploy, or validate a Web frontend after the product direction is already clear, especially for React, Vue, Vite, browser flows, or CloudBase Web integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement, integrate, debug, build, deploy, and validate Web frontends and static sites, especially React, Vue, Vite, browser validation, and CloudBase Web integration work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication examples or generated code could leave protected Web routes without real server-side token validation.

Mitigation: Review authentication code before production use and require server-side token validation for protected routes.

Risk: Token storage patterns may be insecure if copied directly into production code.

Mitigation: Use secure cookie settings and review token handling before deployment.

Risk: CloudBase deployment or hosting changes can affect public routing and availability.

Mitigation: Require explicit user approval before CloudBase deployment or hosting changes and verify routing after deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/web-development)
- [CloudBase integration documentation](https://docs.cloudbase.net/integration/introduce/index.md)
- [Browser validation guidance](artifact/browser-testing.md)
- [Framework guidance](artifact/frameworks.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is scoped to Web frontend work and may include validation steps, browser-check summaries, CloudBase configuration, and deployment instructions.]

## Skill Version(s):

1.27.40 (source: server release metadata; artifact frontmatter reports 2.32.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
