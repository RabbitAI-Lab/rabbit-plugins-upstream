## Description:

Monitor websites for changes, downtime, or specific content. Get notified when a page changes, goes down, or matches/stops matching a pattern. Lightweight — no database needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zacjiang](https://clawhub.ai/user/zacjiang)

### License/Terms of Use:


## Use Case:

Developers and operators use this skill to run lightweight website uptime, change-detection, and content-pattern checks from an agent workflow or scheduled task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can fetch unrestricted URLs from the user's machine.

Mitigation: Use trusted URL lists and avoid monitoring private or internal endpoints unless that access is intended.

Risk: Fetched page text can be saved locally in a configurable state directory.

Mitigation: Choose a private state directory you control instead of a shared /tmp path, and clean old state files when they are no longer needed.

Risk: Runtime behavior depends on the external requests package.

Mitigation: Install dependencies in a dedicated environment with pinned versions where possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zacjiang/skills/site-monitor)
- [ClawHub publisher profile](https://clawhub.ai/user/zacjiang)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration guidance]

**Output Format:** [Plain text status messages, short diffs, exit codes, and Markdown guidance with bash commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return exit codes for unchanged, changed, and unavailable states; watch and batch modes can write local state files.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata, released 2026-03-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
