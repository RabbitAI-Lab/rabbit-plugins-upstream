## Description: <br>
Searches and analyzes DEV environment server logs for trace IDs, request IDs, orders, request records, and transaction failures across procurement, platform, supplier, and order services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[extraskittles](https://clawhub.ai/user/extraskittles) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to investigate DEV test-environment issues by running log searches, downloading matched logs, and summarizing root causes from transaction traces and supplier request/response payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can retrieve, save, and display sensitive DEV backend logs and raw supplier HTTP request/response payloads. <br>
Mitigation: Install only for authorized DEV log-system users; review and redact tokens, identifiers, order data, URLs, and personal data before sharing outputs. <br>
Risk: Downloaded logs and optional configuration may persist locally after an investigation. <br>
Mitigation: Treat ~/.DEV_SKILL/dev-find-log/config.json and executeId log directories as sensitive, and delete old investigation directories when they are no longer needed. <br>


## Reference(s): <br>
- [DEV log system API reference](references/api.md) <br>
- [DEV transaction service-layer mapping](references/service-layers.md) <br>
- [ClawHub skill listing](https://clawhub.ai/extraskittles/skills/zzrtest) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Markdown, Analysis, Configuration guidance] <br>
**Output Format:** [Markdown analysis with shell commands, JSON command output, and downloaded log files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save log downloads and local configuration under ~/.DEV_SKILL/dev-find-log/.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
