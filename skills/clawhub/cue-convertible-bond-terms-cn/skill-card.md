## Description:

Turns an A-share convertible bond prospectus or issuance announcement into eight source-anchored, verbatim clause cards, flags missing details, and leaves financial judgments for human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and financial document reviewers use the skill to extract eight verbatim A-share convertible-bond clauses from a prospectus or issuance announcement, preserve source anchors, and identify missing details. Investment and operational judgments remain for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private or sensitive documents may be sent to optional online parsing services.

Mitigation: Use public or redacted documents when possible and review the provider's retention terms before enabling online parsing.

Risk: An API key could be exposed if supplied to an untrusted destination.

Mitigation: Verify that the routing destination is trusted and uses HTTPS before supplying the key; keep credentials in local storage.

Risk: Optional installers and integrations are outside the inspected release bundle.

Mitigation: Review and pin optional installers and integrations before enabling them.

## Reference(s):

- [可转债条款记法速查](references/cb-clauses.md)
- [Cue MCP configuration](https://cuecue.cn/hub/mcp)
- [Cue Omni Reader configuration](https://cuecue.cn/hub/omni-reader)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown clause card with verbatim quotes and source anchors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Eight clause entries; missing clauses are identified, and financial judgments are left for human review.]

## Skill Version(s):

0.1.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
