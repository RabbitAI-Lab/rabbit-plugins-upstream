## Description:

Read MaxPreps.com high school sports data - find a school, then get team schedules, scores, records, rosters, stat leaders, rankings, and athlete careers for any US high school.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve public MaxPreps high-school sports data and turn it into schedules, scores, rosters, rankings, standings, stat leaders, and athlete career summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local Node.js helper contacts public MaxPreps web endpoints and caches a temporary build identifier.

Mitigation: Install and run it only where outbound requests to MaxPreps and a temporary local cache are acceptable; review proposed commands before execution.

Risk: Incorrect paths, stale build identifiers, or out-of-season pages can produce empty or misleading sports data.

Mitigation: Resolve schools and teams with the documented search and teams lookups, rely on the helper's build-id refresh, and cross-check important schedules or rosters against source totals.

## Reference(s):

- [MaxPreps recipes](references/recipes.md)
- [MaxPreps](https://www.maxpreps.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/maxpreps-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a local Node.js helper to fetch public MaxPreps JSON routes and decode sports data; no MaxPreps credentials or browser session are required.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
