## Description: <br>
面试模拟工具帮助个人求职者进行工程、产品、业务和职能等多岗位模拟面试，并按经验等级调整难度、提供逐题评分和改进建议。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External individual job seekers use this skill to run single-session mock interviews for selected roles, seniority levels, focus areas, and durations. The agent asks interview questions, gives per-question feedback, and produces a scorecard with strengths, gaps, and suggested study areas. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests exec and write capabilities even though the interview simulator primarily operates through chat. <br>
Mitigation: Run it in a restricted workspace and approve command execution or file writes only when the user explicitly asks for a specific action. <br>
Risk: The scanner verdict is suspicious because the requested agent powers are broader than the apparent interview-practice use case. <br>
Mitigation: Prefer a release that removes exec/write access or clearly limits the skill to conversational interview simulation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/interview-sim-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown conversation with interview questions, feedback, scores, and a final scorecard] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured scorecard-style summaries and short command responses such as skip, hint, explain, score, harder, easier, and end.] <br>

## Skill Version(s): <br>
1.0.2 (source: evidence.json release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
