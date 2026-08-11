## Description:

HeartFlow 心虫 is a local rule-based cognitive preprocessing and text-discrimination engine that classifies and routes input, detects PAD emotion signals, checks AI output, and returns deterministic gate decisions for downstream agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yun520-1](https://clawhub.ai/user/yun520-1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use HeartFlow to add a local rule-engine gate that checks user input, draft responses, and AI output for safety, honesty, manipulation, routing, and cognitive-state signals before downstream generation or delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes a broad authenticated local MCP service.

Mitigation: Review the exposed tools before deployment, set your own MCP token, and run the service only in environments where a local authenticated MCP endpoint is acceptable.

Risk: The skill can keep persistent local state in its own files.

Mitigation: Use it only where local state retention is acceptable, avoid running the pm2 service unless needed, and consider setting HEARTFLOW_PATH_GUARD=enforce when working with private projects.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yun520-1/skills/mark-heartflow-skill)
- [npm package @yun520-1/heartflow](https://www.npmjs.com/package/@yun520-1/heartflow)

## Skill Output:

**Output Type(s):** [text, JSON, guidance, configuration, shell commands]

**Output Format:** [Structured JSON-like findings with concise text guidance and optional command/configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns local rule-engine scores, gate actions, findings, and routing guidance; artifact documentation claims no LLM dependency.]

## Skill Version(s):

6.5.1 (source: server release metadata and package.json; SKILL.md frontmatter lists 6.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
