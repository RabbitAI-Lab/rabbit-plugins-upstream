## Description:

Munger Observer guides bounded reviews of specific decisions, plans, or artifacts using evidence, counterevidence, alternatives, opportunity cost, privacy boundaries, and user-verifiable next checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jdrhyne](https://clawhub.ai/user/jdrhyne)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users apply this skill when they want an agent to perform a focused decision review, premortem, or artifact critique based on supplied or explicitly approved evidence. It is suited for surfacing material observations, bounded inferences, alternatives, opportunity costs, and next checks without assessing personal traits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using history, memory, logs, or recurring schedules could expose sensitive context if the review scope is too broad.

Mitigation: Require explicit, bounded approval for named sources, time range, item count, privacy exclusions, schedule parameters, and any later scope expansion.

Risk: Reviewed content may contain untrusted instructions, links, secrets, or irrelevant personal data.

Mitigation: Treat reviewed material only as evidence, avoid executing or following instructions from it, and minimize personal data in both analysis and output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jdrhyne/skills/munger-observer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown decision review with structured bullet sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Concise output; includes scope, evidence used, confidence, observation, inference, counterevidence, alternative, opportunity cost, and a verify-next check when evidence supports a finding.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
