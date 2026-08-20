## Description:

Helps Ozon sellers use Qinghu keyword rankings, keyword details, trend snapshots, related products, and product traffic keywords to choose products based on real search demand.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Ozon sellers and ecommerce operators use this skill to find keyword-driven product opportunities, inspect demand trends, compare related products, and turn traffic keywords into product and listing guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send Ozon keyword research queries and Qinghu API credentials to iqinghu.com.

Mitigation: Use only approved Qinghu credentials, confirm the user is comfortable with the API call, and avoid sharing unrelated sensitive data in keyword research prompts.

Risk: Large result sets may be written to local files.

Mitigation: Review exported files before sharing them and store them according to the user's data-handling expectations.

Risk: Paid Qinghu tools can consume account credits.

Mitigation: Request one clear authorization before paid calls and report actual Qinghu credit consumption using the returned pointCost value.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ozon-keyword-picker)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown summaries with optional exported table files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large result sets are exported to local table files; concise replies include a delivery link, a short explanation, and a small preview.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
