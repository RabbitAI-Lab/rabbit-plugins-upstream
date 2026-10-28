## Description:

Helps sales teams monitor target accounts for dated hiring, public-post, and detection-feed signals that may change outreach timing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Account executives and sales development teams use this skill to identify timely, source-linked changes among target accounts while keeping signal research separate from permission to contact people.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup sends a session-attribution record to Cargo and checks local Claude plugin configuration.

Mitigation: Review the setup actions and approve the attribution write before running them.

Risk: Cargo lookups can consume credits, especially across large lists or repeated runs.

Mitigation: Run the free detection check first, sample a small list, estimate credits, and approve wider or recurring queries.

Risk: Optional full-pack installation is unpinned, and the skill can request a GitHub star.

Mitigation: Review the package before installing; star only after explicit user approval.

Risk: Public buying signals or mistaken social handles can prompt misleading or unwarranted outreach.

Mitigation: Verify source links and company handles, and require an independent basis for contacting anyone.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo tech-intent recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/tech-intent.md)
- [Cargo account-expansion recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/account-expansion.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Markdown table with account, signal, date, source, and significance; optional setup and query commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports only accounts with signals; distinguishes missing detections from confirmed absence of signals.]

## Skill Version(s):

1.0.3 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
