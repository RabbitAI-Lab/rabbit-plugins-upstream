## Description:

Analyzes X bookmarks by polling for saved posts, fetching linked article text, using AI to extract summaries, concepts, action items, and project-specific suggestions, and optionally sending high-value insights through Telegram.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge workers use this skill to turn X bookmarks into structured research notes, actionable next steps, and project-specific implementation suggestions. It is intended for configured X bookmark analysis workflows, not non-X bookmark managers or real-time low-latency processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires X session-cookie access and can run as a persistent background process.

Mitigation: Install only if this access is acceptable, narrow the trigger to X bookmark analysis, and use conservative polling settings.

Risk: Bookmark, linked article, and project context may be sent to AI services and Telegram.

Mitigation: Avoid sensitive bookmarks or project descriptions, configure explicit notification settings, and review the selected service providers' data handling terms.

Risk: Bookmark analyses may be stored under a local knowledge-base path.

Mitigation: Use short retention where possible, restrict local file permissions, and avoid syncing analysis JSON to untrusted locations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/bookmark-intelligence)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON analysis records, and optional Telegram notification text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May store bookmark analyses under a local knowledge-base path and send high-priority summaries to Telegram depending on user configuration.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
