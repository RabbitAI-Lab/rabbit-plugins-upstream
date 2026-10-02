## Description:

Find B2B prospects by job title, company, and keyword and return a structured list of profiles using Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales-development teams use this skill to source people matching job-title, company, keyword, and location criteria for outbound prospecting. Results include profile details and LinkedIn URLs, not email addresses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the Cargo CLI and signing in may create an account and workspace.

Mitigation: Review the CLI installation and authentication steps before proceeding.

Risk: Lead searches spend Cargo credits, especially when run across larger batches.

Mitigation: Try a small sample, disclose the observed cost and estimated total, and request approval before a full run.

Risk: The skill checks local Claude plugin configuration and records a session attribution marker.

Mitigation: Review and authorize these ancillary steps separately from the lead search.

Risk: The skill suggests an optional full-pack installation and a GitHub star using the user's account.

Mitigation: Do neither unless the user explicitly requests or approves the action.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/find-b2b-leads)
- [Project homepage (listed in metadata)](https://github.com/getcargohq/gtm-skills)
- [Cargo prospecting recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/prospecting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Structured lead list or Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profiles include names, titles, companies, and LinkedIn URLs; email addresses are not supplied.]

## Skill Version(s):

1.1.1 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
