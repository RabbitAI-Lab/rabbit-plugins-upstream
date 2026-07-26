## Description: <br>
Helps agents create, edit, and test process-oriented skills using test-driven documentation practices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivansslo](https://clawhub.ai/user/ivansslo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to author, revise, and pressure-test agent skills before deployment. It guides agents through skill structure, discovery-focused descriptions, and test scenarios that reveal whether a skill changes agent behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides agents in writing and editing other skills, which can shape future agent behavior. <br>
Mitigation: Review proposed skill changes before deployment and confirm they remain scoped to the intended skill directory. <br>
Risk: Optional publishing or contribution workflows may include git operations. <br>
Mitigation: Inspect proposed commits and remote operations before allowing pushes or publishing steps. <br>
Risk: Skill-authoring guidance may be misapplied to one-off or project-specific conventions. <br>
Mitigation: Use the skill's creation criteria to keep reusable skills separate from project-local instructions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivansslo/skills/writing-skills-2) <br>
- [Server-resolved source provenance](https://github.com/ivansslo/Supwrs/tree/main/skills/writing-skills) <br>
- [Agent Skills specification](https://agentskills.io/specification) <br>
- [Testing Skills With Subagents](testing-skills-with-subagents.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with examples, checklists, tables, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces human-readable skill-authoring and skill-testing guidance for an agent; no executable code is shipped in the skill artifact.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
