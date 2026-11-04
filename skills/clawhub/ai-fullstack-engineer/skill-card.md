## Description:

An AI full-stack engineering toolkit that guides API, database, backend, frontend, performance, and browser work through an integrated application delivery workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skills-repo](https://clawhub.ai/user/skills-repo)

### License/Terms of Use:

MIT

## Use Case:

Developers and small teams use this skill to plan and build web applications across API design, data modeling, backend and frontend implementation, browser debugging, and delivery workflows. It also provides scaffolding and OpenAPI type generation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The database template uses unsafe default credentials and exposes a database port.

Mitigation: Replace the password, use a restricted application database account, and remove the published port or bind it to localhost before running the template.

Risk: Browser workflows may send private page content to an AI provider without making that data flow clear.

Mitigation: Use an approved model provider and a dedicated test browser; keep passwords out of prompts and exclude sensitive pages from screenshots.

Risk: External tools used by the workflows may change or include code outside this review.

Mitigation: Pin and verify external tools before execution.

## Reference(s):

- [Full-Stack Workflow](references/fullstack-workflow.md)
- [Backend Playbook](references/backend-playbook.md)
- [Frontend Playbook](references/frontend-playbook.md)
- [Next.js App Router Playbook](references/nextjs-app-router-playbook.md)
- [Tailwind Audit Playbook](references/tailwind-audit-playbook.md)
- [Multi-Agent Orchestration Playbook](references/multi-agent-orchestration-playbook.md)
- [Browser Operations Playbook](skills/browser-ops/references/browser-ops-playbook.md)
- [Playwright MCP](https://github.com/microsoft/playwright-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Code, Markdown, Shell commands, Configuration files]

**Output Format:** [Markdown guidance, code snippets, shell commands, and generated project or configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include scaffold files and TypeScript types generated from an OpenAPI specification.]

## Skill Version(s):

1.0.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
