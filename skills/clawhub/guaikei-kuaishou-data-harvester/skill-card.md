## Description:

Collects public Kuaishou search results, creator posts, and video comments through the Guaikei API and returns structured JSON for content research, competitor monitoring, and sentiment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, marketers, and data analysts use this skill to collect public Kuaishou data for topic research, competitor monitoring, creator analysis, and comment review. Agents can route keyword, creator-profile, or video-comment requests to the appropriate command and return structured results for follow-on analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou keywords, profile or video URLs, and the Guaikei API token are sent to a third-party service.

Mitigation: Use the skill only when third-party data sharing is approved, and keep GUAIKEI_API_TOKEN out of prompts, shared logs, and command output.

Risk: Generated logs may retain comments, creator identifiers, or business-sensitive research data.

Mitigation: Protect or delete logs and exported results according to the user's data-retention and redistribution requirements.

Risk: Server security review marked the release suspicious because token-handling guidance and automatic local result storage need review.

Mitigation: Review the skill before deployment, use token presence checks instead of printing token values, and scan saved outputs before sharing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-data-harvester)
- [Guaikei API Site](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Files, Guidance]

**Output Format:** [Structured JSON with status, request metadata, and result data, usually summarized in Markdown by the agent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and may save result logs locally.]

## Skill Version(s):

1.0.0 (source: frontmatter metadata, package.json, changelog released 2026-08-29, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
