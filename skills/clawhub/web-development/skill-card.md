## Description: <br>
Use when users need to implement, integrate, debug, build, deploy, or validate a Web frontend after the product direction is already clear, especially for React, Vue, Vite, browser flows, or CloudBase Web integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to implement, debug, build, deploy, and validate web frontends, especially React, Vue, Vite, routing, browser validation, and CloudBase Web integration work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authentication examples may lead an agent toward weak access control if copied into production without review. <br>
Mitigation: Review authentication snippets before production use, require real server-side token validation, and avoid client-readable access-token cookies where possible. <br>
Risk: CloudBase deployment guidance can be applied with an implicit or incorrect region. <br>
Mitigation: Select an explicit CloudBase region that matches deployment and compliance needs before using the skill for production work. <br>
Risk: Frontend changes may be declared complete without browser-level verification. <br>
Mitigation: Run the skill's static checks and browser-validation workflow for changes affecting routing, rendering, forms, authentication, or async UI. <br>


## Reference(s): <br>
- [CloudBase main skill entry](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/SKILL.md) <br>
- [Web Development raw source](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/web-development/SKILL.md) <br>
- [Browser validation playbook](browser-testing.md) <br>
- [Framework guidance](frameworks.md) <br>
- [CloudBase integration documentation](https://docs.cloudbase.net/integration/introduce/index.md) <br>
- [CloudBase Web SDK CDN](https://static.cloudbase.net/cloudbase-js-sdk/latest/cloudbase.full.js) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code snippets, shell commands, configuration examples, and validation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to run build, lint, test, deployment, and browser-validation checks when applicable.] <br>

## Skill Version(s): <br>
1.27.17 (source: ClawHub release metadata; artifact frontmatter declares 2.24.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
