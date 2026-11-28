## Description:

Helps agents plan content strategy, decide what content to create, and organize topics across content pillars, buyer stages, and editorial priorities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[coreyhaines31](https://clawhub.ai/user/coreyhaines31)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, founders, and content strategists use this skill to turn business context, customer research, keyword data, and competitive gaps into content pillars, prioritized topics, topic clusters, and editorial planning guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read named product-marketing context files that contain sensitive business information.

Mitigation: Review those files before use and avoid including confidential material that should not be used in generated content strategy guidance.

Risk: The headless CMS reference discusses preview tokens and CMS integration concepts.

Mitigation: Handle any CMS preview tokens through normal secret-management practices and avoid placing secrets in skill or prompt text.

## Reference(s):

- [Headless CMS Guide](references/headless-cms.md)
- [ClawHub skill page](https://clawhub.ai/coreyhaines31/skills/content-strategy)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with structured tables, lists, scoring frameworks, and topic maps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask for business, customer, current content, resource, and competitor context before recommending a strategy.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter metadata.version is 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
