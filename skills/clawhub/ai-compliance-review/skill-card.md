## Description: <br>
Reviews Chinese business text for advertising, privacy, finance, labor, and ecommerce compliance risks and returns risk ratings, legal references, and revision suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[g620710](https://clawhub.ai/user/g620710) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business reviewers use this skill to submit Chinese marketing, privacy, financial promotion, labor, ecommerce, or general business text for an AI-generated compliance review. The report is intended as a screening aid and should be reviewed by a qualified human for important legal decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reviewed text and the API key are sent to the publisher's remote service. <br>
Mitigation: Do not submit confidential, personal, regulated, or business-sensitive material unless the backend, retention terms, and authorization to share the data have been verified. <br>
Risk: The shipped script defaults to a plain-HTTP backend endpoint. <br>
Mitigation: Use only after confirming transport security and, where supported, configuring a trusted HTTPS endpoint before sending review content. <br>
Risk: The README-style commands do not match the shipped script interface. <br>
Mitigation: Validate setup and commands against the packaged script before relying on the skill in a workflow. <br>
Risk: AI compliance reviews can miss issues or provide incorrect legal interpretations. <br>
Mitigation: Treat outputs as screening guidance and require human legal or compliance review for important decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/g620710/skills/ai-compliance-review) <br>
- [Publisher profile](https://clawhub.ai/user/g620710) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Text compliance report from the remote service; documentation also describes Markdown and JSON report outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include risk summaries, issue details, legal references, risk levels, scores, and suggested revisions.] <br>

## Skill Version(s): <br>
1.1.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
