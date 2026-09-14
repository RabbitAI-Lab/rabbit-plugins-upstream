## Description:

Use when users need to implement, integrate, debug, build, deploy, or validate a Web frontend after the product direction is already clear, especially for React, Vue, Vite, browser flows, or CloudBase Web integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement, debug, build, deploy, and validate web frontends or static sites, especially React, Vue, Vite, browser flows, and CloudBase Web integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may copy unsafe CloudBase authentication examples into production applications.

Mitigation: Review authentication code before reuse; use server-side token verification and server-set HttpOnly, Secure, SameSite cookies or another secure session pattern.

Risk: Credential and SDK configuration examples may lead to exposed secrets or unpinned dependencies if copied directly.

Mitigation: Avoid exposing secret keys through NEXT_PUBLIC variables and pin SDK versions for deployed apps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/web-development)
- [CloudBase integration documentation](https://docs.cloudbase.net/integration/introduce.md)
- [Browser validation guide](artifact/browser-testing.md)
- [Framework guidance](artifact/frameworks.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with inline code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include implementation guidance, validation steps, browser-check instructions, and CloudBase configuration guidance.]

## Skill Version(s):

1.27.52 (source: server release metadata; artifact frontmatter reports 2.34.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
