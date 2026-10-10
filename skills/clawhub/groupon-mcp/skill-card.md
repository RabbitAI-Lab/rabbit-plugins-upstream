## Description:

Helps agents search Groupon deals, inspect deal details, and browse categories using public, read-only deal data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents looking for Groupon offers can search by city or keyword, inspect a deal's pricing and fine print, and browse categories without signing in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Groupon receives the searches, city slugs, and deal IDs submitted for lookup.

Mitigation: Share only lookup inputs you are comfortable sending to Groupon.

Risk: Refreshing an expired query fingerprint from a browser request could expose account or session data if the entire request is copied.

Mitigation: Copy only the public sha256Hash value, not cookies, authorization headers, or personal account data.

## Reference(s):

- [Groupon query recipes](references/graphql-queries.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/groupon-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with deal details and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only deal lookups; no purchases or account access.]

## Skill Version(s):

1.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
