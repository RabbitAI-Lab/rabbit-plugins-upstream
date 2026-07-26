## Description: <br>
Runs a three-tier codebase audit with git-history triage, targeted area review, and gated full-codebase review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use this skill to audit branch or release changes, identify churn and instability, and escalate only when evidence supports deeper review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes local audit findings under .coordination/agents, which may include incomplete or sensitive review notes if committed without checking. <br>
Mitigation: Review generated findings files before committing or sharing them. <br>
Risk: Broad review prompts may trigger a multi-tier audit workflow when a narrower review was intended. <br>
Mitigation: Use explicit prompts that define the desired audit scope and tier. <br>
Risk: Full-codebase Tier 3 audits can consume substantial context, compute, and reviewer attention. <br>
Mitigation: Proceed to Tier 3 only after documented Tier 2 justification and explicit user approval. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-tiered-audit) <br>
- [Project homepage from metadata](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown findings files with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes tiered audit findings under .coordination/agents and requires explicit approval before Tier 3 full-codebase audits.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
