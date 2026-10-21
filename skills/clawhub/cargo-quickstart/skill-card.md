## Description:

Guides a new Cargo user from a buyer persona to a lead list, credit receipt, and optional recurring search play.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

New Cargo users and sales teams use this skill to find leads matching a buyer persona, review the credit cost, and optionally save the search as a recurring play.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid lead or job searches can consume credits, particularly when falling back to another provider.

Mitigation: Confirm the provider, result limit, and estimated credit cost before each paid search or fallback; require explicit approval before exceeding the initial budget.

Risk: The fallback instructions can switch data providers without informing the user.

Mitigation: Disclose any provider change and obtain approval before running the alternative search.

Risk: Installing the latest CLI release and saving a recurring play can change behavior or create ongoing searches.

Mitigation: Prefer a pinned CLI version and review the schedule, provider, and expected ongoing credit use before approving a recurring play.

## Reference(s):

- [Cargo Quickstart on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-quickstart)
- [Cargo skills homepage (publisher-declared)](https://github.com/getcargohq/cargo-skills)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown lead table, credit receipt, and optional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports actual matches and credit use; proposes a recurring play for explicit approval.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
