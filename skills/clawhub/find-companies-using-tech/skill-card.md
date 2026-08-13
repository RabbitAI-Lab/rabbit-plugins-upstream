## Description:

Find companies by the technology they run or the roles they are hiring for, powered by Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, growth, and go-to-market teams use this skill to find companies that use specified technologies, are hiring for specified roles, or match both signals. Agents can guide setup, run Cargo CLI searches, and explain sampling and credit-aware execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search criteria and workflow data are sent to Cargo and theirStack during use.

Mitigation: Use an approved Cargo workspace and avoid submitting sensitive criteria unless that data sharing is authorized.

Risk: Cargo CLI actions consume credits, and cost can scale with larger runs.

Mitigation: Start with a 10-20 record sample, report observed cost and hit rate, and get approval before a larger run.

Risk: The workflow requires installing and authenticating the Cargo CLI.

Mitigation: Install the documented @cargo-ai/cli package, verify login with Cargo, and confirm the active workspace before executing searches.

## Reference(s):

- [Cargo GTM Skills Repository](https://github.com/getcargohq/gtm-skills)
- [Cargo Tech Intent Recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/tech-intent.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Cargo CLI commands, JSON payload examples, setup guidance, cost estimates, and result-interpretation guidance.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
