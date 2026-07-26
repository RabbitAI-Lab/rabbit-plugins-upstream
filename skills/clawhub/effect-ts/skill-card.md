## Description: <br>
Comprehensive Effect-TS development guide for TypeScript, focused on Effect v4 with full v3 support for existing codebases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and engineers use this skill to build, debug, review, migrate, and generate Effect-TS code while matching the project's Effect v3 or v4 API surface. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Effect v4 is beta and APIs may change, so generated code can become stale or mix v3 and v4 patterns. <br>
Mitigation: Check the installed Effect version and verify APIs against current Effect sources before relying on generated code. <br>
Risk: Examples may involve network, database, child-process, upload, worker-thread, or OpenAI-provider behavior. <br>
Mitigation: Run those examples only when intentional for the project, and provide OPENAI_API_KEY only for explicit Effect AI usage. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/effect-ts) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/tenequm) <br>
- [Clawdis Homepage](https://github.com/tenequm/skills/tree/main/skills/effect-ts) <br>
- [Effect v4 Source and Migration Guides](https://github.com/Effect-TS/effect-smol) <br>
- [Effect v4 LLM Guide](https://github.com/Effect-TS/effect-smol/blob/main/LLMS.md) <br>
- [Effect v3 Stable Docs](https://effect.website/docs) <br>
- [Effect LLM Topic Index](https://effect.website/llms.txt) <br>
- [Effect Full LLM Docs](https://effect.website/llms-full.txt) <br>
- [Effect API List](https://tim-smart.github.io/effect-io-ai/) <br>
- [LLM Corrections Reference](references/llm-corrections.md) <br>
- [Migration v4 Reference](references/migration-v4.md) <br>
- [Core Patterns Reference](references/core-patterns.md) <br>
- [Concurrency Reference](references/concurrency.md) <br>
- [Dependency Injection Reference](references/dependency-injection.md) <br>
- [Resource Management Reference](references/resource-management.md) <br>
- [Schema Reference](references/schema.md) <br>
- [HTTP Reference](references/http.md) <br>
- [Effect AI Reference](references/effect-ai.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with TypeScript and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference OPENAI_API_KEY for optional Effect AI examples.] <br>

## Skill Version(s): <br>
0.6.2 (source: frontmatter, changelog, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
