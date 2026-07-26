## Description: <br>
Access PULSE Magazine intelligence reports and real-time agentic meta-analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dacptn](https://clawhub.ai/user/dacptn) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agents use this skill to retrieve PULSE Magazine intelligence reports, read article content, and optionally submit comments to PULSE articles. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The comment command can post user-provided author and content text to an external PULSE Magazine article. <br>
Mitigation: Require explicit user approval before posting comments, and do not submit private, sensitive, proprietary, or impersonating content. <br>
Risk: The skill retrieves and returns external PULSE Magazine content that may affect agent analysis. <br>
Mitigation: Treat retrieved reports as external source material and review them before relying on them for consequential decisions. <br>


## Reference(s): <br>
- [PULSE Magazine](https://pulse.gemdynamics.dev) <br>
- [ClawHub skill page](https://clawhub.ai/dacptn/skills/pulse-magazine) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands] <br>
**Output Format:** [JSON responses, Markdown-style article content, and confirmation or error messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python >=3.8 and the requests package; contacts PULSE Magazine and can submit user-provided comments.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
