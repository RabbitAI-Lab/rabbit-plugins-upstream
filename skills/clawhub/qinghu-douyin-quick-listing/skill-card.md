## Description:

This skill helps agents collect 1688 product information, manage Douyin shop listing templates through Xiaofeng ERP, publish batches to Douyin stores, and edit listed product titles, images, SKUs, and carousel images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and commerce operators use this skill to source products from 1688, prepare Douyin shop distribution through Xiaofeng ERP, publish listings, and make targeted post-listing edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Qinghu credentials and ERP-authorized Douyin shop data.

Mitigation: Install and run it only when the user is comfortable granting access to Qinghu tokens, authorized shop accounts, and product listing or editing workflows.

Risk: Product listing and editing actions can affect live Douyin shop inventory and customer-facing content.

Mitigation: Use the skill's confirmation gates, preview listings before execution, and submit only fields the user explicitly asked to change.

Risk: Larger result sets may be exported or cached to local files that contain sensitive business data.

Mitigation: Review generated spreadsheets or cached files after use and handle them according to the user's data-retention requirements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-douyin-quick-listing)
- [Qinghu API Endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Xiaofeng ERP Console](https://xfdyorder.zzbtool.com/zzb_super_goods_xf/index.html#/index)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON snippets, shell commands, API-call instructions, and exported local files when larger result sets are returned.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce concise status summaries, failure details, product-edit summaries, authorization links, and local spreadsheet exports for larger datasets.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
