## Description:

Monitors target accounts for dated public buying signals, such as relevant hiring, public statements, and detection-feed events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and account teams use this skill to identify timely public activity at target accounts and report actionable signals with dates, source links, and context. Signals support research, not permission to contact someone.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cargo login persists and monitoring connector calls may spend credits.

Mitigation: Review account access and credit balance; sample 10–20 accounts and approve estimated cost before running the full list.

Risk: Unpinned npm and npx installs may resolve changing packages.

Mitigation: Review the package and resolved version before installing or running it.

Risk: Nonessential attribution reads local agent configuration and writes a Cargo session; the optional star flow writes a persistent marker and can act on a GitHub account.

Mitigation: Decline or remove attribution and starring steps unless needed; review local reads and writes, and require explicit consent before any GitHub action.

Risk: Public buying signals can be mistaken for permission to contact individuals or attributed to the wrong account.

Mitigation: Verify the source, date, and account identity; require an independent outreach basis before contacting anyone.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo tech intent recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/tech-intent.md)
- [Cargo account expansion recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/account-expansion.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown table of dated, linked account signals with brief explanations; optional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports only accounts with relevant signals; includes date, source, and why each signal matters.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
