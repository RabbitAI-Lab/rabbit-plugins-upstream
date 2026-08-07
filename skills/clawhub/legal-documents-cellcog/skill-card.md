## Description: <br>
Legal Documents helps agents draft contracts, NDAs, policies, legal research memos, and compliance materials through CellCog while reminding users that outputs are not legal advice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cellcog](https://clawhub.ai/user/cellcog) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask CellCog to draft legal documents, legal policies, compliance materials, and research-oriented legal memos from natural language prompts. Outputs are starting points for review, not legal advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Legal and business prompts can contain sensitive information that is sent to CellCog's remote service. <br>
Mitigation: Confirm the organization is comfortable using CellCog as a third-party service before submitting sensitive material. <br>
Risk: AI-generated legal documents or research can be incomplete, inaccurate, or unsuitable for a specific jurisdiction. <br>
Mitigation: Have important legal documents reviewed by a qualified attorney before execution or use in high-value, regulated, or jurisdiction-specific matters. <br>
Risk: CELLCOG_API_KEY exposure could allow unauthorized use of the CellCog service. <br>
Mitigation: Store the API key in a protected environment variable, avoid committing it to files, and rotate it if exposure is suspected. <br>
Risk: Higher CellCog chat modes may consume significant credits. <br>
Mitigation: Use the normal agent mode for routine drafting and monitor credit usage before selecting deeper chat modes. <br>


## Reference(s): <br>
- [Legal Documents on ClawHub](https://clawhub.ai/cellcog/skills/legal-documents-cellcog) <br>
- [CellCog](https://cellcog.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Python examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, CELLCOG_API_KEY, and the CellCog client or skill dependency.] <br>

## Skill Version(s): <br>
1.0.14 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
