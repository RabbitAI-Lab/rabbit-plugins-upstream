## Description: <br>
Adapts reviewed core drafts or published articles into channel-specific publish-ready marketing outputs for WeChat, developer communities, Chinese social posts, English X posts, LinkedIn summaries, and sales one-pagers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing and communications teams use this skill to adapt reviewed technical-product drafts into channel-specific publication materials while preserving source data, product naming, and customer redaction. It supports both new multi-channel launches and re-promotion of existing published content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Adapted marketing content may preserve incorrect or unreviewed claims from the source material. <br>
Mitigation: Provide a specific reviewed draft or article URL and review generated posts before publication. <br>
Risk: Sensitive customer names or internal details in the input could be carried into channel outputs. <br>
Mitigation: Carry source redaction through every channel version and require the documented human review steps before publishing. <br>
Risk: Channel outputs can drift from brand naming, approved positioning, or language quality expectations. <br>
Mitigation: Use the channel specifications and brand rules, mark uncertain English text for confirmation, and proofread publication-ready versions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-adapter) <br>
- [Developer community content specification](artifact/references/channel-specs/dev-community.md) <br>
- [LinkedIn content specification](artifact/references/channel-specs/linkedin.md) <br>
- [WeChat official account content specification](artifact/references/channel-specs/wechat-official.md) <br>
- [X overseas content specification](artifact/references/channel-specs/x-overseas.md) <br>
- [Sales one-pager template](artifact/references/templates/one-pager.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown files and a concise execution summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces channel-specific outputs under content/adapted/ when used with workspace write tools.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
