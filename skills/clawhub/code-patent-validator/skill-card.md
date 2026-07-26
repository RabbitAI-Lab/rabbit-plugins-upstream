## Description: <br>
Code Patent Validator turns code scan findings into search queries for researching existing implementations before consulting an attorney. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leegitw](https://clawhub.ai/user/leegitw) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering teams use this skill to convert code scan results or described implementation patterns into structured search strategies, evidence maps, and differentiation questions for self-directed research before seeking legal advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat generated search strategies as legal conclusions. <br>
Mitigation: Keep outputs framed as research guidance and consult a qualified patent attorney for legal conclusions or filing decisions. <br>
Risk: Users may disclose confidential invention details in the agent context. <br>
Mitigation: Avoid sharing confidential details unless comfortable placing them in the agent context; redact sensitive implementation details where possible. <br>
Risk: The skill generates queries but does not perform searches, so relying on it alone can leave research incomplete. <br>
Mitigation: Run the generated searches in the recommended sources, document findings systematically, and compare results before making decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/leegitw/skills/code-patent-validator) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown and structured JSON-style research strategy content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates search queries, source priorities, analysis questions, evidence checklists, next steps, and a disclaimer; it does not perform searches or provide legal conclusions.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
