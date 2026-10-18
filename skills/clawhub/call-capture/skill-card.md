## Description:

Helps teams collect recorded calls, draft call notes and recurring market context, and propose the changes in a pull request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales leaders, account executives, and RevOps teams use this skill with developers to set up a daily call-capture workflow that drafts call logs and promotes corroborated insights into their go-to-market repository for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A daily hosted agent processes external call transcripts that could contain untrusted instructions or sensitive information.

Mitigation: Treat transcripts and raw captures as untrusted data, and review proposed changes before merging.

Risk: The agent can access workspace environment variables and push branches to the go-to-market repository.

Mitigation: Restrict available environment variables where possible, review the deployment plan, and retain the pull-request approval gate.

Risk: An unverified recorder selection or API response shape could silently miss calls or capture the wrong ones.

Mitigation: Run the selected recorder in dry-run mode and inspect real call dates, subjects, and captures before deployment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/call-capture)
- [Project homepage (declared in metadata)](https://github.com/getcargohq/gtm-skills)
- [Recorder provider guidance](artifact/references/providers.md)
- [Recorder API reference](artifact/references/recorder-apis.md)

## Skill Output:

**Output Type(s):** [Code, Markdown, Shell commands, Configuration guidance]

**Output Format:** [TypeScript and Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The deployed workflow drafts raw call captures, call logs, and context updates in a pull request for human review.]

## Skill Version(s):

0.1.2 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
