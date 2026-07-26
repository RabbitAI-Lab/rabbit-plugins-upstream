## Description: <br>
Pre-flight safety check for planned agent actions with permission gates, allowlists, risk scoring, and audit output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agent platform teams, and security reviewers use this skill to evaluate planned shell or agent actions before execution and receive allow, warn, or deny decisions with reasons. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The curl install path downloads a raw file at install time, which may change outside the reviewed artifact. <br>
Mitigation: Review or pin the downloaded raw file before using the curl install path. <br>
Risk: The CI verifier intentionally executes local Python self-tests. <br>
Mitigation: Run the CI verifier only against trusted folders. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itspremkumar/skills/agent-guardrails) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; the CLI emits plain text or JSON decision records.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local stdlib Python execution; no network or telemetry behavior is described in the artifact.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
