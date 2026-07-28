## Description: <br>
Cloudbase helps agents plan, build, deploy, debug, and review Tencent CloudBase applications across Web, WeChat Mini Program, mobile, Cloud Functions, Cloud Run, databases, storage, auth, AI models, and AI agent workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create and maintain CloudBase applications, including backend resources, authentication, data storage, deployment, AI model integration, and post-implementation review. It is intended for CloudBase projects and explicitly excludes unrelated frontend-only or self-hosted backend work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide real CloudBase cloud changes, including public access, ACL, CORS, auth, deployment, paid-plan, or destructive local-file changes. <br>
Mitigation: Require explicit user confirmation before sensitive, paid, public, or destructive operations and scope plugin installation to the intended IDE or project. <br>
Risk: Some auth or logging examples may be under-scoped for production use. <br>
Mitigation: Harden token validation, origin allowlists, data minimization, and redaction before copying examples into production workflows. <br>


## Reference(s): <br>
- [ClawHub cloudbase release page](https://clawhub.ai/binggg/skills/cloudbase) <br>
- [CloudBase main skill](artifact/SKILL.md) <br>
- [CloudBase scenarios](artifact/references/scenarios.md) <br>
- [Deployment workflow](artifact/references/deployment-workflow.md) <br>
- [CloudBase MCP setup](artifact/references/mcp-setup.md) <br>
- [CloudBase code review](artifact/references/cloudbase-code-review/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with code blocks, configuration snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose CloudBase MCP or CLI operations, deployment steps, security-rule changes, and review findings that require user confirmation before sensitive or destructive actions.] <br>

## Skill Version(s): <br>
1.92.29 (source: server release metadata, created 2026-07-28; artifact frontmatter version is 2.25.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
