## Description: <br>
Fellow (fellow.app) lets an agent read, list, and update data in a connected Fellow workspace through OOMOL's oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users use this skill to operate a connected Fellow workspace from an agent session. It supports reading meeting notes and action items, checking the current user and workspace, and updating action-item archive or completion state after confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access meeting notes, action items, and workspace details from the connected Fellow account. <br>
Mitigation: Install only when Fellow workspace access is intended, and treat returned meeting notes and action items as sensitive. <br>
Risk: Write actions can archive action items or change their completion state. <br>
Mitigation: Review the exact target, payload, and expected effect with the user before approving any write action. <br>


## Reference(s): <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Fellow homepage](https://fellow.app) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Actions run through the oo CLI; write actions require user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
