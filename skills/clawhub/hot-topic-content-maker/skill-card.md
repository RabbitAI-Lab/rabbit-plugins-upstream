## Description:

Hot Topic Content Maker helps agents turn a supplied or looked-up trend into same-day social content with angles, cover copy and imagery, captions, hashtags, and optional short narrated video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, and social media operators use this skill to move quickly from a live topic or seasonal peg to a publishable vertical social post. It supports optional trend lookup, angle selection, post planning, paid media generation, delivery review, and recovery for Beatra-backed image, speech, and video tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a broad shared Beatra bearer token stored under ~/.beatra.

Mitigation: Confirm the access model before installation, avoid exposing the token in chat or logs, and use the documented disconnect and revocation controls when access should end.

Risk: Executable package code silently checks for and installs newer Beatra releases by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when each code change should require explicit review.

Risk: Trend-driven posts can make incorrect or misleading claims about live events if facts are assumed.

Mitigation: Use only facts supplied by the user or returned by an attributed trend lookup, and present momentum or shelf-life judgments as inference.

## Reference(s):

- [Hot topic workflow](artifact/references/workflow.md)
- [Finding the angle](artifact/references/angle-finding.md)
- [Looking up what is trending](artifact/references/trend-lookup.md)
- [Building the post](artifact/references/post-plan.md)
- [One run, end to end](artifact/references/worked-example.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)
- [Questions and anti-patterns](artifact/references/faq.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Beatra skill homepage](https://beatra.ai/skills/hot-topic-content-maker)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with structured approval text, inline shell commands, JSON payload examples, and returned artifact details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image, audio, and video artifact links returned by Beatra tools; paid calls require explicit user confirmation.]

## Skill Version(s):

0.2.1 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
