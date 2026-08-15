## Description:

Find B2B leads by job title, company, and keyword, and return them as a structured list, powered by Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, GTM, and recruiting teams use this skill to source person-level B2B prospects by role, company attributes, keywords, and location. It is suited for outbound lead discovery when the user needs named people and profile URLs rather than company lists or email enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses an external Cargo CLI and requires account login, which may store authentication locally through that CLI.

Mitigation: Install only the expected @cargo-ai/cli package, use the documented login flow or API token, and verify the active account with cargo-ai whoami before running searches.

Risk: Lead searches can spend Cargo credits, especially when a batch fans out across many records.

Mitigation: Start with a 10-20 record sample, report observed cost and hit rate, then ask for approval with the record count and estimated credit use before running larger batches.

Risk: Incorrect target profile, provider access, or limit settings can produce irrelevant or overly broad lead results.

Mitigation: Confirm the target role, company criteria, provider access, location, and limit before execution; prefer limits in multiples of 25 because pages return in blocks of 25.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/find-b2b-leads)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command blocks and structured lead-list text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger asynchronous Cargo CLI operations that return run or batch identifiers before results are available.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
