## Description: <br>
CloudBase guides agents through developing, deploying, debugging, and reviewing CloudBase projects across web, WeChat Mini Program, backend, database, storage, auth, AI model, and operations workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to select CloudBase-specific workflows, configure resources, implement app features, and review code for common CloudBase pitfalls before deployment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can steer agents toward high-impact CloudBase actions such as environment changes, permission updates, deployments, API key creation, public endpoint exposure, or local directory deletion. <br>
Mitigation: Install it only for intentional CloudBase work and require explicit approval before MCP or cloud actions that change resources or expose services. <br>
Risk: Auth, JWT, CORS, public-access, service-role, logging, telemetry, and external LLM examples may be unsafe or under-scoped if copied directly into production. <br>
Mitigation: Treat these examples as drafts and complete production security review before deployment. <br>


## Reference(s): <br>
- [ClawHub Cloudbase Skill Page](https://clawhub.ai/binggg/skills/cloudbase) <br>
- [CloudBase Development Guidelines](artifact/SKILL.md) <br>
- [CloudBase MCP Setup](artifact/references/mcp-setup.md) <br>
- [CloudBase Deployment Workflow](artifact/references/deployment-workflow.md) <br>
- [CloudBase Code Review Rules Index](artifact/references/cloudbase-code-review/references/RULES_INDEX.md) <br>
- [CloudBase Change Safety Protocol](artifact/references/cloudbase-platform/references/protocols/change-safety-protocol.md) <br>
- [CloudBase Deployment Gate](artifact/references/cloudbase-platform/references/protocols/deployment-gate.md) <br>
- [CloudBase HTTP API Guide](artifact/references/http-api/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with code snippets, command examples, configuration steps, and review checklists.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routes to topic-specific reference skills and includes approval gates for high-impact cloud actions.] <br>

## Skill Version(s): <br>
1.92.27 (source: server release metadata; artifact frontmatter version: 2.25.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
