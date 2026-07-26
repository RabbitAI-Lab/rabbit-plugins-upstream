## Description: <br>
Apple Health Skill helps users query workouts, heart-rate trends, activity rings, VO2 Max, performance management metrics, and related health data through an AI coaching workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an authorized health-data sync service, query training and wellness metrics, and receive personalized training or recovery guidance from an AI coach. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process sensitive Apple Health, wearable, training, and chat-history data through an external health service. <br>
Mitigation: Use only a trusted health service, avoid sending unnecessary identifiers or chat history, and review data-sharing expectations before connecting real health data. <br>
Risk: Callback URLs can expose results or notifications to destinations outside the user's control. <br>
Mitigation: Configure callbacks only to endpoints the user controls and trusts. <br>
Risk: API keys used for authenticated endpoints can grant access to health data if exposed. <br>
Mitigation: Store HEALTH_API_KEY outside source control, avoid logging it, and rotate the key if disclosure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/apple-health-skill) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include health-data summaries, API request examples, execution logs, and training recommendations; authenticated endpoints require HEALTH_API_KEY.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
