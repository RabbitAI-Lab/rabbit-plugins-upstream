## Description:

Build generative UI with OpenUI across LLM providers and backend languages; scaffold, integrate, and validate projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add OpenUI generative UI workflows to applications, including project detection, scaffolding, component library setup, backend integration, prompt generation, and validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Package installation and npx commands can modify a project or pull new dependencies.

Mitigation: Review package names, versions, and generated commands before execution.

Risk: Chat content may be sent to an external model provider during generated integrations.

Mitigation: Use approved providers and tell end users when their chat content is sent outside the application.

Risk: Provider API keys and backend access settings can be exposed or over-permissive if configured casually.

Mitigation: Keep provider keys in environment variables or secret management and restrict cross-origin access to intended frontends.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/othmanadi/skills/openui-forge)
- [Server-Resolved Source Repository](https://github.com/OthmanAdi/openui-forge/tree/main/skills/openui-forge)
- [OpenUI Full LLM Documentation](https://www.openui.com/llms-full.txt)
- [OpenUI LLM Documentation Index](https://www.openui.com/llms.txt)
- [Adapter Matrix](references/adapter-matrix.md)
- [Backend Patterns](references/backend-patterns.md)
- [Component Patterns](references/component-patterns.md)
- [OpenUI Lang Specification](references/openui-lang-spec.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code blocks, shell commands, configuration snippets, and file templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update OpenUI frontend and backend files and run validation scripts when used by an agent.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence; artifact frontmatter reports 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
