## Description: <br>
Apple Health Skill helps agents query synchronized Apple Health-style fitness data, retrieve workouts and performance metrics, and produce AI coach guidance for training analysis and recovery planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect fitness activity, heart-rate trends, VO2 Max, training load, athlete profile, and coach chat history through a health data sync service. It is suited for training analysis, recovery assessment, and fitness data management workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive health, profile, workout, and chat data. <br>
Mitigation: Use it only with trusted health sync services and avoid exposing returned data in logs, callbacks, or shared transcripts. <br>
Risk: The skill requires an API key for authenticated health endpoints. <br>
Mitigation: Store HEALTH_API_KEY outside source control, keep it private, and rotate it if it may have been exposed. <br>
Risk: The skill requests read, write, and command execution authority. <br>
Mitigation: Run it with the narrowest available agent permissions and review proposed commands before execution. <br>
Risk: Callback URLs can send results to external destinations. <br>
Mitigation: Use callback URLs only when the destination is trusted and expected to receive health-related output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/apple-health-skill) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Health API WOD endpoint example](https://health-api.example.com/api/v1/wod?sport=run&duration=45) <br>
- [Health API coach chat endpoint example](https://health-api.example.com/api/v1/coach/chat) <br>
- [Health API workouts endpoint example](https://health-api.example.com/api/v1/workouts?start=2026-02-09&end=2026-02-15) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON-shaped API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include sensitive health, profile, workout, and coach-chat data returned from the configured health sync service.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
