## Description:

公众号选题雷达 helps content teams research WeChat public-account topics by analyzing seed keywords, real-time WeChat Search trends, or comparator accounts and producing opportunity scores, matrices, and content-gap reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

External content teams, content strategists, and agents use this skill to find WeChat public-account topic opportunities, evaluate demand and competition, translate trends into durable article angles, and compare account content gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a user-provided Mange Cloud API key and can make paid calls to api.we-media.cn.

Mitigation: Confirm the selected mode, estimated cost, and output paths before running it, and keep API keys out of shared logs and public files.

Risk: Topic opportunity scores are local heuristic rankings based on sampled public search results, so sparse or fast-moving topics may produce low-confidence conclusions.

Mitigation: Review sample counts, confidence labels, source links, and the generated report before using the recommendations for content decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/wechat-topic-radar)
- [Mange Cloud API endpoint](https://api.we-media.cn)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; optional local HTML, Markdown, JSON, and XLSX report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use a user-provided API key, make paid API calls, and save reports or snapshots to local paths selected by the user.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
