## Description:

Finds a person's LinkedIn profile URL from their name and company, then checks the match before returning it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development and revenue operations teams use this skill to find and validate LinkedIn profile URLs for contacts using their names and companies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact details are sent to Cargo for LinkedIn lookup and validation.

Mitigation: Use only contact data approved for third-party processing.

Risk: Setup reads a local Claude plugin file and sends a session attribution record to Cargo.

Mitigation: Review local configuration access and session attribution before running setup.

Risk: The skill can prompt for a GitHub star outside the lookup task.

Mitigation: Do not star a repository unless the user explicitly agrees.

Risk: Installing the latest CLI or skill pack can introduce unreviewed changes.

Mitigation: Pin and review dependency versions in controlled environments.

Risk: Same-name matches can return the wrong person's profile, and large batches consume credits.

Mitigation: Validate company matches, reject uncertain results, and approve a small pilot before a full batch.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [LinkedIn URL lookup recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/linkedin-url-lookup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Text or Markdown table of profile URLs and validation statuses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Unresolved or mismatched contacts are marked explicitly; batch results are available as CSV.]

## Skill Version(s):

1.0.2 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
