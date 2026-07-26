## Description: <br>
Hire guides users through a conversational setup process for creating a new AI team member, including role design, agent identity files, model selection, OpenClaw config updates, and optional review scheduling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[larsderidder](https://clawhub.ai/user/larsderidder) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent workspace operators use Hire when they want to add a new AI assistant or team member through guided role definition, boundaries, tooling, and setup. The skill helps gather requirements, summarize the proposed role, generate agent files, and update workspace configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make persistent agent files, shared-memory links, OpenClaw configuration patches, main-agent allowlist changes, restarts, and optional cron schedules. <br>
Mitigation: Review the generated files, config patch, allowlist change, restart behavior, and cron schedule before approving or deploying the skill. <br>
Risk: The skill may run in response to broad hiring or create-agent language, which could trigger setup behavior outside an explicitly intended request. <br>
Mitigation: Prefer invoking it only for explicit '/hire' or create-agent requests and confirm the proposed role and boundaries before setup. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/larsderidder/skills/hire) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with generated agent files and configuration patch instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create persistent agent directories, shared USER.md and MEMORY.md links, OpenClaw gateway configuration changes, allowlist updates, restarts, and optional cron schedules.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
