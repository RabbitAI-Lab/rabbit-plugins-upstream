## Description: <br>
This is a simple client for connecting to an mqtt instance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[enchantedmotorcycle](https://clawhub.ai/user/enchantedmotorcycle) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to run a short-lived MQTT client that connects to a broker with environment-provided credentials and observes broker messages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The client may subscribe to all MQTT topics visible to the configured credentials and print raw message payloads. <br>
Mitigation: Use least-privilege MQTT credentials, avoid accounts with access to sensitive topics, and prefer or patch a version that honors MQTT_TOPIC and redacts payloads by default. <br>
Risk: The bootstrap script loads connection details from a .env file before running the client. <br>
Mitigation: Inspect the .env file before execution, store only the required MQTT settings, and run the skill in an isolated workspace or user context. <br>


## Reference(s): <br>
- [MQTT](https://mqtt.org/) <br>
- [ClawHub Skill: Mqtt Client](https://clawhub.ai/enchantedmotorcycle/skills/mqtt-client) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Terminal log output and Markdown setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs for 60 seconds and prints connection status plus received MQTT topic payloads to stdout.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
