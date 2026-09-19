## Description:

Structured decision modifiers (/think, /verify, /adversarial, /edge, /confidence, /assumptions, etc.) stress-test conclusions, evidence, assumptions, alternatives, and edge cases when validating an important design, architecture decision, or ambiguous plan before committing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, architects, and decision makers use this skill to apply structured prompt modifiers that validate design choices, compare alternatives, expose assumptions, and flag edge cases before committing to a plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ordinary phrases such as asking whether an answer is right or requesting a code review may trigger a more structured verification format than expected.

Mitigation: Use the skill for important decisions, architecture choices, code reviews, security-sensitive validation, and ambiguous planning where the additional structure is useful.

Risk: Structured analysis can still be misleading if the underlying evidence is incomplete or the assumptions are wrong.

Mitigation: Check that outputs distinguish observed evidence, inference, assumptions, and uncertainty before relying on the recommendation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-meta-prompting)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON response structures with decision records, comparison tables, confidence tiers, and verification markers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May auto-trigger for architecture decisions, code reviews, security-sensitive validation, and ambiguous planning; combined modifiers compose left-to-right.]

## Skill Version(s):

4.6.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
