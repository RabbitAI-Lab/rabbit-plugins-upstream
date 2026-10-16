## Description:

Compare public fixtures, live scores, match statistics, standings, and head-to-head records using Crawlora Flashscore and LiveScore tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

People researching sports matches use this skill to check fixtures and scores, prepare sourced previews or recaps, and reconcile Flashscore and LiveScore observations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sports queries send requested lookup parameters to Crawlora and require a Crawlora API key.

Mitigation: Use a key you are authorized to use and send only intended public match lookup parameters.

Risk: Unbounded lookups or polling can consume API credits.

Mitigation: Limit requests to the needed matches and agreed credit budget; poll only when requested.

## Reference(s):

- [Supported sports endpoints](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/multi-sport-match-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown match research with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source links, match status, observation times, and unresolved provider differences when available.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
