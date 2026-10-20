## Description:

专利查新与可专利性判断。当用户问一个技术方案有没有人做过、能不能申请专利、有没有新颖性或创造性、申请前要做查新、立项前要筛查方向是否被占，或要一份可交付的查新报告时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

External users and patent professionals use this skill to compare an invention disclosure with prior art, assess novelty and inventiveness, and prepare a patent-search report for screening or pre-filing review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Weak service-key protections may expose credentials to misuse.

Mitigation: Use a limited service key from the environment rather than pasting it into chat, and review credential-file protections and redirect restrictions before use.

Risk: Submitting unpublished invention materials may involve sensitive information and provider data-retention or downstream-processing practices.

Mitigation: Before uploading unpublished inventions, review the provider's retention and downstream processing in its privacy policy: https://www.ip930.com/legal/privacy.

Risk: A report submission can incur charges.

Mitigation: Confirm the material, scope, and charge with the user before submitting.

## Reference(s):

- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [ClawHub skill page](https://clawhub.ai/ip930/skills/patent-novelty-cn)
- [Solution guide](artifact/references/solution-guide.md)
- [Workflow guide](artifact/references/workflow.md)
- [FAQ](artifact/references/faq.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files, JSON]

**Output Format:** [Prior-art comparisons, similarity analysis, and novelty conclusions; downloadable DOCX report and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous paid service; confirm scope and charges before submission.]

## Skill Version(s):

1.1.5 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
