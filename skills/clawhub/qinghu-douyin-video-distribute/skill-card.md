## Description:

Qinghu AI helps agents identify rising Douyin commerce videos, convert Douyin links, gather matching 1688 supply options, and prepare Xiaofeng ERP distribution into Douyin stores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operators and their agents use this skill to discover fast-rising Douyin product videos, evaluate linked product demand, find matching 1688 suppliers, and prepare or execute Douyin store distribution through Xiaofeng ERP.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires Qinghu and Xiaofeng API access for commerce and store-distribution actions.

Mitigation: Confirm the operator is comfortable granting that access before installation or use.

Risk: API tokens may be needed to call Qinghu services.

Mitigation: Prefer environment variables or managed secrets rather than pasting tokens into chat.

Risk: Distribution actions can affect Douyin store listings.

Mitigation: Review the distribution preview and require confirmation before execution.

Risk: Large datasets may be saved as local exported files.

Mitigation: Store and share exports according to the user's data handling requirements.

Risk: Following another seller's product or video can involve brand, patent, or content-rights concerns.

Mitigation: Check product authorization and recreate marketing material rather than directly reusing another creator's video.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-douyin-video-distribute)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Xiaofeng ERP backend](https://xfdyorder.zzbtool.com/zzb_super_goods_xf/index.html#/index)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, files, guidance]

**Output Format:** [Markdown summaries with structured data tables or exported files when datasets are large]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include video lists, supplier details, distribution previews, execution results, failure reasons, and local exported data files.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
