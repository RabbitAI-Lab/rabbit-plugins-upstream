## Description:

Creates a source-traceable, one-page company briefing for sales meeting preparation using Cargo and public company information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Account executives and sales development teams use this skill to prepare a sourced company briefing, identify publicly stated priorities and competitors, and formulate questions for a meeting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes vendor attribution and a local plugin check unrelated to preparing the briefing.

Mitigation: Review those optional setup steps before running them, and only share session information intentionally.

Risk: A GitHub star prompt uses local state and can act through the user's GitHub account.

Mitigation: Review the persistent marker file and star prompt; star only with explicit user consent.

Risk: Research calls consume Cargo credits, especially when repeated across accounts or when many job postings are returned.

Mitigation: Estimate cost, cap job results, and request approval before running a batch.

Risk: An optional full-pack install adds more skills than this standalone briefing requires.

Mitigation: Skip the full-pack install unless the broader set of Cargo skills is wanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/research-account)
- [Cargo skill homepage (listed in Clawdis metadata; not verified provenance)](https://github.com/getcargohq/gtm-skills)
- [Related account-expansion recipe (linked in skill)](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/account-expansion.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [One-page Markdown briefing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Labels sourced, inferred, and unknown claims; includes three suggested meeting questions.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
