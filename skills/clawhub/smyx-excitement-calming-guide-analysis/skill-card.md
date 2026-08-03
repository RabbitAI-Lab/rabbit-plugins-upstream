## Description: <br>
Analyzes pet activity images or videos for over-excitement signals and produces behavior-safety scoring, calming guidance, and report/history links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Pet owners, boarding and daycare operators, and training schools use this skill to analyze pet activity media for over-excitement indicators and receive behavior-safety guidance and report links. The output is for behavior safety reference, not medical advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Household pet media and report requests may be processed by external lifeemergence.com services. <br>
Mitigation: Use the skill only with media and environments approved for external processing, especially in shared, workplace, or sensitive home-camera contexts. <br>
Risk: The skill may silently create or reuse a local identity and store tokens in a workspace SQLite database. <br>
Mitigation: Review local identity and token handling before deployment, and isolate or clear workspace state according to organizational policy. <br>
Risk: Behavior-safety recommendations may be incorrect or unsuitable for a specific pet or setting. <br>
Mitigation: Treat outputs as guidance for human review, not medical advice or fully autonomous intervention. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-excitement-calming-guide-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown or JSON report text with behavior observations, excitement scoring, calming recommendations, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May retrieve cloud report history and may save report output to a user-specified file.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; SKILL.md frontmatter states 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
