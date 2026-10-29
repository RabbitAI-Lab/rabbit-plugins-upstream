## Description:

Turns a meeting recording and optional agenda materials into Chinese minutes with timestamped transcript excerpts, self-labeled topic sections, decisions and action items linked to source utterances, and items to verify; it is not for live transcription.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and teams use this skill to turn Chinese-language meeting recordings and optional agenda materials into reviewable minutes, including timestamped transcript excerpts, decisions, action items, and unresolved questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentialed connection checks could expose the CUE API key.

Mitigation: Before enabling credentialed checks, require validated destinations and blocked redirects.

Risk: Confidential meeting content may be processed by Cue.

Mitigation: Use the manual card workflow for confidential meetings unless Cue processing and its data-handling terms are approved.

Risk: The validator can reject legitimate financial quotations.

Mitigation: Preserve quoted financial amounts and review validator failures rather than changing amounts to satisfy the validator.

Risk: Optional dependencies may pose version-related concerns.

Mitigation: Review fixed versions of optional dependencies before installing them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huhoo/skills/cue-meeting-minutes-cn)
- [Cue API key guidance](https://cuecue.cn/hub/api-key)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Five-section Markdown meeting-minutes card with transcript excerpts and mm:ss timestamps when channel data is available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documented local-audio limit is one file up to 256 MiB (268435456 bytes), subject to the channel's reported limit; not for real-time transcription. Oversize files should be split. ASR errors are retained and marked for review.]

## Skill Version(s):

0.2.26 (source: frontmatter; confirmed by server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
