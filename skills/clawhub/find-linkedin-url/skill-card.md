## Description:

Finds a person's LinkedIn profile URL from their name and company, then validates the candidate against the person's employer using Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development and revenue operations teams use this skill to find and validate LinkedIn URLs for contacts using their names and companies, rejecting missing or mismatched profiles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact names and companies are sent to external services, and large batches consume credits.

Mitigation: Approve sharing contact data; trial a small batch, review its cost and match rate, and approve larger runs before executing them.

Risk: Setup uses an unpinned CLI release and can change local Cargo state.

Mitigation: Review the installation and account changes, and use a pinned CLI version when possible.

Risk: The skill includes session attribution, local agent configuration inspection, and an optional promotional GitHub star unrelated to lookup.

Mitigation: Skip attribution and the star unless intentionally desired; require explicit approval before using the user's GitHub account.

## Reference(s):

- [Cargo GTM skills homepage (release metadata)](https://github.com/getcargohq/gtm-skills)
- [LinkedIn URL lookup recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/linkedin-url-lookup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown table of contact names, companies, validated LinkedIn URLs, and status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Unresolved or mismatched contacts are marked rather than assigned a guessed URL.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
