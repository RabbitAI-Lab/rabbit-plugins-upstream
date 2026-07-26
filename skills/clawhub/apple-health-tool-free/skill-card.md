## Description: <br>
Apple Health Tool Free helps agents answer personal Apple Health questions by calling the Transition API for workout, heart-rate, activity-ring, VO2 Max, and coaching queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal users use this skill with an agent to query and summarize Apple Health data synced through Transition. It is intended for fitness tracking, routine health self-checks, trend review, and basic AI coaching conversations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive Apple Health data through an external Transition API. <br>
Mitigation: Use it only when the user intends to query Transition-backed Apple Health data, limit health-data permissions where possible, and avoid sharing sensitive outputs beyond the intended agent session. <br>
Risk: The artifact shows API key setup in shell profiles, env files, and optional local configuration. <br>
Mitigation: Treat the Transition API key like a password, keep it out of repositories and transcripts, prefer environment variables or a secret store, and review any file writes before accepting them. <br>
Risk: Security evidence notes broad activation wording and inconsistent free-tier capability instructions. <br>
Mitigation: Invoke the skill only for Apple Health and Transition tasks, verify current free-tier limits before relying on results, and avoid using it for generic data analysis. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/apple-health-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples, shell commands, and optional Python snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured API responses, execution logs, local configuration examples, and cache-file examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
