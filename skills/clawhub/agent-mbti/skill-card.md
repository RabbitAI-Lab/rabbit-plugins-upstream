## Description: <br>
Agent Mbti diagnoses an AI agent's MBTI-style behavior preferences, compares them with a user's desired personality profile, and produces a diagnostic report with style and configuration recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[torchesfrms](https://clawhub.ai/user/torchesfrms) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, agent operators, and users use this skill to assess an agent's MBTI-style behavior pattern, compare it with the user's desired interaction style, and produce guidance for communication, proactivity, reasoning, and execution preferences. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: MBTI-style output may be mistaken for authoritative psychology, safety policy, or a definitive evaluation of an agent. <br>
Mitigation: Treat the report as preference guidance only, and review recommendations before using them to change agent behavior. <br>
Risk: Style recommendations could conflict with normal task, privacy, or safety instructions. <br>
Mitigation: Keep existing task, privacy, and safety requirements authoritative when applying any suggested behavior adjustments. <br>


## Reference(s): <br>
- [Agent MBTI skill page](https://clawhub.ai/torchesfrms/skills/agent-mbti) <br>
- [Agent self-assessment survey](references/survey-free.json) <br>
- [User preference survey](references/user-survey-free.json) <br>
- [Scoring rules](references/scoring.md) <br>
- [Personality type reference](references/personality-types.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown diagnostic report with MBTI-style scores, type comparison, match analysis, and recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local questionnaire and scoring references; no risky system access is requested by the skill evidence.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
