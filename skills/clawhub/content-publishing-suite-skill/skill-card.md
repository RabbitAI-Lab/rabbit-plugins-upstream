## Description: <br>
Turns a fact-checked and compliance-approved final Markdown draft into multi-channel publishing assets for WeChat, LinkedIn, standalone HTML, and archive ledgers; it orchestrates format conversion only and does not auto-publish. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and content operations teams use this skill after editorial approval to convert a reviewed Markdown draft into platform-specific publishing files and a local archive record while keeping publishing actions behind confirmation gates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unreviewed or non-compliant drafts could be converted into publish-ready assets. <br>
Mitigation: Require the input gate: an approved final-check JSON or an explicit reviewed marker with user confirmation before generating assets. <br>
Risk: Generated assets could leak internal notes, pen names, conversation traces, or credentials. <br>
Mitigation: Run the output validation gate and review generated files for internal markers, conversation traces, and credential patterns before publishing. <br>
Risk: Optional Notion or platform publishing could write to the wrong target. <br>
Mitigation: Default to dry-run, list targets, require user confirmation before external action, and read back any write. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/content-publishing-suite-skill) <br>
- [WeChat style reference](references/wechat-style.md) <br>
- [Channel output contracts](references/channel-contracts.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance plus generated HTML, Markdown, JSON, and package manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates local dry-run publishing packages; external writes require target confirmation and readback.] <br>

## Skill Version(s): <br>
1.1.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
