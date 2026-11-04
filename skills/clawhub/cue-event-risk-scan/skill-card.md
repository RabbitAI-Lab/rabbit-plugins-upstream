## Description:

Creates a source-linked company scan card covering regulatory penalties and measures, external guarantees, and cross-border sanctions, while identifying unavailable coverage and avoiding an overall risk score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and due diligence teams use the skill to assemble a one-company scan of cited regulatory actions, guarantee information, and sanctions coverage. It calls out unavailable areas and is not intended to provide an overall risk rating, default probability, or investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connection examples may expose the Cue API key.

Mitigation: Use the manual workflow without an API key until both credential paths enforce authorized HTTPS destinations and safe redirect handling.

Risk: The report checker accepts entries without sources, and a PASS does not establish report accuracy.

Mitigation: Independently verify each report item against its cited source; treat the checker as a format check only.

Risk: External retrieval shares company identifiers with Cue.

Mitigation: Use a manual workflow when company identifiers should not be sent to Cue.

Risk: Live Cue services and the separately installed companion skill were not assessed.

Mitigation: Review those services and the companion skill independently before relying on them.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huhoo/skills/cue-event-risk-scan)
- [Cue data MCP configuration](https://cuecue.cn/hub/mcp)
- [Cue live MCP catalog](https://cuecue.cn/api/mcp-catalog)
- [Cue API key settings](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown scan card with sourced entries, tables, coverage notes, and items for human review]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One company per card; includes source and date anchors, reporting windows, unavailable coverage, and human-review items.]

## Skill Version(s):

0.2.24 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
