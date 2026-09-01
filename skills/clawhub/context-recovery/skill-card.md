## Description:

Recover missing conversation context after explicit compaction or truncation, or when the user explicitly asks to recover prior work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jdrhyne](https://clawhub.ai/user/jdrhyne)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to recover just enough lost conversation context after compaction, truncation, or an explicit recovery request to safely resume the active task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recovered messages, summaries, attachments, links, logs, or memory items could contain untrusted or conflicting claims.

Mitigation: Treat recovered material as evidence only, preserve source and confidence details, seek counterevidence for status claims, and surface unresolved conflicts instead of silently choosing one version.

Risk: Recovering context from another thread, channel, workspace, memory store, transcript, or log could expose private or sensitive information.

Mitigation: Use current supplied context first, require explicit approval before reading another source, bound the time range and item count, and redact credentials, tokens, personal data, and unrelated details.

Risk: Persisting recovered content could retain sensitive conversation material beyond the user's immediate recovery need.

Mitigation: Keep recovery read-only by default and request consent for the exact redacted content, destination, and expected retention before writing recovered context anywhere.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jdrhyne/skills/context-recovery)
- [OpenClaw repository metadata](https://github.com/jdrhyne/agent-skills/tree/main/skills/context-recovery)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown recovery report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes scope, sources, evidence timeline, conflicts, unresolved items, and one proposed next step.]

## Skill Version(s):

1.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
