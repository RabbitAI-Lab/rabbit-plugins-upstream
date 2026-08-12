## Description: <br>
Tracks calories, macros, and weight trends from meal photos, text logs, nutrition labels, and scale logs, with guardrails for medical and eating-disorder risk. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to log meals and drinks, estimate calories and macros, set calorie or protein targets, and interpret weight trends. It is also intended to pause or narrow tracking when medical, pregnancy, underweight, minor, or eating-disorder risk signals are present. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may maintain sensitive food, weight, goal, and health-context notes on the user's machine. <br>
Mitigation: Install only when local storage under ~/Clawic/data/calories/ is acceptable, and review stored notes for privacy-sensitive health details. <br>
Risk: Calorie tracking can worsen harm for users with eating-disorder signals, underweight status, pregnancy or breastfeeding, minors, insulin use, kidney disease, or other medical contexts. <br>
Mitigation: Use the skill's built-in red-flag rules to pause self-derived targets, route medical decisions to clinicians, and let clinician-set targets override the skill. <br>
Risk: Meal, exercise, and weight-trend estimates can be misleading if treated as exact. <br>
Mitigation: Use ranges, 7-day weight averages, measured TDEE after sufficient logs, and conservative exercise-calorie handling as described in the artifact guidance. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/calories) <br>
- [Publisher Profile](https://clawhub.ai/user/ivangdavila) <br>
- [Clawic Skill Page](https://clawic.com/skills/calories) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [Setup](artifact/setup.md) <br>
- [Estimation](artifact/estimation.md) <br>
- [Targets](artifact/targets.md) <br>
- [Safety](artifact/safety.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown or plain text responses with calorie and macro ranges, target calculations, trend summaries, and local log or configuration updates.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses ranges rather than exact calorie claims; may maintain local food, weight, preference, and health-context notes under ~/Clawic/data/calories/.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
