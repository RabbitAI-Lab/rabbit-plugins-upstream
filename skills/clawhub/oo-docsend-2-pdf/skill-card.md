## Description: <br>
Docsend2pdf helps an agent convert a DocSend document URL to a PDF through the OOMOL oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill when a task requires converting a specific DocSend document link into PDF download metadata through the Docsend2pdf connector. Users should confirm the document URL is intended for conversion before running it. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Converting a document sends the DocSend URL to OOMOL/Docsend2pdf for external processing. <br>
Mitigation: Confirm the exact URL and intended conversion before running the convert action, and avoid sending sensitive links unless the user accepts that processing. <br>
Risk: First-time setup may require installing the oo CLI from an external installer. <br>
Mitigation: Use the install command only when the CLI is missing and the user trusts the OOMOL installer source. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-docsend-2-pdf) <br>
- [Docsend2pdf homepage](https://docsend2pdf.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown instructions with inline shell commands and JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; converted PDF results are returned as JSON-safe download metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
