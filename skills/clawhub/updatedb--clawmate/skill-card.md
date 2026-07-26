## Description: <br>
ClawMate helps agents search and preview files, manage feedback workflows, and initialize or plan ClawMate projects through Phase I-V project workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[updatedb](https://clawhub.ai/user/updatedb) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to work with local ClawMate projects: finding preview links for files, listing projects, processing feedback, and creating or updating project planning documents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A misconfigured CLAWMATE_URL could direct ClawMate requests to an unintended service. <br>
Mitigation: Configure CLAWMATE_URL only for a trusted ClawMate service and avoid pointing it at untrusted hosts. <br>
Risk: Project initialization and feedback workflows can create directories, write files, and initialize Git repositories. <br>
Mitigation: Review the proposed target paths and confirm before running workflows that modify the filesystem. <br>


## Reference(s): <br>
- [Clawmate on ClawHub](https://clawhub.ai/updatedb/skills/clawmate) <br>
- [ClawMate project homepage](https://github.com/updatedb/clawmate) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated preview links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local project files when the user confirms workflows that modify the filesystem.] <br>

## Skill Version(s): <br>
2.7.2 (source: release metadata and artifact/_meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
