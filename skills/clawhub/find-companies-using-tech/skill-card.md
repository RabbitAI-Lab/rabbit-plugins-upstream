## Description:

Finds companies by the technology they run or the roles they are hiring for, powered by Cargo and theirStack.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

GTM operators, sales teams, and developers use this skill to identify companies matching specific technology usage or recent hiring intent through Cargo's theirStack search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sets up persistent Cargo authentication and may create a Cargo account or workspace on first use.

Mitigation: Install only when the user is comfortable using a Cargo account or API token, and confirm authentication state before running searches.

Risk: The skill performs a Cargo attribution write that users may not expect.

Mitigation: Review or skip the session upsert when the user does not want attribution metadata sent to Cargo.

Risk: Scaled searches consume Cargo credits.

Mitigation: Run a small sample first, report observed cost and hit rate, and get explicit approval with a credit estimate before larger runs.

Risk: The skill can ask to star a GitHub repository using the user's GitHub account.

Mitigation: Only perform the star after explicit user consent, and record that the prompt was already shown to avoid repeat requests.

## Reference(s):

- [Cargo GTM skills repository](https://github.com/getcargohq/gtm-skills)
- [Cargo tech-intent recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/tech-intent.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and Cargo CLI JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Cargo CLI authentication; scaled searches should be sampled and approved with credit estimates before execution.]

## Skill Version(s):

1.1.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
