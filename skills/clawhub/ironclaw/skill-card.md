## Description: <br>
Safety for AI agents. Real-time threat classification to detect malicious content before it causes agents harm. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samidh](https://clawhub.ai/user/samidh) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External agents and developers use Ironclaw to classify skill files, direct messages, outbound data, and shell commands for safety risks before acting on them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected text submitted for classification is sent to Ironclaw. <br>
Mitigation: Redact secrets, private conversations, proprietary data, and account details before submitting content. <br>
Risk: Ironclaw API keys can grant access to higher service limits if exposed. <br>
Mitigation: Protect any Ironclaw API key and avoid placing live keys in shared prompts, logs, or skill files. <br>
Risk: Safety classifications can be uncertain or incorrect. <br>
Mitigation: Manually review low-confidence results and continue reviewing future skill updates before replacing local files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/samidh/skills/ironclaw) <br>
- [Ironclaw homepage](https://ironclaw.io) <br>
- [Ironclaw API base](https://ironclaw.io/api/v1) <br>
- [Ironclaw documentation](https://ironclaw.io/docs) <br>
- [Published SKILL.md](https://ironclaw.io/skill.md) <br>
- [Published HEARTBEAT.md](https://ironclaw.io/heartbeat.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown with inline HTTP request examples, JSON payloads, and bash snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Remote classification responses include a label and confidence score; anonymous and registered rate limits are described in the skill.] <br>

## Skill Version(s): <br>
1.3.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
