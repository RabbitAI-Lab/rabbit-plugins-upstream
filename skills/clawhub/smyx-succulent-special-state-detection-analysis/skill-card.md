## Description: <br>
AI-powered succulent special-state detection from plant images or videos that identifies black rot, melting, and stretching, then reports condition type, severity, confidence, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, growers, greenhouse operators, and shop staff use this skill to analyze succulent plant images or videos for special abnormal states and review generated analysis reports. Agents can also query prior cloud-hosted reports for the associated internal user identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded plant images, videos, and report-history queries are processed by LifeEmergence remote services. <br>
Mitigation: Use the skill only when that remote processing is acceptable for the workspace and avoid submitting sensitive media. <br>
Risk: The skill can create or reuse internal identity state and store token-bearing account records with limited user control. <br>
Mitigation: Run it in a dedicated workspace where third-party skill code is allowed to consume only intended identity environment variables and local state. <br>
Risk: The security verdict is suspicious even though no individual risk findings were listed. <br>
Mitigation: Review the skill and its remote-service behavior before deployment, and monitor any generated local account or token records. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-succulent-special-state-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Succulent special-state API documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON-oriented analysis text with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include condition type, severity, confidence, suggested observations, historical report tables, and remote report URLs.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
