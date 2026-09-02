## Description:

Helps API developers and platform teams generate, improve, and validate OpenAPI or Swagger documentation for REST APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, backend teams, developer-experience teams, and API maintainers use this skill to turn API documentation requests into practical OpenAPI or Swagger workflows, artifacts, checklists, analysis, code changes, and verification notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broader API or developer-experience prompts than intended because implicit invocation is enabled and trigger wording is loose.

Mitigation: Review whether invocation was intended before relying on the output, and narrow the trigger wording for deployments that need stricter activation boundaries.

Risk: OpenAPI or Swagger guidance can introduce incomplete schemas, inaccurate examples, or misleading validation advice if the source API behavior is underspecified.

Mitigation: Validate generated documentation against the actual API implementation, available tests, and documented success criteria before publishing.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [Openapi Docs Generator on ClawHub](https://clawhub.ai/kyro-ma/skills/openapi-docs-generator)
- [Ask HN: Why do we need MCP?](https://news.ycombinator.com/item?id=49488654)
- [Measure opportunity effectiveness across review and downstream outcomes](https://github.com/sgajbi/lotus-idea/issues/1156)
- [Make review feedback a governed offline opportunity-quality signal](https://github.com/sgajbi/lotus-idea/issues/1155)
- [program: reconstruct, simplify, and mechanically govern the repository](https://github.com/ListenCloser/listencloser/issues/634)
- [Hive Advisory Report](https://github.com/weavster-dev/weavster/issues/1)
- [Add HMAC signature verification for incoming webhooks](https://github.com/francovp/cabros-bot/issues/737)
- [roadmap: make the HTTP gateway a unified, operable multi-node product](https://github.com/majiayu000/litellm-rs/issues/1292)
- [HarmonyOS Developer Community](https://segmentfault.com/brand/harmonyos-next)
- [SegmentFault JavaScript](https://segmentfault.com/t/javascript)
- [SegmentFault TypeScript](https://segmentfault.com/t/typescript)
- [ONES R&D Management](https://ones.cn/?utm_term=ONES%C2%A0%E7%A0%94%E5%8F%91%E7%AE%A1%E7%90%86&utm_campaign=%E9%A6%96%E9%A1%B5%E6%A0%87%E7%AD%BE&_channel_track_key=myqX1C0f&utm_source=%E6%80%9D%E5%90%A6%E8%BD%AC%20ONES)
- [Swagger Bearer Token Answer](https://segmentfault.com/q/1010000017381307/a-1020000017382712)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with optional code, command, checklist, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include assumptions, validation steps, and remaining risks when relevant.]

## Skill Version(s):

0.20260831.40551 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
