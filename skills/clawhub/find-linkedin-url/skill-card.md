## Description:

Find and validate a person's LinkedIn profile URL from their name and company using Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development and RevOps teams use this skill to find a contact's LinkedIn profile URL from their name and company, then validate the match against company details. It marks unresolved or incorrect matches rather than guessing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A lookup may return the wrong person's profile, and contact details are shared with Cargo.

Mitigation: Use this only for contacts you may share with Cargo, and verify each candidate's identity and company before accepting the result.

Risk: Credit costs grow with the number of contacts processed.

Mitigation: Run a small sample first, review its cost and hit rate, then obtain approval before processing the full list.

Risk: The external CLI and broader Cargo pack are outside this artifact review.

Mitigation: Review those tools separately, preferably at fixed versions.

## Reference(s):

- [Cargo LinkedIn URL lookup recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/linkedin-url-lookup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV data, Guidance]

**Output Format:** [Markdown table or CSV rows with a LinkedIn profile URL and validation status per contact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Unresolved or rejected matches are marked explicitly.]

## Skill Version(s):

1.0.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
