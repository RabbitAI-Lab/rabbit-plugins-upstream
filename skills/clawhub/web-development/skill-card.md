## Description:

Use when users need to implement, integrate, debug, build, deploy, or validate a Web frontend after the product direction is already clear, especially for React, Vue, Vite, browser flows, or CloudBase Web integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to implement, debug, build, deploy, and validate web frontends and static sites, especially React, Vue, Vite, browser flows, and CloudBase Web integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Insecure authentication examples could lead an agent to create applications with exposed tokens or bypassed auth checks.

Mitigation: Review and correct generated authentication code before use in real applications, especially token handling and server-side verification.

Risk: Frontend or routing changes may be treated as complete without runtime validation.

Mitigation: Run the relevant build, type, lint, and browser-flow checks for affected routes, forms, auth, and CloudBase SDK behavior before release.

## Reference(s):

- [Framework Guidance](artifact/frameworks.md)
- [Browser Validation](artifact/browser-testing.md)
- [CloudBase Integration Documentation](https://docs.cloudbase.net/integration/introduce/index.md)
- [CloudBase Web SDK CDN](https://static.cloudbase.net/cloudbase-js-sdk/latest/cloudbase.full.js)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline code blocks and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include browser validation checklists, framework-specific implementation guidance, and CloudBase configuration steps.]

## Skill Version(s):

1.27.30 (source: server release metadata; artifact frontmatter reports 2.25.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
