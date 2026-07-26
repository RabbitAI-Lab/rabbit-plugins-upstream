## Description: <br>
Analyzes fixed-camera feeder and waterer images or videos to quantify livestock feeding duration, feeding bouts, drinking frequency, baseline deviations, and behavior anomaly alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Farm operators, livestock managers, and agents use this skill to analyze feeder or waterer camera footage, summarize feeding and drinking behavior, compare activity against historical baselines, and surface non-diagnostic anomaly alerts for husbandry review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using the skill may upload livestock images or videos, or forward video URLs, to a cloud analysis service. <br>
Mitigation: Install and run it only in workspaces where cloud processing of that media is acceptable, and avoid providing footage that contains unrelated sensitive content. <br>
Risk: The skill can query cloud report history and silently manage local account identity, including tokens or profile data in local storage. <br>
Mitigation: Review workspace identity and storage practices before use, restrict access to the workspace, and clear local credentials when the skill is no longer needed. <br>
Risk: Behavior anomaly alerts are observational and are not veterinary diagnosis or treatment advice. <br>
Mitigation: Use results as husbandry decision support and confirm health or treatment decisions through farm procedures and qualified veterinary review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-feed-drink-behavior-monitor-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON-style structured reports with optional report links and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include feeding duration, feeding frequency, drinking frequency, time distribution, baseline deviation level, anomaly level, and cloud report links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
