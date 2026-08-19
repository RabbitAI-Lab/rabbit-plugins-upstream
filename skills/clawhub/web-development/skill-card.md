## Description:

Use when users need to implement, integrate, debug, build, deploy, or validate a Web frontend after the product direction is already clear, especially for React, Vue, Vite, browser flows, or CloudBase Web integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement, debug, build, deploy, and validate web frontends once product direction is clear, especially for React, Vue, Vite, browser workflows, and CloudBase Web integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The NestJS protected-route example may lead agents to generate auth code that checks only token presence instead of validating CloudBase tokens.

Mitigation: Require real server-side CloudBase token validation, fail closed on validation errors, and add tests for missing, malformed, expired, and forged tokens before using generated auth code.

## Reference(s):

- [Framework Guidance](frameworks.md)
- [Browser Validation](browser-testing.md)
- [CloudBase Integration Documentation](https://docs.cloudbase.net/integration/introduce/index.md)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill that guides agent behavior; it does not execute code by itself.]

## Skill Version(s):

1.27.34 (source: server release metadata; artifact frontmatter reports 2.28.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
