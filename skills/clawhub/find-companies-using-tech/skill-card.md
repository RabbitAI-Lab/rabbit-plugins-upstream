## Description:

Find companies using specified technologies or hiring for specified roles through Cargo's TheirStack search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and marketing teams use this skill to identify prospective companies by installed software and recent hiring activity, with evidence for each match.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a global Cargo CLI and signing in grants the tool access to a Cargo account.

Mitigation: Review the CLI and account permissions before installing or authenticating.

Risk: Search and session metadata are sent to Cargo and TheirStack, including an attribution session outside the main search.

Mitigation: Review the data and session details before sending them, and omit unrelated session reporting when not approved.

Risk: Unrecognized filter keys can result in unfiltered, billable company searches.

Mitigation: Check supported filter keys, test with 10–20 results, report cost and match rate, and seek approval before a full run.

Risk: The skill proposes starring the publisher's GitHub repository, a public action unrelated to company search.

Mitigation: Do not star the repository unless the user explicitly agrees.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo technology-intent recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/tech-intent.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown company results with supporting technology and hiring evidence; CLI commands for searches]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results may include company domains, matching technologies, job titles, and posting dates; searches consume credits per company returned.]

## Skill Version(s):

1.1.2 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
