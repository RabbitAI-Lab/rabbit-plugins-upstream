## Description:

Fast path for a minimal CloudBase Web and database demo using CloudBase browser SDK CRUD, MCP-managed schema, preview-first workflow, and cloud functions only when secrets, scheduled work, or logic beyond database rules require them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to build quick CloudBase-backed Web demos such as message boards, Todo, Notes, and Kanban apps. It guides the agent toward browser SDK CRUD, minimal database setup, local preview, and avoiding unnecessary cloud functions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may perform CloudBase schema/admin operations and browser SDK CRUD while building demos.

Mitigation: Review proposed CloudBase MCP or CLI actions, database permissions, and generated CRUD code before applying them.

Risk: The skill is scoped to preview-first demo apps rather than production multi-service backends or workloads that need secrets.

Mitigation: Use separate production backend guidance for payments, callbacks, cron jobs, WebSockets, third-party secrets, or server-side business logic.

Risk: Server-resolved import provenance is unavailable for this release.

Mitigation: Treat source origin as unverified and review the packaged SKILL.md before deployment.

## Reference(s):

- [Tencent CloudBase Minimal Web BaaS Demo on ClawHub](https://clawhub.ai/binggg/skills/minimal-web-baas-demo)
- [WorkBuddy CLI Hooks](https://www.workbuddy.ai/docs/cli/hooks)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CloudBase MCP or CLI schema/admin steps, browser SDK CRUD implementation guidance, and preview-first workflow instructions.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
