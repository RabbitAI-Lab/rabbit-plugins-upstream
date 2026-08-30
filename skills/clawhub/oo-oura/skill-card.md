## Description:

Oura (ouraring.com). Use this skill for ANY Oura request — searching and reading data. Whenever a task involves Oura, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to read Oura wellness, sleep, readiness, heart rate, stress, activity, workout, tag, ring, and account profile data through an OOMOL-connected Oura account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read sensitive wellness and personal Oura account data.

Mitigation: Invoke it deliberately only for tasks that require connected-account data, and treat returned sleep, readiness, heart rate, stress, activity, workout, tag, device, and personal information as sensitive.

Risk: The connector is unnecessary for general Oura questions that do not require account data.

Mitigation: Use non-account sources for general Oura questions and reserve this skill for authenticated data retrieval.

## Reference(s):

- [ClawHub Oura Skill](https://clawhub.ai/oomol/skills/oo-oura)
- [Oura Homepage](https://ouraring.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON responses from the Oura connector]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Oura connector actions return data under a JSON data field with execution metadata.]

## Skill Version(s):

1.0.0 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
