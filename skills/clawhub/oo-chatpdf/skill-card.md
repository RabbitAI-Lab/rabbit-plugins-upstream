## Description: <br>
ChatPDF lets agents add public PDF URLs, ask questions against imported PDFs, and delete ChatPDF sources through the OOMOL oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate a connected ChatPDF account from an agent: import public PDF URLs, ask stateless questions about imported PDFs, and delete sources after confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change ChatPDF state by importing public PDF URLs. <br>
Mitigation: Confirm the exact PDF URL and expected effect with the user before running the add action. <br>
Risk: The skill can delete one or more imported ChatPDF sources. <br>
Mitigation: Confirm the target source IDs and obtain explicit approval before running the delete action. <br>
Risk: ChatPDF actions are mediated through the user's OOMOL-connected account. <br>
Mitigation: Confirm the user is comfortable using OOMOL as the intermediary before installation or use. <br>


## Reference(s): <br>
- [ClawHub ChatPDF Skill](https://clawhub.ai/oomol/skills/oo-chatpdf) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [ChatPDF Homepage](https://www.chatpdf.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash and JSON command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target ChatPDF through the OOMOL oo CLI and return JSON responses.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
