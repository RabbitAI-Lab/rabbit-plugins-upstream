## Description:

Finds a person's LinkedIn profile URL from their name and company, then validates the match before returning it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development and revenue operations teams use this skill to find LinkedIn URLs for contacts from names and companies, rejecting mismatches rather than guessing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill checks local agent configuration and sends session attribution to Cargo in addition to making LinkedIn lookup calls.

Mitigation: Review these steps and allow the Cargo CLI and connector to access only data you intend to share.

Risk: Installation instructions use unpinned packages, including an optional full-pack install.

Mitigation: Prefer a reviewed, pinned CLI version; skip the full-pack install unless you intend to add it.

Risk: An optional GitHub star uses the user's account.

Mitigation: Review the request and approve a star only if you want to endorse the project.

Risk: Bulk lookups consume credits and candidate profiles can match the wrong person.

Mitigation: Test a small sample, approve the estimated full-run cost, and validate company matches before accepting URLs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/find-linkedin-url)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [LinkedIn URL lookup recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/linkedin-url-lookup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Contact list or table with LinkedIn URLs and validation status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Unresolved or mismatched contacts are marked explicitly.]

## Skill Version(s):

1.0.3 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
