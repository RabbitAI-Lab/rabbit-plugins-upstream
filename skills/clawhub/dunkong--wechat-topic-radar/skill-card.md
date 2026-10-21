## Description:

Helps WeChat public-account teams identify article topics from keywords, trending searches, and peer-account histories using public article data and heuristic opportunity scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and marketing teams use this skill to compare WeChat article topics, assess competing public accounts, and plan evidence-backed editorial angles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chosen keywords, WeChat account identifiers, and public article URLs are sent to a third-party API.

Mitigation: Share only intended inputs and keep the API key in an environment variable.

Risk: API requests may incur charges, especially when the collection scope expands.

Mitigation: Review the current cost estimate and collection scope before authorizing paid requests.

Risk: Reports and snapshots are written to local files.

Mitigation: Choose output and snapshot paths deliberately and review files before sharing.

Risk: Small or time-sensitive public samples can yield misleading opportunity scores.

Mitigation: Check sample counts and source evidence; treat heuristic rankings as editorial guidance, not guaranteed demand.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dunkong/skills/wechat-topic-radar)
- [We-Media API guide](https://api.we-media.cn/client/ai-guide)
- [We-Media API product documentation](https://api.we-media.cn/client/products)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Files]

**Output Format:** [HTML and Markdown reports; optional Excel and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Topic opportunity scores, article evidence, content gaps, and actual API spending; scores are heuristic, not predictions.]

## Skill Version(s):

1.4.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
