## Description:

Review federal exclusion evidence for a business or person using GovGazette when the user asks about a potential SAM exclusion, debarment or suspension match.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mooshee](https://clawhub.ai/user/mooshee)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement reviewers use this skill to research potential SAM exclusion, debarment, or suspension matches for a business or person using GovGazette records. It helps the agent report identity evidence, source status, dates, restriction type, agency, and official links without making a final eligibility determination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries are sent to a remote GovGazette MCP server for exclusion-record lookups.

Mitigation: Confirm the remote server connection is acceptable before installation and keep confidential bid material, private credentials, and unnecessary personal data out of queries.

Risk: Exclusion search results can be incomplete, stale, or ambiguous, especially for name-only matches.

Mitigation: Treat results as research evidence, cite dated official sources, and avoid presenting no-match results or name-only matches as final legal or eligibility determinations.

## Reference(s):

- [GovGazette MCP server](https://govgazette.com/mcp)
- [ClawHub skill page](https://clawhub.ai/mooshee/skills/govgazette-exclusion-review)

## Skill Output:

**Output Type(s):** [guidance, markdown, text]

**Output Format:** [Markdown or plain text with citations to retrieved records and dated official sources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include identity evidence, source status, dates, restriction type, agency, official links, and cautions about possible matches.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
