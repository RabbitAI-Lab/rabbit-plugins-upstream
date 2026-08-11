## Description:

Analyze one named competitor's organic footprint, ranking keywords, content themes, backlinks, and weaknesses using a connected Conqueror MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samuelnoah45](https://clawhub.ai/user/samuelnoah45)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, SEO teams, and developers use this skill to deep-dive a named competitor's organic search footprint and turn keyword, SERP, content, backlink, and local SEO evidence into priority actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Competitor conclusions can be misleading if keyword rows are treated as page-level or local-pack evidence.

Mitigation: Separate evidence from inference and use SERP, local business, or local SERP tools before making page-level or local SEO claims.

Risk: Comparisons can use first-party Search Console data for the user's domain when Search Console is connected.

Mitigation: Install and run the skill only for authorized projects and review whether Search Console access is intended for the requested comparison.

Risk: The workflow depends on a connected Conqueror MCP server and may be incomplete if tool data is unavailable.

Mitigation: State missing data explicitly and continue without backlink or comparison evidence only when the final analysis labels the gap.

## Reference(s):

- [Conqueror Competitor Analysis Skill](https://clawhub.ai/samuelnoah45/skills/conqueror-competitor-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown analysis with an evidence table and prioritized action sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a connected Conqueror MCP server and relevant domain or project inputs.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
