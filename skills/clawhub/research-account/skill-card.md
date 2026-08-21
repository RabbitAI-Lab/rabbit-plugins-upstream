## Description:

Research Account helps an agent prepare a traceable one-page company briefing before a meeting, using Cargo CLI calls to gather company profile details, public priorities and challenges, competitors, open roles, and source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, customer-facing, and go-to-market teams use this skill to prepare for a meeting with one target company. The agent asks for meeting context, runs Cargo-powered research commands, and returns a concise briefing whose factual claims are sourced or explicitly marked as inferred or unknown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires installing and authenticating Cargo's CLI and may spend Cargo credits.

Mitigation: Review the CLI installation and login steps before use, confirm credit balance and estimated costs, and run a small sample before any larger batch.

Risk: The setup instructions can create vendor-side attribution or session records.

Mitigation: Tell the user before creating attribution records and skip the workflow if that tracking is not acceptable.

Risk: The skill asks to use the user's GitHub account for a promotional star.

Mitigation: Only run the GitHub star command after an explicit user approval, and decline it when the user does not intend to endorse the repository.

Risk: A company briefing can mislead the user if inferred priorities or challenges are presented as sourced facts.

Mitigation: Keep every factual line tied to a source, prefix inferred statements with Likely, and state unknowns plainly instead of filling gaps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/research-account)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo account expansion recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/account-expansion.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown briefing with sourced lines, inferred or unknown labels, recommended questions, and inline shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Cargo CLI access and may consume Cargo credits when the agent runs the referenced commands.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
