## Description:

Discards the accumulated drafts and framings from this thread and re-derives the task from a clean problem statement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Agent users use this skill when prior drafts, assumptions, or repeated attempts are anchoring the conversation. It extracts the facts worth keeping and either recommends a clean-context handoff for high-stakes work or re-derives the task from the brief for mild drift.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording could interrupt an ongoing task when the user asks for a fresh take or says the discussion is going in circles.

Mitigation: Review the extracted brief before relying on the reset for sensitive or complex work.

Risk: For deep contamination or high-stakes work, the current context may be unreliable for authoring its own reset.

Mitigation: Use the extracted brief with a fresh subagent or start a new session.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/reset-context-contamination)
- [Skill homepage](https://github.com/tenequm/skills/tree/main/skills/reset-context-contamination)

## Skill Output:

**Output Type(s):** [guidance, markdown]

**Output Format:** [Markdown prose]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-only skill; no executable code, tool calls, credential use, or MCP references were identified in the provided evidence.]

## Skill Version(s):

0.1.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
