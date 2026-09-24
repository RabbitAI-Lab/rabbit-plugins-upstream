## Description:

Zhejiang technology-based SME roster lookup for newest-batch newly listed companies, city distribution, and sourcing leads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users, agents, and business-development teams use this skill to query Zhejiang Province technology-based SME roster data, identify newly listed companies, compare city-level distribution, and screen agency, finance, tax, or industrial-park sourcing leads.

### Deployment Geography for Use:

Global use; data coverage is limited to Zhejiang Province, China.

## Known Risks and Mitigations:

Risk: Roster queries and any API or session credentials are sent to a hardcoded external data service.

Mitigation: Install and run the skill only when the publisher and data service are trusted for the intended queries and credentials.

Risk: The skill creates a plaintext credential file at ~/.odf/zj-sme-roster.json and reuses stored cookies or install IDs across runs.

Mitigation: Remove ~/.odf/zj-sme-roster.json to clear local state, stored cookies, install identifiers, and any saved API key.

Risk: The roster only covers the collected portion of Zhejiang Province technology-based SME data, so a missed query is not proof that a company is absent from the official roster.

Mitigation: Present lookup results with the skill's stated coverage limits and defer to official sources when the skill output conflicts with official publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/zj-sme-roster)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown summaries of roster matches, city distribution tables, and coverage notes, with shell commands for invoking the script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries are sent to a hardcoded external data service; local state may include API/session credentials and install cookies.]

## Skill Version(s):

1.0.6 (source: server release metadata, SKILL.md frontmatter, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
