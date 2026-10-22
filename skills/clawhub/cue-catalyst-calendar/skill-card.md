## Description:

Creates a date-ordered watch calendar for portfolio holdings using only dates explicitly disclosed by a source or derivable from a cited statute under verifiable conditions; it does not provide trading, price-impact, or timing judgments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT

## Use Case:

External investors and research teams use it to prepare a date-ordered calendar of verifiable upcoming events for their holdings, along with a source index and run log. It is not for trade timing, price-impact calls, or rumor-based events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connection test may send an API key to an unverified server, including over an unencrypted connection.

Mitigation: Use user-supplied announcements offline, or independently approve the destination and require HTTPS before providing a real key.

Risk: Online queries disclose which issuers interest the user.

Mitigation: Use the offline, user-supplied-announcement path when issuer interests are sensitive.

Risk: A calendar checker passing does not establish that its dates are factually accurate.

Mitigation: Verify calendar dates against the original disclosures and their evidence snapshots.

Risk: Unreviewed installer versions or source revisions may introduce unwanted changes.

Mitigation: Review installer versions and source revisions before use.

## Reference(s):

- [Event taxonomy](references/event-taxonomy.md)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Markdown, JSONL]

**Output Format:** [Markdown calendar and run log; JSONL source index]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Date-ordered; calendar dates require disclosure or applicable-statute evidence anchors.]

## Skill Version(s):

0.1.27 (source: frontmatter, CHANGELOG.md, released 2026-10-22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
