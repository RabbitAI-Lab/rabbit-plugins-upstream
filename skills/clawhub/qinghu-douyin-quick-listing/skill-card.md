## Description:

Helps agents use Qinghu data interfaces and Xiaofeng ERP workflows to source products from 1688, list them to Douyin stores in batches, and edit published product listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and their agents use this skill to move 1688 product candidates through Qinghu data lookup, Xiaofeng ERP authorization, Douyin distribution-template selection, batch listing, and post-listing edits. It is intended for Douyin store listing workflows that require user confirmation before data or listing operations are executed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use Qinghu API tokens from the environment.

Mitigation: Install and run it only in workspaces where Qinghu tokens are intentional and authorized for the task.

Risk: Product, supplier, pricing, or shop account data may be exported to local files.

Mitigation: Use it only where spreadsheet exports of ecommerce data are acceptable, and handle exported files according to the workspace data policy.

Risk: Listing and edit workflows can affect live Douyin store products.

Mitigation: Require user confirmation before tool calls, preview distribution operations before execution, and submit only fields the user explicitly asked to change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-douyin-quick-listing)
- [Qinghu data API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu account login](https://www.iqinghu.com/workbench/login?urlCode=agentch)
- [Xiaofeng ERP backend](https://xfdyorder.zzbtool.com/zzb_super_goods_xf/index.html#/index)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with JSON-RPC request bodies, concise status summaries, and optional exported spreadsheet file links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report listing or edit results, failure reasons, next actions, and Qinghu point consumption when paid calls are made.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
