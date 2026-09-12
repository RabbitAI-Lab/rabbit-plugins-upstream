## Description:

Discards this thread's accumulated drafts and framings and re-derives the task from a clean problem statement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

External users, developers, and agent operators use this skill to recover from a conversation that has drifted, looped, or become anchored on unhelpful prior drafts by extracting a clean brief and re-deriving the task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may cause an agent to ignore prior drafts and reframe the task from a cleaned-up brief.

Mitigation: Use it when the user explicitly asks for a reset or when the thread is visibly drifting, and preserve known facts, hard constraints, and previously ruled-out approaches in the brief.

Risk: For deep contamination or high-stakes work, an in-thread reset may still carry over flawed assumptions.

Mitigation: Hand the extracted brief to a fresh subagent or recommend starting a new session, as the skill itself directs for high-severity cases.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/reset-context-contamination)
- [OpenClaw Homepage](https://github.com/tenequm/skills/tree/main/skills/reset-context-contamination)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text]

**Output Format:** [Markdown guidance with concise procedural steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No code execution, data access, credentials, tools, or MCP integrations detected.]

## Skill Version(s):

0.1.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
