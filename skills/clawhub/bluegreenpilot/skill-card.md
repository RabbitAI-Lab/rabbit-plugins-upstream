## Description: <br>
Guide safe blue-green deployments with persistent repo config, environment state, health checks, explicit switch confirmation, and rollback discipline. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thiagocaltoe](https://clawhub.ai/user/thiagocaltoe) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and release engineers use this skill to plan, verify, promote, switch traffic, and roll back blue-green deployments while keeping environment state, health checks, and rollback paths explicit. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A production traffic switch or rollback could affect live service availability. <br>
Mitigation: Require explicit final confirmation, review the generated plan, and verify rollback steps before any production deployment or traffic change. <br>
Risk: Secrets could be exposed if users place credentials in BlueGreenPilot configuration files. <br>
Mitigation: Keep secrets out of .bluegreenpilot files and use environment variables, CI secrets, or a dedicated secret manager. <br>
Risk: Incorrect active-slot, state-backend, database, or rollback assumptions could lead to unsafe deployment guidance. <br>
Mitigation: Read persistent state, verify environment topology and health checks, and stop when state, rollback, or database policy is unknown. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/ThiagoCAltoe/bluegreenpilot/tree/main/skills/bluegreenpilot) <br>
- [Project homepage](https://github.com/ThiagoCAltoe/bluegreenpilot) <br>
- [ClawHub skill page](https://clawhub.ai/thiagocaltoe/skills/bluegreenpilot) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with deployment plans, checklists, command examples, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires human review and explicit confirmation before state-changing deployment, traffic switch, or rollback actions.] <br>

## Skill Version(s): <br>
2026.6.6 (source: server release metadata; artifact frontmatter reports 2026.6.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
