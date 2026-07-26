## Description: <br>
Decision Forensics reconstructs the decision actually made in messy Slack, email, or meeting text into a decision record with commitments, assumptions, dismissed options, and reconstruction confidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external collaborators, and project teams use this skill to turn messy decision discussions into a clear reconstructed record that identifies what was decided, who committed to what, what assumptions were inferred, and what questions remained unresolved. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided Slack, email, or meeting text may contain confidential business decisions or personal information. <br>
Mitigation: Only provide discussions the user is authorized to share, and redact sensitive information when appropriate. <br>
Risk: The reconstructed decision record may overstate agreement or misattribute commitments if the source discussion is ambiguous. <br>
Mitigation: Require quoted or near-quoted evidence for attributions, label assumptions as reconstructed, and review the confidence grade before relying on the record. <br>


## Reference(s): <br>
- [Decision Forensics on ClawHub](https://clawhub.ai/mohitagw15856/skills/decision-forensics) <br>
- [Decision Forensics homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/decision-forensics.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown decision record with tables, quoted evidence, reconstructed assumptions, and a confidence note] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided discussion text and preserves uncertainty by labeling reconstructed assumptions and confidence.] <br>

## Skill Version(s): <br>
50.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
