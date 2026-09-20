## Description:

Use when users need to implement, integrate, debug, build, deploy, or validate a Web frontend after the product direction is already clear, especially for React, Vue, Vite, browser flows, or CloudBase Web integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement and validate web frontend work in React, Vue, Vite, browser flows, and CloudBase Web integrations after product direction is already clear.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication examples include unsafe token handling and should not be copied directly into production application code.

Mitigation: Review and correct authentication examples before use; prefer server-side session or token verification and avoid storing bearer access tokens in JavaScript-set cookies.

Risk: Frontend changes can appear correct from code review while still failing in browser routing, forms, auth, or async flows.

Mitigation: Run the skill's static checks and browser validation workflow for affected user-visible flows before treating generated changes as complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/web-development)
- [Browser Validation](artifact/browser-testing.md)
- [Framework Guidance](artifact/frameworks.md)
- [CloudBase integration documentation](https://docs.cloudbase.net/integration/introduce.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include validation notes, browser-check summaries, and configuration guidance.]

## Skill Version(s):

1.27.55 (source: server release metadata; artifact frontmatter lists 2.34.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
