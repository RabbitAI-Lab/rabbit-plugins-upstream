## Description:

Qinghu AI's Douyin quick-listing skill helps agents source products from 1688, confirm Xiaofeng ERP authorization and listing templates, publish products to Douyin Shop, and edit listing titles, images, SKUs, and carousel images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operators and agents use this skill to move selected 1688 products into Douyin Shop through Xiaofeng ERP, then review or update published product listings after upload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use a Qinghu API token for Douyin, 1688, and Xiaofeng operations.

Mitigation: Provide the token only through the approved secret or environment variable path, and avoid sharing or logging it in conversation or export files.

Risk: The skill can modify product listings and publish products through external commerce services.

Mitigation: Review the target account, source links, listing template, and proposed changes before approving listing or edit actions.

Risk: Some source-product collection calls may consume Qinghu points.

Mitigation: Confirm the planned tools before paid calls and review the reported Qinghu point consumption after the workflow completes.

Risk: Large result sets may be written to local export files that contain shop or catalog data.

Mitigation: Handle generated exports as business data, share them only with intended recipients, and delete them when no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-douyin-quick-listing)
- [Qinghu data API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Xiaofeng ERP console](https://xfdyorder.zzbtool.com/zzb_super_goods_xf/index.html#/index)

## Skill Output:

**Output Type(s):** [guidance, API Calls, markdown, shell commands, configuration, files]

**Output Format:** [Markdown responses with JSON-RPC request examples, concise status summaries, and optional local export files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports listing or editing results with success counts, failure details, recommended next actions, and Qinghu point consumption when paid calls occur.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
