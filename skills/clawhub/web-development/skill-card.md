## Description:

Use when users need to implement, integrate, debug, build, deploy, or validate a Web frontend after the product direction is already clear, especially for React, Vue, Vite, browser flows, or CloudBase Web integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to execute web frontend work after product direction is clear, including React, Vue, Vite, routing, browser validation, and CloudBase Web integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication examples may lead an agent to build server-side protected routes that accept unverified tokens.

Mitigation: Review and correct authentication snippets before production use; require real CloudBase token validation, fail closed when validation is unavailable, and use secure session storage and cookie practices.

Risk: Frontend implementation guidance can result in incomplete validation if browser-visible flows are not exercised.

Mitigation: Run the relevant typecheck, lint, build, and browser validation flows before treating generated web changes as complete.

Risk: CloudBase static hosting with history-mode SPA routing can return 404 or NoSuchKey on direct sub-route visits.

Mitigation: Configure the static hosting error document to index.html or use hash routing when rewrite support is absent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/web-development)
- [Framework guidance](artifact/frameworks.md)
- [Browser validation guidance](artifact/browser-testing.md)
- [CloudBase integration documentation](https://docs.cloudbase.net/integration/introduce/index.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for agent-facing web engineering workflows and should be verified with build, lint, typecheck, and browser checks when applicable.]

## Skill Version(s):

1.27.33 (source: server release metadata; artifact frontmatter reports 2.28.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
