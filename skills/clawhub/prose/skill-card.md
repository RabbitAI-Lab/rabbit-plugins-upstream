## Description: <br>
OpenProse VM skill pack. Activate on any `prose` command, .prose files, or OpenProse mentions; orchestrates multi-agent workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mondilo1](https://clawhub.ai/user/mondilo1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use Prose to run, compile, author, and inspect `.prose` workflows that orchestrate multi-agent sessions, persistent state, and reusable OpenProse programs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote or imported `.prose` programs can direct the agent to run workflows the user did not author. <br>
Mitigation: Review local, URL, registry, and imported `.prose` programs before execution, and avoid untrusted remote programs. <br>
Risk: Workflow execution can spawn subagents and persist outputs or memory across runs. <br>
Mitigation: Install only when an agentic workflow runner is intended, keep secrets out of prompts and persistent memory, and periodically inspect or clean `.prose/` and `~/.prose/` state. <br>
Risk: PostgreSQL state can expose database credentials through workflow context or logs. <br>
Mitigation: Use a dedicated limited-privilege database for PostgreSQL state and avoid sharing production credentials with workflows. <br>


## Reference(s): <br>
- [OpenProse homepage](https://www.prose.md) <br>
- [ClawHub skill page](https://clawhub.ai/mondilo1/skills/prose) <br>
- [Publisher profile](https://clawhub.ai/user/mondilo1) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline code, shell command snippets, and generated workflow artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update `.prose` programs, runtime state under `.prose/`, and persistent agent memory when requested by a workflow.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
