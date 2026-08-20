## Description:

青虎AI 抖音极速上货 helps agents source products from 1688, select Xiaofeng ERP distribution templates, list products to Douyin shops, and edit listed product titles, images, SKU details, and carousel images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and operators use this skill to move products from 1688 sourcing into Douyin shop listings through Qinghu and Xiaofeng ERP workflows, then review or edit listed products after publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can distribute products to Douyin shops or edit existing product records.

Mitigation: Require the agent to restate the link list, selected template, target account, and requested edits, then wait for user confirmation before execution.

Risk: Incorrect templates or broad edits can create listings that require manual cleanup.

Mitigation: Use a preview step where available, fetch current product details before edits, and submit only fields the user explicitly asked to change.

Risk: Qinghu authorization tokens can be read from user input or environment variables for API calls.

Mitigation: Treat tokens as secrets, avoid echoing them in responses or files, and ask users to review the workflow before granting access.

Risk: Large product result sets may be exported to local files.

Mitigation: Keep exported files local unless the user asks to share them, and summarize only the minimum product data needed in chat.

Risk: Some 1688 data collection tools may consume Qinghu credits.

Mitigation: Ask for one clear approval before first paid use in a session and report actual Qinghu credit consumption after paid calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-douyin-quick-listing)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Xiaofeng ERP backend](https://xfdyorder.zzbtool.com/zzb_super_goods_xf/index.html#/index)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON and shell command examples; may include generated local spreadsheet files for larger result sets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports listing or edit outcomes, failure reasons, required user actions, and Qinghu credit consumption when paid tools are used.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
