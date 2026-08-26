## Description:

Effect-TS development guide for TypeScript, focused on Effect v4 (the recommended default) with full v3 (stable) support for existing codebases. Use when building, debugging, reviewing, or generating Effect code across its error, concurrency, service, streaming, schema, and platform layers, or whenever code imports from 'effect', '@effect/platform', '@effect/ai', or '@effect/sql'. Includes exhaustive wrong-vs-correct API tables to prevent hallucinated Effect code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build, migrate, debug, review, and generate TypeScript code with Effect, including typed errors, concurrency, dependency injection, streams, schema validation, HTTP, SQL, and observability patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is documentation-only, but code examples for multipart uploads can lead to unsafe file handling if copied without local constraints.

Mitigation: Add file-size limits, secure temporary storage, deletion or retention policy, and streaming behavior for large uploads when adapting upload examples.

Risk: Effect v4 is beta and APIs may change, which can make generated guidance stale for a user's installed version.

Mitigation: Detect the installed Effect version before writing code, pin exact v4 beta versions for new projects, and verify APIs against the linked Effect documentation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/effect-ts)
- [Publisher profile](https://clawhub.ai/user/tenequm)
- [ClawHub metadata homepage](https://github.com/tenequm/skills/tree/main/skills/effect-ts)
- [Effect v4 source and migration guides](https://github.com/Effect-TS/effect-smol)
- [Effect v4 LLM guide](https://github.com/Effect-TS/effect-smol/blob/main/LLMS.md)
- [Effect v3 documentation](https://effect.website/docs)
- [Effect LLM topic index](https://effect.website/llms.txt)
- [Effect full LLM documentation](https://effect.website/llms-full.txt)
- [Effect API reference for AI assistants](https://tim-smart.github.io/effect-io-ai/)
- [Error modeling reference](references/error-modeling.md)
- [Concurrency reference](references/concurrency.md)
- [Dependency injection reference](references/dependency-injection.md)
- [HTTP reference](references/http.md)
- [LLM corrections reference](references/llm-corrections.md)
- [Migration to Effect v4 reference](references/migration-v4.md)
- [Resource management reference](references/resource-management.md)
- [Schema reference](references/schema.md)
- [Streams reference](references/streams.md)
- [Testing reference](references/testing.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with TypeScript and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include version-specific Effect v3 or v4 guidance based on the user's installed package version.]

## Skill Version(s):

0.6.4 (source: frontmatter, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
