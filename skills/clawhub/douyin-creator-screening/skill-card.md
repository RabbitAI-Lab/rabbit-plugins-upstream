## Description:

Helps marketing teams find and assess Douyin creators using public video search, trending topics, creator posts, and comment data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Brand and marketing teams, creators, and analysts use this skill to research public Douyin content, compare potential creator partners, and prepare evidence-based KOL shortlists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin keywords or links and the GUAIKEI API token are sent to the external GUAIKEI service.

Mitigation: Use only approved queries and credentials; confirm the service is permitted for the intended data.

Risk: Public creator and comment results can be retained in local logs or used outside authorized contexts.

Mitigation: Limit access and log retention, and use public data only for compliant, authorized analysis.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/douyin-creator-screening)
- [GUAIKEI service](https://www.guaikei.com)
- [Skill options](references/options.md)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [Structured JSON results and text recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public video, creator, comment, and trending-topic data; search, post, and comment results may be logged locally.]

## Skill Version(s):

1.3.0 (source: SKILL.md frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
