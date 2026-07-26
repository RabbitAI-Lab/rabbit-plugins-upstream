## Description: <br>
Fast AI/ML conference deadline lookup and submission-window routing that starts from radar sources and verifies decision-critical dates against official CFP, OpenReview, or submission pages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[1587causalai](https://clawhub.ai/user/1587causalai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External researchers, developers, and research teams use this skill to identify urgent AI/ML conference windows, verify decision-critical deadlines, and convert venue timing into submission sprint actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Radar and index pages can be stale, incomplete, or unsuitable as final authority for submission decisions. <br>
Mitigation: Verify decision-critical dates against official CFP, OpenReview, or submission pages and preserve uncertainty labels such as radar_hint, historical_estimate, or unverified. <br>
Risk: The helper may fetch public deadline sources and store a temporary cache during deadline lookup. <br>
Mitigation: Use it only where outbound public web requests and temporary local caching are acceptable, and review environment constraints before relying on helper output. <br>


## Reference(s): <br>
- [Source policy for AI conference deadlines](references/source-policy.md) <br>
- [ClawHub package page](https://clawhub.ai/1587causalai/skills/ai-conference-deadline-radar) <br>
- [MLCIV AI deadlines](https://mlciv.com/ai-deadlines/?sub=ML,CV,CG,NLP,RO,SP,DM,AP,KR,HCI,EDU) <br>
- [CCFDDL conference deadlines RSS](https://ccfddl.com/conference/deadlines_zh.xml) <br>
- [AI Deadlines](https://aideadlines.org/) <br>
- [AI Deadlines alternate index](https://aideadlin.es/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown deadline tables with concise planning guidance and optional shell commands for the helper script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include source status labels, candidate verification links, urgency classes, and next-action recommendations.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
