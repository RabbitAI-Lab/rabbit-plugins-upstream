## Description:

检查 Amazon Listing 的结构、术语、重复表达和评论反映的理解障碍，给出可读性建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to diagnose Listing readability, terminology, repeated phrasing, and review-backed buyer comprehension barriers before deciding what page copy or product information to improve.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a locally stored ARI API key to access ARI account context and Amazon review data.

Mitigation: Use it only with trusted ARI accounts, keep the key out of reports and examples, and rotate or remove the key when access is no longer needed.

Risk: Some VOC or analysis requests may consume ARI credits automatically under account rules without a fresh per-action approval.

Mitigation: Set autoconfirm off or use quote-only wording when execution is not intended, and require explicit confirmation before paid operations that return confirmationRequired.

## Reference(s):

- [Operation Workflow](references/operation-workflow.md)
- [ARI CLI and API Reference](references/reference.md)
- [Skill README](README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Natural-language guidance and Markdown reports, with JSON returned by CLI commands when used directly]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid operations may consume ARI credits under server-side confirmation rules.]

## Skill Version(s):

1.4.7 (source: server release evidence, frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
