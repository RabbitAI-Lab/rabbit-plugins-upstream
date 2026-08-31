## Description:

Checks whether QA testing requests include a clear requirement description and enough context before downstream test design begins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, test designers, and development teams use this skill as the first step in a testing workflow to determine whether an incoming requirement, attachment, or requirement URL has enough detail to support useful test design.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read requirement files or fetch requirement URLs supplied by the user, which can expose customer, financial, identity, or production data.

Mitigation: Mask or remove sensitive data before providing files, URLs, screenshots, or requirement text.

Risk: The security review notes a quality issue where the skill can drift from validation into generating test cases.

Mitigation: Treat any fallback test cases as a non-authoritative draft and require missing information before using downstream test design outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-input-validation)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or JSON-style structured validation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include pass, fail, or need_more_info status, an input quality score, missing information, clarification questions, and a recommendation.]

## Skill Version(s):

1.7.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
