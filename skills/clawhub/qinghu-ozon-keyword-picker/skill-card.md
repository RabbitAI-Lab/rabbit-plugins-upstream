## Description:

Helps Ozon sellers use Qinghu keyword data to identify searched terms, inspect demand trends, connect keywords to products, and turn traffic-keyword evidence into product and listing recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Ozon sellers and marketplace analysts use this skill to research Russian keyword demand, compare keyword trends, inspect related products, and create product-selection or listing-optimization recommendations from Qinghu data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Qinghu token is required for data access and could be exposed if pasted into shared transcripts or files.

Mitigation: Provide the token only when needed, prefer environment variables such as QINGHU_TOKEN or QHKIT_TOKEN, and avoid repeating secrets in output.

Risk: Larger result sets may be exported to local files that could contain business-relevant keyword or product research.

Mitigation: Review export paths, avoid using sensitive business data when local storage is not acceptable, and remove generated exports when they are no longer needed.

Risk: Authorized Qinghu API calls can consume credits.

Mitigation: Confirm planned tool calls and expected credit use before execution, and report actual pointCost-derived Qinghu credit consumption after paid calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ozon-keyword-picker)
- [Qinghu login](https://www.iqinghu.com/workbench/login?type=1&urlCode=1788417429126)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries, concise recommendations, and exported table files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports Qinghu credit consumption when paid calls are made; larger result sets are expected to be exported locally instead of pasted into chat.]

## Skill Version(s):

0.1.3 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
