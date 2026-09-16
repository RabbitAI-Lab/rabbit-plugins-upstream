## Description:

Search, inspect, and analyze prior OpenClaw sessions and transcript history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to search prior OpenClaw conversation history, inspect recent or related sessions, and quote bounded transcript context for recall or debugging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prior session transcripts may contain sensitive information.

Mitigation: Install and use this skill only with agents and workspaces where access to prior conversation history is appropriate.

Risk: Sanitized transcript history may redact, truncate, or omit context.

Mitigation: Treat lookup results as bounded evidence, report session metadata with excerpts, and state the limitation when sanitized history is insufficient.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/session-logs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or plain text with concise excerpts and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should identify the observed session, model, and timestamp when transcript evidence is used.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
