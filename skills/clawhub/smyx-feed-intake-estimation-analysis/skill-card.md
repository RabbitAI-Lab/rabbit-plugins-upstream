## Description: <br>
Estimates daily feed intake per livestock individual from continuous feeder videos by tracking the change of feed remaining in the trough, and outputs intake trend with anomaly alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and farm-management teams use this skill to analyze feeder images, videos, or media URLs and estimate livestock feed intake trends with anomaly alerts. It is intended for visual intake estimation and report lookup, not feeding-ration or nutrition advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends feeder images, videos, or supplied media URLs to lifeemergence.com services for cloud analysis. <br>
Mitigation: Use it only with media approved for external cloud processing and avoid uploading unrelated sensitive footage. <br>
Risk: The skill can create or reuse a local service identity and persist session tokens locally. <br>
Mitigation: Review or clear workspace data files when identity or token reuse is not desired. <br>
Risk: History lookup can query account-scoped cloud reports when broad report-list triggers are used. <br>
Mitigation: Invoke history lookup only when the user clearly intends to retrieve prior feed-intake reports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-feed-intake-estimation-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Feed intake API documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON analysis output with feed-intake estimates, trend labels, anomaly alerts, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts feeder image or video file paths and media URLs; history lookup returns an account-scoped report table.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
