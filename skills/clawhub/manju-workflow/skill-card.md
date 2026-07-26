## Description: <br>
This skill orchestrates an end-to-end manju production workflow from creative direction through storyboard validation, art prompts, animation prompts, editing plans, and external tool instructions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samwang-001](https://clawhub.ai/user/samwang-001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creative teams and agent users use this skill to turn a manju concept into a complete production package, including storyboard tables, image prompts, video prompts, editing guidance, and external tool steps. It is intended for workflows where the five companion Manju skills are installed and reviewed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording may cause the workflow to activate more often than intended. <br>
Mitigation: Install it only in contexts where manju production requests are expected, and review activation behavior before broad deployment. <br>
Risk: The skill can produce a long end-to-end production package from a single request. <br>
Mitigation: Review the generated package before using it in external image, video, or editing tools. <br>
Risk: The workflow depends on five companion skills for role-specific rules. <br>
Mitigation: Confirm all companion skills are installed, current, and reviewed before relying on the full workflow. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/samwang-001/manju-skills/tree/main/manju-workflow) <br>
- [ClawHub skill page](https://clawhub.ai/samwang-001/skills/manju-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown production package with tables, prompts, checklists, and external tool instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the manju-director, manju-writer, manju-artist, manju-animator, and manju-editor companion skills for the full workflow.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
