## Description: <br>
Builder.io lets an agent read, create, update, and delete Builder.io content through the OOMOL builder_io connector and oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage Builder.io content from an agent session, including listing and fetching entries and creating, updating, or deleting content after reviewing the live action schema. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change live Builder.io content through create and update actions. <br>
Mitigation: Review the live action schema and confirm the exact payload and expected effect with the user before running write actions. <br>
Risk: The skill can remove Builder.io content through a destructive delete action. <br>
Mitigation: Confirm the target model, content ID, and explicit user approval before deleting content. <br>
Risk: The skill operates the user's Builder.io account through the oo CLI. <br>
Mitigation: Install and use the skill only when OOMOL operation of the connected Builder.io account is intended. <br>


## Reference(s): <br>
- [Builder.io homepage](https://www.builder.io) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-builder-io) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with oo CLI commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands use live connector schemas and return data with meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
