## Description:

Track official government documents in the Chinng AI-Agent Portal, including US Federal Register, EU EUR-Lex, and Japanese agency feeds, for regulatory monitoring, comment deadlines, effective dates, and primary-source policy reading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chinng-inta](https://clawhub.ai/user/chinng-inta)

### License/Terms of Use:

MIT-0

## Use Case:

Policy analysts, compliance teams, and agents use this skill to find and report official government policy documents with agency, jurisdiction, document type, identifiers, deadlines, effective dates, official source links, and portal links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a disclosed third-party read-only portal endpoint for government document discovery.

Mitigation: Install and use the portal endpoint only when that third-party endpoint is acceptable for the user's environment.

Risk: Generated or feed-derived summaries may not be authoritative document content.

Mitigation: Report summaries only when summary_source is official; otherwise use structured fields and direct the reader to the official source URL for substance.

Risk: Recurring monitoring can miss revised documents if cursor state is advanced too early.

Mitigation: Persist a new change cursor only after the batch has been processed successfully and distinguish revised records from newly published documents.

## Reference(s):

- [Chinng AI-Agent Portal MCP endpoint](https://portal.chinng-lab-srv.dev/mcp)
- [ClawHub skill page](https://clawhub.ai/chinng-inta/skills/government-policy-watch)
- [Publisher profile](https://clawhub.ai/user/chinng-inta)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured reporting instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should retain official source URLs and portal links, distinguish new documents from revisions, and avoid restating generated or feed-derived summaries as document content.]

## Skill Version(s):

0.2.1 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
