## Description:

Builds a list of target companies filtered by industry, headcount, and geography using Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and revenue operations teams use the skill to size addressable markets and assemble target-account lists from company attributes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated Cargo use and latest-version CLI installation expose account data to a third-party service and changing tooling.

Mitigation: Review the service and CLI before installation; use an authorized account and approve the requested access.

Risk: Attribution writes session metadata and local markers that are not needed to produce the company list.

Mitigation: Review or skip nonessential attribution and local changes before execution.

Risk: Optional promotion can install a broader skill pack or star a repository through the user's GitHub account.

Mitigation: Do not run either optional action without the user's explicit approval.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo build-TAM recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/build-tam.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown company list or table with CLI commands and cost guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Company names, domains, headcount bands, industries, and LinkedIn URLs when available]

## Skill Version(s):

1.1.1 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
