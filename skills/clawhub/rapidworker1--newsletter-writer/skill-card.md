## Description:

Drafts newsletter issues from a brief and selected links, with US email compliance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rapidworker1](https://clawhub.ai/user/rapidworker1)

### License/Terms of Use:

MIT-0

## Use Case:

US newsletter operators, community managers, and solo creators use the skill to turn an issue brief and selected links into a newsletter draft, with compliance reminders and personalization fields for review before sending.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The renderer has a CSV/Markdown input mismatch and a placeholder defect, so generated output may be unreliable.

Mitigation: Correct those defects before relying on the renderer, and manually review each generated issue and compliance check.

Risk: Untrusted inputs or a shared output folder could expose or overwrite newsletter content.

Mitigation: Use trusted inputs and a dedicated output folder.

Risk: The optional Windows executable has not been evaluated; its published hash alone does not establish that it is safe.

Mitigation: Evaluate the optional Windows app separately before use; do not treat the published hash as a safety assessment.

## Reference(s):

- [Newsletter rules](references/newsletter-rules.md)
- [Newsletter issue template](templates/newsletter-issue.md)
- [ClawHub release](https://clawhub.ai/rapidworker1/skills/newsletter-writer)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Markdown newsletter draft with subject, preview text, sections, links, call to action, and footer, plus compliance checks and merge fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves platform personalization tags for the sender to use in their email platform; does not send or schedule campaigns.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
