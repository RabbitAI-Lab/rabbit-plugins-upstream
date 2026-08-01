## Description: <br>
This skill should be used when users need to translate natural language molecular structure queries into MolQL (Mol-Script) expressions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhonghua-wang](https://clawhub.ai/user/zhonghua-wang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, structural biologists, and molecular visualization users use this skill to translate natural language selection requests into MolQL expressions for Mol* or compatible viewers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The included publish script can publish the skill under an authenticated ClawHub CLI session. <br>
Mitigation: Run the publish script only when intentionally maintaining or releasing the skill. <br>
Risk: Ambiguous molecular selection requests can produce an expression for the wrong ligand, radius, residue scope, or structural feature. <br>
Mitigation: Ask clarifying questions before translating ambiguous active-site, binding-pocket, ligand, radius, or scope requests. <br>


## Reference(s): <br>
- [MolQL Syntax Reference](references/molql-syntax.md) <br>
- [MolQL Translation Examples](references/translation-examples.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/zhonghua-wang/skills/molql) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown with MolQL code blocks and concise explanations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask clarifying questions for ambiguous molecular selection requests.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
