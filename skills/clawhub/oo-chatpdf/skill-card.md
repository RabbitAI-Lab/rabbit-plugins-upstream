## Description: <br>
ChatPDF lets agents import PDF URLs, ask stateless questions about imported PDFs, and delete ChatPDF sources through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to operate ChatPDF through an OOMOL-connected account: importing publicly reachable PDF URLs, asking questions against imported PDFs, and deleting sources when explicitly approved. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can add ChatPDF sources through a connected OOMOL account. <br>
Mitigation: Confirm the exact PDF URL payload and expected effect with the user before running write actions. <br>
Risk: The skill can delete one or more ChatPDF sources. <br>
Mitigation: Confirm the target source IDs and obtain explicit user approval before running destructive actions. <br>
Risk: First-time setup, connection, or billing errors may require account actions. <br>
Mitigation: Run setup steps only after a matching command failure and use the documented OOMOL setup, connection, or billing paths. <br>


## Reference(s): <br>
- [ChatPDF homepage](https://www.chatpdf.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands inspect live connector schemas before action execution; write and destructive actions require explicit approval.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
