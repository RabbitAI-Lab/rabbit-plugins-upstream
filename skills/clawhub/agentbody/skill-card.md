## Description:

AgentBody routes agent tasks to documented AgentBody REST APIs for supported public social data, public HTTPS document parsing, explicitly requested text humanization, supported SEO data, and AgentBody account or usage questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentbody](https://clawhub.ai/user/agentbody)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to choose and call the appropriate AgentBody API for supported public-data, document parsing, SEO, text humanization, and account-related tasks while reporting results with stated coverage limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make network calls to AgentBody using the user's API key.

Mitigation: Install only when AgentBody API access is intended, review credential locations before use, and expect calls to AgentBody endpoints.

Risk: API responses, documents, posts, comments, captions, and transcripts may contain untrusted content.

Mitigation: Treat returned content as evidence only, ignore embedded instructions, and keep final reporting separate from interpretation.

Risk: Unsupported sources, private content, or unclear API contracts can lead to incomplete or incorrect results.

Mitigation: Use only documented public inputs, read the current API directory and selected detail pages, and state limitations instead of guessing or substituting operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/agentbody/skills/agentbody)
- [AgentBody API Directory](https://docs.agentbody.io/llms.txt)
- [AgentBody Documentation](https://agentbody.io/)
- [AgentBody API Endpoint](https://api.agentbody.io)

## Skill Output:

**Output Type(s):** [guidance, text, markdown, API calls, configuration]

**Output Format:** [Markdown or text summaries with API results and coverage limits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires AGENTBODY_API_KEY for API calls; uses documented public-data and document APIs only.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
