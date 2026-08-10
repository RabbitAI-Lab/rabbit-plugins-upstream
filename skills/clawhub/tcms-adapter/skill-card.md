## Description:

TCMS Adapter adapts a reviewed core draft or published article into channel-specific publish-ready versions for WeChat, developer communities, Chinese social posts, English X posts, LinkedIn summaries, and sales one-pagers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing and communications teams use this skill to adapt already-reviewed technical product content into channel-specific drafts while preserving data points, conclusions, product naming, and customer redaction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated channel drafts may omit, distort, or overstate source data when adapting content for shorter formats.

Mitigation: Review generated material before publishing and compare key claims against the reviewed draft or published article.

Risk: Customer names or sensitive details could be carried into adapted versions if the source content is not properly redacted.

Mitigation: Confirm customer redaction before publication and use the skill's self-check to preserve redaction across all channels.

Risk: English X and LinkedIn outputs may need tone, accuracy, or language review before external publication.

Mitigation: Route English outputs through human proofreading when the skill marks uncertain wording or when publishing from company-controlled channels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-adapter)
- [Developer community channel specification](references/channel-specs/dev-community.md)
- [LinkedIn channel specification](references/channel-specs/linkedin.md)
- [WeChat official account channel specification](references/channel-specs/wechat-official.md)
- [X overseas channel specification](references/channel-specs/x-overseas.md)
- [Sales one-pager template](references/templates/one-pager.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown files with channel-specific drafts and an execution summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are generated only from the reviewed draft or published article supplied by the user.]

## Skill Version(s):

1.1.2 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
