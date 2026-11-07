## Description:

Smart context compaction for OpenClaw agents that scans tool outputs, extracts valuable information into memory files, and generates a pre-compact checklist before /compact.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavmson](https://clawhub.ai/user/wavmson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill before context compaction to preserve important configuration details, decisions, errors, user preferences, and task progress in memory files. It helps them review what will be retained before choosing whether to run /compact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill scans prior conversation and tool output, which can include secrets, internal endpoints, sensitive paths, or other operational details.

Mitigation: Require the agent to show proposed memory entries before writing, redact secrets and authentication material, and avoid storing sensitive endpoints or paths unless necessary.

Risk: Selected details are written to persistent memory files and may remain available longer than intended.

Mitigation: Periodically review and delete memory files that are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wavmson/skills/pre-compact)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown checklist with memory-entry summaries and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May append selected extracted details to memory/YYYY-MM-DD.md after review.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
