## Description: <br>
JF Open Pro AI Pet Care helps developers integrate JF Tech pet-care APIs for service status, pet records, alerts, behavior statistics, and cloud-video-backed monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and integration engineers use this skill to connect applications and automation workflows to JF Tech pet-care services, including pet profile management, anomaly alert review, alert configuration, service switching, and behavior statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires JF Tech app credentials, device identifiers, and authorization tokens that can access pet-care API data and settings. <br>
Mitigation: Use environment variables or a secret manager, avoid storing credentials in TOOLS.md or command history, and rotate tokens if exposure is suspected. <br>
Risk: Some actions can immediately change service state, delete pet records, or disable alert settings. <br>
Mitigation: Review generated commands before execution and require manual confirmation for delete, service switch, and alert-configuration changes. <br>
Risk: Security evidence notes movecard parameter bugs that may affect script reliability. <br>
Mitigation: Test each script in a non-production setup with known credentials and expected API responses before relying on it operationally. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/jftech/skills/jf-open-pro-ai-pet-care) <br>
- [JF Tech developer portal](https://developer.jftech.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python and shell command examples; scripts return formatted text or JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires JF Tech app credentials, device identifiers, and authorization tokens supplied by the user environment.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
