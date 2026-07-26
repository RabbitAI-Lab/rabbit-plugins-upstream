## Description: <br>
目的地安全指数为旅行者提供基于本地内置公开数据的目的地安全评分、风险提示、排名和多目的地对比。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-planning agents use this skill to compare destination safety, review common risk categories, and collect practical travel-safety reminders before a trip. Its output should be treated as a static planning aid and checked against current official travel advisories for safety-critical decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may mistake static travel-safety scores for current or authoritative safety advice. <br>
Mitigation: Present outputs as planning support and verify safety-critical decisions against current official travel advisories before acting. <br>
Risk: Source freshness, coverage limits, and update frequency are not documented in the artifact. <br>
Mitigation: Require publisher documentation for current official sources, update cadence, and coverage limits before relying on the skill for travel-safety decisions. <br>
Risk: The artifact includes strong safety claims for countries and regions where conditions can change quickly. <br>
Mitigation: Keep disclaimers visible in generated guidance and avoid representing the skill as a live risk-warning service. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [markdown, json, guidance] <br>
**Output Format:** [Markdown reports for successful safety checks, rankings, and comparisons; JSON error objects for unsupported or incomplete requests] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Static local travel-safety dataset; output includes scores, risk notes, safety tips, and emergency phone numbers for supported destinations.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
