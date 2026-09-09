## Description:

Use when writing or continuing a long document - a novel, serial, manual, course, screenplay, or AI-written book - that has more chapters than fit in one context window.

This skill is ready for commercial/non-commercial use.

## Publisher:

[emberspun-ai](https://clawhub.ai/user/emberspun-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External writers, editors, and developers use this skill to keep long manuscripts consistent across chapters that exceed one context window. It guides agents through recalling prior context, tracking unresolved threads, recording chapter changes, and checking continuity before publication or revision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires running the disclosed npm MCP server.

Mitigation: Review and approve the MCP server before installation, and install it only in environments where that dependency is acceptable.

Risk: The skill stores manuscript text and continuity data in local plain files.

Mitigation: Use it only for projects where local plain-file storage is acceptable, and apply normal local disk access controls for sensitive manuscripts.

Risk: Using inconsistent project names or stale thread numbers can cause empty recall results or incorrect thread updates.

Mitigation: Keep the project name identical across sessions and refresh thread listings for the current chapter before progressing or resolving threads.

## Reference(s):

- [Longform Memory Source and Documentation](https://emberspun.com/open-source/longform-memory)
- [Emberspun AI Book Writer](https://emberspun.com)
- [ClawHub Skill Page](https://clawhub.ai/emberspun-ai/skills/longform-writing)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with a JSON MCP configuration example and inline tool-call names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the longform-memory MCP server; manuscript memory is stored locally in plain files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
