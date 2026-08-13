## Description:

Effect-TS development guide for TypeScript that helps agents build, debug, review, and generate Effect v4 and v3 code while avoiding incorrect framework APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to guide agent work on TypeScript projects that use Effect, including version-aware code generation, debugging, review, migration, and framework-specific patterns. It is especially useful when code imports from 'effect', '@effect/platform', '@effect/ai', or '@effect/sql'.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated examples may include network APIs, environment variables, databases, child processes, or background fibers when the user's task calls for those Effect features.

Mitigation: Review generated code before running it in sensitive projects, and check environment-variable and process-spawning behavior before execution.

Risk: Effect v4 is beta software and APIs can change between beta releases.

Mitigation: Pin an exact Effect version and verify generated APIs against the skill's version-specific references before adopting code.

Risk: Agents may mix Effect v3 and v4 APIs or generate hallucinated Effect APIs.

Mitigation: Use the skill's correction tables and primary documentation references to verify imports, services, error handling, and concurrency APIs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/effect-ts)
- [ClawHub publisher profile](https://clawhub.ai/user/tenequm)
- [OpenClaw homepage](https://github.com/tenequm/skills/tree/main/skills/effect-ts)
- [Effect v4 source and migration guides](https://github.com/Effect-TS/effect-smol)
- [Effect v4 LLM guide](https://github.com/Effect-TS/effect-smol/blob/main/LLMS.md)
- [Effect v3 documentation](https://effect.website/docs)
- [Effect LLM topic index](https://effect.website/llms.txt)
- [Effect full LLM documentation](https://effect.website/llms-full.txt)
- [Effect API reference](https://tim-smart.github.io/effect-io-ai/)
- [LLM corrections reference](references/llm-corrections.md)
- [Effect v4 migration reference](references/migration-v4.md)
- [Core Effect patterns reference](references/core-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with TypeScript and shell command code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Version-sensitive guidance that should match the user's installed Effect version.]

## Skill Version(s):

0.6.3 (source: SKILL.md frontmatter, CHANGELOG, evidence release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
