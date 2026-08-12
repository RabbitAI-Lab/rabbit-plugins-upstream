## Description:

Guides agents to consider evidence-backed removal of harmful or nonessential elements before adding features, layers, processes, or controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tjboudreaux](https://clawhub.ai/user/tjboudreaux)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agent users use this skill when they are about to add a feature, abstraction, dependency, process, or control. It helps them identify evidence-backed removals first, preserve load-bearing safeguards, and add only when a demonstrated need remains.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Over-applying subtraction could remove load-bearing controls such as authentication, validation, tests, retries, rate limits, or safety checks.

Mitigation: Require evidence of non-use or net harm, classify reversibility, preserve do-not-touch controls, and stage removals with rollback and verification.

Risk: A removal proposal could be misleading if based on preference rather than usage, call-graph, metrics, or experiment evidence.

Mitigation: Document evidence for each candidate and reject subtraction when evidence is missing or the element may be load-bearing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tjboudreaux/skills/thinking-via-negativa)
- [Publisher profile](https://clawhub.ai/user/tjboudreaux)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Structured Markdown or text with goal, removal candidates, action, verification plan, and do-not-touch fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reasoning aid only; no external services, credentials, tools, or MCP servers are referenced.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
