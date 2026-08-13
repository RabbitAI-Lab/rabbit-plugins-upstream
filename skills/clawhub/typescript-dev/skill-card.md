## Description:

Builds full-stack TypeScript apps with Vite 8, React 19, Tailwind CSS v4, shadcn/ui, Biome, Vitest, and Hono, covering frontend build and dev workflows plus a Hono backend or edge API layer with type-safe RPC, validation, OpenAPI, testing, linting, formatting, and deployment guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill when configuring or maintaining full-stack TypeScript projects that combine Vite, React, Tailwind CSS, shadcn/ui, Biome, Vitest, and Hono. It provides stack-specific guidance, code examples, configuration patterns, shell commands, testing practices, and deployment notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-invoked commands such as shadcn add, biome check --write, migrations, and deployment examples can modify project files or publish code.

Mitigation: Review diffs after file-changing commands, use dry-run or diff modes where available, and require explicit user confirmation before deployment or publication commands.

Risk: The skill gives opinionated, version-targeted stack guidance that may not match an existing project's versions or constraints.

Mitigation: Confirm the project's installed versions and constraints before applying configuration changes, and consult the linked upstream documentation for version-specific behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/typescript-dev)
- [OpenClaw homepage](https://github.com/tenequm/skills/tree/main/skills/typescript-dev)
- [Vite reference](references/vite.md)
- [React reference](references/react.md)
- [TypeScript reference](references/typescript.md)
- [Tailwind CSS reference](references/tailwind.md)
- [shadcn/ui reference](references/shadcn.md)
- [Biome reference](references/biome.md)
- [Vitest reference](references/vitest.md)
- [Hono reference](references/hono.md)
- [Vite guide](https://vite.dev/guide/)
- [React Compiler](https://react.dev/learn/react-compiler)
- [TypeScript 6.0 announcement](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)
- [Tailwind CSS docs](https://tailwindcss.com/docs)
- [shadcn/ui docs](https://ui.shadcn.com/docs)
- [Biome docs](https://biomejs.dev/)
- [Hono docs](https://hono.dev/docs/)
- [Vitest guide](https://vitest.dev/guide/)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with inline TypeScript, JSON, CSS, and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Version-targeted guidance for a TypeScript web stack; no hidden execution behavior reported by security evidence.]

## Skill Version(s):

0.3.3 (source: frontmatter and changelog, released 2026-08-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
