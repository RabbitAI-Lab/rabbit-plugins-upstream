## Description: <br>
Analyzes pet feeding-area videos or video URLs to detect selective refusal behaviors such as pushing staple food from the bowl, eating only treats, or sniffing and leaving, then returns frequency tracking and feeding-adjustment suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet owners, smart-feeder operators, boarding centers, and pet hospital staff use this skill to analyze feeding-area media for picky-eating behavior and receive a structured behavior report with non-diagnostic feeding guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet videos and report history may be sent to remote services. <br>
Mitigation: Use the skill only with media and account context that the user intends to associate with the remote service. <br>
Risk: The skill automatically creates or reuses identities and stores tokens locally. <br>
Mitigation: Review the workspace data directory before installation and use an isolated workspace when handling sensitive account context. <br>
Risk: Cloud history retrieval has limited user control. <br>
Mitigation: Confirm the active account context before requesting history and avoid using shared or unintended accounts. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-picky-eater-detection-analysis) <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown report or JSON detail output, with optional saved text output file and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are behavior-analysis references and do not provide disease diagnosis or treatment advice.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact SKILL.md frontmatter says 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
