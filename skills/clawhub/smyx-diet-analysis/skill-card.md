## Description: <br>
Analyzes videos to evaluate human eating behaviors, habits, and dietary patterns. It identifies tendencies towards unhealthy eating and provides structured analysis reports along with nutritional improvement recommendations. | 饮食行为健康分析工具，针对人的饮食行为、进食习惯、饮食结构进行视频分析，识别不良饮食行为倾向，提供结构化分析报告和营养改善建议 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to submit meal videos or URLs for dietary behavior analysis, including eating speed, eating habits, diet structure, risk behaviors, and nutrition-oriented recommendations. It can also retrieve cloud-hosted historical analysis reports associated with the resolved user identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Meal videos and report history are sent to configured lifeemergence.com cloud services and associated with an automatically resolved local or cloud identity. <br>
Mitigation: Install and run the skill only where those services and the publisher are trusted, and avoid submitting sensitive health-related media unless that linkage is acceptable. <br>
Risk: The skill may create local workspace data and persist authentication tokens for reuse. <br>
Mitigation: Run it in a workspace with restricted data-directory access, review local data storage before reuse, and clear stored identity or token data when persistence is not desired. <br>
Risk: Dietary behavior output can look like health guidance but is not a medical or nutrition diagnosis. <br>
Mitigation: Treat reports as wellness reference material and consult a qualified clinician or nutrition professional for medical or dietary decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-diet-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, files] <br>
**Output Format:** [Markdown and JSON text, with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured dietary analysis, health warnings, recommendations, report links, and historical report lists.] <br>

## Skill Version(s): <br>
1.0.9 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
