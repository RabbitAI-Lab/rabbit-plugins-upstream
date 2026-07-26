## Description: <br>
Install a durable Challenge the Direction rule into an agent's AGENTS.md after explicit user approval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[srmhrrm-hub](https://clawhub.ai/user/srmhrrm-hub) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to install a persistent decision-quality rule in a workspace AGENTS.md so future agent sessions challenge weak premises before consequential work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill intentionally changes a workspace AGENTS.md instruction file, which can affect later sessions that load that file. <br>
Mitigation: Review the exact target path and rule block before approving installation, and verify that the rule appears exactly once after editing. <br>
Risk: Installing the rule in the wrong instruction file may fail to affect the intended workspace or may influence an unintended workspace. <br>
Mitigation: Confirm the active AGENTS.md path before editing and rely on the skill's requirement to stop when the target or authority hierarchy is unclear. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/srmhrrm-hub/skills/critical-thinking) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown rule block with concise installation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user approval before editing AGENTS.md; repeated use should be idempotent.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
