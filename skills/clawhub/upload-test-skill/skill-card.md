## Description: <br>
Tests whether a skill upload can be recognized, triggered, and produce a basic Markdown output using only de-identified test text. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[li19921117](https://clawhub.ai/user/li19921117) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and release maintainers use this skill to confirm that a ClawHub skill package is uploaded, recognized, triggered, and returning the expected fixed-structure test report in agent environments such as QClaw, OpenClaw, or Codex. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive or real business data could be included in test input. <br>
Mitigation: Use only de-identified sample text; if likely PII or sensitive business data appears, return a risk notice and do not repeat the sensitive fields. <br>
Risk: A successful test report could be mistaken for platform approval. <br>
Mitigation: Treat the report only as a local recognition and trigger check; the skill explicitly does not promise upload platform review results. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/li19921117/upload-test-skill) <br>
- [ClawHub skill page](https://clawhub.ai/li19921117/skills/upload-test-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance] <br>
**Output Format:** [Markdown report with a checklist table, input summary, risk notice, and next-step suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Designed for de-identified test input; likely sensitive input should produce a risk notice without repeating sensitive fields.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
