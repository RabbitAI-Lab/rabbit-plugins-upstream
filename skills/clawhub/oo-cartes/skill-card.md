## Description: <br>
Cartes.io lets agents read, create, update, and delete Cartes.io data through the OOMOL oo CLI and cartes connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to manage Cartes.io maps and markers through an OOMOL-connected account. It supports reads, searches, creation, updates, location history, category lookup, and explicit deletion workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can create or update Cartes.io maps, markers, and marker locations in the connected account. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write. <br>
Risk: Destructive actions can delete Cartes.io maps or markers. <br>
Mitigation: Require explicit user approval for the target map or marker before running deletion actions. <br>
Risk: Commands operate through the user's OOMOL-connected Cartes.io account. <br>
Mitigation: Install and use the skill only when the user intends agents to manage that Cartes.io account, and review prompts before approving state-changing operations. <br>


## Reference(s): <br>
- [Cartes.io homepage](https://cartes.io/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands use the OOMOL oo CLI and return connector JSON responses when run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
