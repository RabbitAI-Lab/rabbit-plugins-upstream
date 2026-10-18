## Description:

Guides agents through implementing, debugging, deploying, and validating React, Vue, Vite, and CloudBase Web frontends after the product direction is set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to build and troubleshoot Web frontends, verify browser flows, and integrate or deploy CloudBase Web features when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication examples may permit protected routes to accept unverified tokens.

Mitigation: Require real server-side token or session verification before returning protected data.

Risk: JavaScript-managed access-token cookies may expose tokens to client-side scripts.

Mitigation: Review and revise token storage before using the authentication examples; explicitly address the security tradeoffs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/binggg/skills/web-development)
- [Browser validation guide](artifact/browser-testing.md)
- [Framework guidance](artifact/frameworks.md)
- [CloudBase integration documentation](https://docs.cloudbase.net/integration/introduce.md)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown with code and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include build and browser-validation results.]

## Skill Version(s):

1.27.83 (source: ClawHub release metadata; artifact frontmatter lists 2.35.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
