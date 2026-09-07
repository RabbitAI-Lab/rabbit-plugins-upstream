## Description:

Reviews AI-generated test cases before release, using senior QA sampling across business validity, scenario completeness, and executability to produce correction feedback and prompt-improvement suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA reviewers, test engineers, and delivery teams use this skill to perform final review of AI-generated test cases before they are accepted or published. It supports sampling strategy, issue classification, correction suggestions, and feedback for improving future prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad Chinese review or final-approval phrases when multiple review-related skills are installed.

Mitigation: Use explicit QA test-case review wording when invoking the skill, especially in workspaces with several review skills.

## Reference(s):


## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown review report with test-case tables, review summaries, issue lists, correction suggestions, learning points, and prompt-optimization recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes traceability identifiers such as REV-XXXX review IDs and TC_* test-case IDs.]

## Skill Version(s):

1.7.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
