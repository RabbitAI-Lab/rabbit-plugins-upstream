## Description:

Read public MaxPreps high school sports data to find schools and explore team schedules, scores, rosters, statistics, rankings, and athlete careers in the United States.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents serving sports researchers, journalists, and other users can look up public US high school team results, rosters, rankings, and athlete career information from MaxPreps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper makes network requests to MaxPreps and retrieves public roster and athlete information.

Mitigation: Run it only when those read-only requests are acceptable, and handle retrieved athlete information with care.

## Reference(s):

- [ClawHub maxpreps-mcp release](https://clawhub.ai/chrischall/skills/maxpreps-mcp)
- [MaxPreps](https://www.maxpreps.com)
- [Usage recipes](references/recipes.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown with sports data and optional shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The included helper returns structured JSON for requested public MaxPreps data.]

## Skill Version(s):

1.1.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
