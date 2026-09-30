## Description:

Find companies using specified technologies or hiring for specified roles through Cargo's theirStack search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development and marketing teams use this skill to identify companies by technology adoption and recent hiring signals, with evidence for each match.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cargo login and networked company searches expose account and query activity to the service.

Mitigation: Use an approved Cargo account and share only searches appropriate for that service.

Risk: Provider searches consume credits, and large batches can incur substantial charges.

Mitigation: Start with a small sample, check observed cost and match rate, and approve the estimated cost before scaling up.

Risk: The skill includes unrelated attribution logging and inspection of local agent configuration.

Mitigation: Review and omit those steps unless their behavior is explicitly acceptable.

Risk: The optional GitHub star uses an authenticated account and creates a public endorsement.

Mitigation: Do not run the star command without explicit user consent.

Risk: CLI installation references an unpinned latest package version.

Mitigation: Review and pin the package version before installing.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo tech-intent recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/tech-intent.md)
- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/find-companies-using-tech)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown company lists with match evidence and optional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provider searches consume credits; results depend on available technology and hiring data.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
