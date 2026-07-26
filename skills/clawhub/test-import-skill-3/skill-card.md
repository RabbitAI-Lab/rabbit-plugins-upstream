## Description: <br>
Self-reflection + Self-criticism + Self-learning + Self-organizing memory. Agent evaluates its own work, catches mistakes, and improves permanently. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiaoyu-157](https://clawhub.ai/user/xiaoyu-157) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and developers use this skill to record explicit corrections, self-reflections, and recurring patterns in local memory so future work can follow confirmed preferences and avoid repeated mistakes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill persists local notes about corrections, preferences, and repeated patterns. <br>
Mitigation: Avoid storing secrets or sensitive personal details, and use the documented forget and export patterns to review or remove stored memory. <br>
Risk: Incorrect or over-promoted memories can cause repeated behavior changes. <br>
Mitigation: Log explicit corrections and self-reflections, promote lessons only after repeated evidence, and ask before confirming persistent rules. <br>
Risk: Memory context may be incomplete when local files are unavailable or too large to load. <br>
Mitigation: Load the HOT memory first, load only relevant project or domain namespaces on demand, and tell the user when memory was not loaded. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/xiaoyu-157/skills/test-import-skill-3) <br>
- [Server-Resolved GitHub Repository](https://github.com/xiaoyu-157/test-import-skill-3) <br>
- [Skill Homepage](https://clawic.com/skills/self-improving) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with tables, filesystem paths, and short command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local memory files under ~/self-improving/ when the agent applies the skill.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata); artifact frontmatter reports 1.2.16 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
