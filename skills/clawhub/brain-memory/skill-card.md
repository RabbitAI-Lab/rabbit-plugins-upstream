## Description: <br>
Recall and store persistent memories in the user's brain (~/.brain) with the brain CLI: deterministic recall with spreading activation, spaced reinforcement after presenting results, and classified model-driven memorization across life domains (personal, family, social, professional). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[onurkarali](https://clawhub.ai/user/onurkarali) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use Brain Memory to give agents persistent cross-session recall, reinforcement, and memorization through the brain CLI. The skill is intended for workflows where durable personal, project, or relationship context helps future agent responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents receive broad cross-session access to personal memory files in ~/.brain. <br>
Mitigation: Install only when persistent shared memory is intended, review stored memories regularly, and avoid storing secrets or credentials. <br>
Risk: Memory sync may expose sensitive user context outside the local machine if enabled. <br>
Mitigation: Understand whether sync is enabled before use and prefer clear controls to inspect, delete, disable, or scope memories. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/onurkarali/skills/brain-memory) <br>
- [Brain Memory Homepage](https://brainmemory.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read from and write to the user's shared ~/.brain memory store through the brain CLI.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
