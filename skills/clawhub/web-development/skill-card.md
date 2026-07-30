## Description: <br>
Use when users need to implement, integrate, debug, build, deploy, or validate a Web frontend after the product direction is already clear, especially for React, Vue, Vite, browser flows, or CloudBase Web integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to implement, debug, build, deploy, and validate Web frontends, especially React, Vue, Vite, browser flows, and CloudBase Web integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authentication examples could lead an agent to create weak login protection if copied directly into production code. <br>
Mitigation: Require real server-side token validation and prefer safer server-set HttpOnly cookies when browser-readable access-token cookies are not necessary. <br>
Risk: CORS examples could produce overly permissive deployed applications. <br>
Mitigation: Use explicit trusted CORS origins for deployed apps and review authentication examples before relying on the generated code. <br>


## Reference(s): <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Browser validation workflow](artifact/browser-testing.md) <br>
- [Framework guidance](artifact/frameworks.md) <br>
- [ClawHub skill page](https://clawhub.ai/binggg/skills/web-development) <br>
- [CloudBase integration documentation](https://docs.cloudbase.net/integration/introduce/index.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline code and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to run build, typecheck, lint, test, browser validation, or CloudBase deployment checks when applicable.] <br>

## Skill Version(s): <br>
1.27.20 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
