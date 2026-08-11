## Description:

Analyzes images or videos of plant roots in transparent pots or seedling boxes to return visual health findings, a 0-100 root health score, vitality grade, care guidance, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, growers, plant factory operators, hydroponic maintainers, and developers use this skill to analyze clear root images or videos for visible signs of root stress or rot and to retrieve cloud-hosted historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Root images, videos, or media URLs are sent to the vendor cloud service.

Mitigation: Use only with content approved for that vendor service and avoid sensitive or regulated imagery unless the publisher documents retention, access, and deletion controls.

Risk: The skill can create or reuse an identity without prompting and stores account tokens or profile data in a shared workspace database.

Mitigation: Run in a scoped workspace, review token storage before deployment, and ask the publisher to document identity creation, token lifecycle, and cleanup behavior.

Risk: Cloud report-history access has incomplete user-facing disclosure.

Mitigation: Confirm which reports are retrievable for the active identity and disclose history retrieval behavior to users before enabling the skill.

Risk: Pet-health remnants in API names and documentation may create ambiguity about the plant-root workflow.

Mitigation: Ask the publisher to remove or explain unrelated pet-health references before using the skill in sensitive workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-root-health-transparent-pot-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with report links; optional saved output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local image/video file paths, public media URLs, and cloud report-history listing.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
