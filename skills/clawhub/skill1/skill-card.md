## Description: <br>
Self-reflection, self-criticism, self-learning, and self-organizing memory help an agent evaluate its own work, catch mistakes, and improve future behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiaoyu-157](https://clawhub.ai/user/xiaoyu-157) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to keep local memory of corrections, preferences, recurring patterns, and self-reflections so later work can adapt to explicit feedback. It is intended for agents that should transparently learn from mistakes without relying on external services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores local memory about corrections, preferences, and recurring patterns, which may unintentionally retain sensitive user feedback. <br>
Mitigation: Review the stored files periodically, avoid including secrets or sensitive personal data in feedback that may be logged, and clear or disable memory when reuse is no longer wanted. <br>
Risk: Personalization can become inaccurate if weak or one-time signals are promoted into durable rules. <br>
Mitigation: Use the skill's stated promotion rules: ignore silence, treat one-time instructions as local context, and confirm repeated lessons before promoting them to always-loaded memory. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xiaoyu-157/skills/skill1) <br>
- [Server-resolved GitHub provenance](https://github.com/xiaoyu-157/test-import-skill-4/tree/main/skill1) <br>
- [Skill homepage](https://clawic.com/skills/self-improving) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with file paths, tables, and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local memory files under ~/self-improving/ when the user enables the workflow.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter reports 1.2.16) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
