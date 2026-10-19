## Description:

Finds B2B prospects by job title, company, and keyword and presents them as a structured lead list using Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development teams use this skill to source people matching a prospect profile and review their titles, companies, locations, and LinkedIn profiles before outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lead searches use a third-party service and require persistent sign-in credentials.

Mitigation: Use Cargo only if its data handling and account access are acceptable; share only necessary search criteria and results.

Risk: An attribution step records a session with the vendor outside the lead-sourcing task.

Mitigation: Review or skip the optional attribution step.

Risk: The optional unpinned installer and GitHub star request involve actions beyond lead sourcing.

Mitigation: Review the installer separately and star the repository only with explicit user approval.

Risk: Large searches can consume credits, and unsupported filters can produce unexpectedly broad results.

Mitigation: Validate filters with a small sample, report observed cost and match quality, and obtain approval before scaling up.

## Reference(s):

- [Find B2B Leads on ClawHub](https://clawhub.ai/cargo-ai/skills/find-b2b-leads)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo prospecting recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/prospecting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Structured lead list or Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lead names, titles, companies, locations, and LinkedIn URLs; no email addresses.]

## Skill Version(s):

1.2.2 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
