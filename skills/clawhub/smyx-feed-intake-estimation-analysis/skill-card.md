## Description: <br>
Estimates daily feed intake per livestock individual from continuous feeder videos by tracking the change of feed remaining in the trough, and outputs intake trend with anomaly alerts. | 通过食槽视频估算每日采食量变化，异常时预警。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to estimate livestock feed intake from fixed feeder images or videos, review intake trends, and identify abnormal feeding patterns. It also supports querying prior feed-intake reports associated with the current account identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Feeder images or videos, report queries, and account identity data are sent to lifeemergence.com services. <br>
Mitigation: Install and use only after confirming that these remote-service data flows are acceptable for the workspace and livestock operation. <br>
Risk: The security evidence reports automatic identity creation or reuse and local token storage. <br>
Mitigation: Review identity lifecycle, token storage location, and shared-workspace access before use in sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-feed-intake-estimation-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Feed intake API documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON text, with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include structured intake estimates, trend labels, anomaly alerts, historical report tables, and report links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; skill frontmatter reports 1.0.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
