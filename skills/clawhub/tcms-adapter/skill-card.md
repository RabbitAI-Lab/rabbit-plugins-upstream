## Description: <br>
Channel-adaptation agent that adapts a reviewed core draft into channel-specific publish-ready versions and generates re-promotion material for existing content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing teams and content operators use this skill to adapt reviewed technical product drafts or published articles into WeChat, developer-community, Chinese social, English X, LinkedIn, and sales one-pager formats while preserving source data, product naming, and redaction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated marketing copy may preserve incorrect source claims or produce public-facing wording that is not ready for publication. <br>
Mitigation: Use reviewed source drafts or published article URLs as input, then review channel-specific outputs before publishing. <br>
Risk: Public posts may expose customer names, sensitive details, or inconsistent product naming if the source draft is not prepared correctly. <br>
Mitigation: Apply the skill's self-checks for data preservation, product names, customer redaction, and sensitive information; route official-account, LinkedIn, social, and uncertain English outputs through the documented human review gates. <br>


## Reference(s): <br>
- [TCMS Adapter ClawHub page](https://clawhub.ai/haiyangchenbj/skills/tcms-adapter) <br>
- [Developer community content specification](artifact/references/channel-specs/dev-community.md) <br>
- [LinkedIn content specification](artifact/references/channel-specs/linkedin.md) <br>
- [WeChat official-account content specification](artifact/references/channel-specs/wechat-official.md) <br>
- [X overseas content specification](artifact/references/channel-specs/x-overseas.md) <br>
- [Sales one-pager template](artifact/references/templates/one-pager.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown files with an execution summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are channel-specific drafts under content/adapted/ and may include social posts, article versions, LinkedIn summaries, and sales one-pagers.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
