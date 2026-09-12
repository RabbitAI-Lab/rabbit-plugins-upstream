## Description:

Effect-TS guide for TypeScript, v4 default with v3 support. Use when writing, debugging, or reviewing Effect code across errors, concurrency, services, streams, and schema, or when code imports from 'effect' or any '@effect/*' package.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to write, debug, review, and migrate Effect TypeScript code with version-aware v3 and v4 guidance. It helps agents produce typed errors, dependency injection, concurrency, streams, schema, observability, HTTP, SQL, testing, and migration guidance without relying on commonly hallucinated APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Effect v4 examples target beta APIs that may change over time.

Mitigation: Pin exact package versions, commit lockfiles, and verify generated APIs against the referenced Effect documentation before adopting code.

Risk: Multipart upload examples can introduce file-handling risk if copied without limits and cleanup.

Mitigation: Apply upload size limits, schema validation, streaming behavior, and resource cleanup when implementing file uploads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/effect-ts)
- [Project homepage](https://github.com/tenequm/skills/tree/main/skills/effect-ts)
- [Effect v4 source and migration guides](https://github.com/Effect-TS/effect-smol)
- [Effect v4 LLM guide](https://github.com/Effect-TS/effect-smol/blob/main/LLMS.md)
- [Effect v3 documentation](https://effect.website/docs)
- [Effect LLM topic index](https://effect.website/llms.txt)
- [Effect full LLM documentation](https://effect.website/llms-full.txt)
- [Effect API reference](https://tim-smart.github.io/effect-io-ai/)
- [LLM corrections reference](references/llm-corrections.md)
- [Effect v4 migration reference](references/migration-v4.md)
- [Core patterns reference](references/core-patterns.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with TypeScript and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include version-specific v3 or v4 guidance, API corrections, and environment variable notes such as OPENAI_API_KEY for optional Effect AI examples.]

## Skill Version(s):

0.6.5 (source: evidence release, frontmatter, metadata, and CHANGELOG; released 2026-09-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
