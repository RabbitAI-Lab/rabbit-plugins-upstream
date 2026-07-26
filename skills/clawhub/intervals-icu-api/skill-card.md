## Description: <br>
Guides agents through authenticating with the Intervals.icu API and using curl examples to retrieve, create, update, export, and delete training, calendar, wellness, and sport-settings data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pseuss](https://clawhub.ai/user/pseuss) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, coaches, and athletes use this skill to draft authenticated Intervals.icu API requests for training analysis, calendar management, wellness logging, workout export, and data sync workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Examples can modify or delete real Intervals.icu training, calendar, wellness, and sport-settings records. <br>
Mitigation: Require explicit user confirmation before POST, PUT, bulk, settings, wellness, or DELETE operations and review request payloads before execution. <br>
Risk: API keys and bearer tokens grant access to a user's Intervals.icu account and can be exposed if pasted into shared chats or logs. <br>
Mitigation: Use environment variables or a secret manager for credentials, and avoid writing tokens into reusable prompts, transcripts, or command history. <br>


## Reference(s): <br>
- [Intervals.icu API Documentation](https://intervals.icu/api-docs.html) <br>
- [Intervals.icu OpenAPI Specification](https://intervals.icu/openapi-spec.json) <br>
- [Intervals.icu API Access Forum Discussion](https://forum.intervals.icu/t/api-access-to-intervals-icu/609) <br>
- [Intervals.icu Settings](https://intervals.icu/settings) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash, JSON, and endpoint examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes curl examples for read, write, bulk, export, and settings operations against Intervals.icu API endpoints.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
