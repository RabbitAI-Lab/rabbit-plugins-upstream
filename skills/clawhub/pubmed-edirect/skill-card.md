## Description: <br>
Search and retrieve literature from PubMed using NCBI's EDirect command-line tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[killgfat](https://clawhub.ai/user/killgfat) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, researchers, and literature reviewers use this skill to run NCBI EDirect searches, retrieve PubMed records, and extract structured biomedical literature data from local shell workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires manually installed command-line tools that execute locally. <br>
Mitigation: Download EDirect only from the official NCBI source, review the installer before execution, and avoid running installation or examples as root. <br>
Risk: EDirect commands contact NCBI services and example workflows can create or overwrite local output files. <br>
Mitigation: Run commands in a dedicated workspace, review output paths before execution, and keep network access expectations visible to users. <br>
Risk: Optional NCBI API keys or email addresses may be stored in shell configuration. <br>
Mitigation: Protect API keys and email configuration as local credentials and avoid exposing them in shared logs, scripts, or workspaces. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/killgfat/skills/pubmed-edirect) <br>
- [NCBI EDirect Documentation](https://www.ncbi.nlm.nih.gov/books/NBK179288/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Files] <br>
**Output Format:** [Markdown guidance with shell command examples and script-generated text, CSV, XML, or abstract files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may contact NCBI services and write local result files.] <br>

## Skill Version(s): <br>
0.4.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
