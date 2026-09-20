## Description:

Shisan Xinuo Workflow is a workflow-governance skill that guides engineering agents through auditable task routing, restatement, capability checks, gates, verification evidence, and persistent task records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zxc663](https://clawhub.ai/user/zxc663)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to make coding, debugging, review, and multi-file engineering tasks follow a consistent workflow with explicit gates, evidence, verification, and handoff records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent workflow, memory, and rule files can influence future agent sessions.

Mitigation: Install only when persistent project workflow governance is intended, prefer default or on-demand use, and review every proposed file addition or merge.

Risk: Hard or global injection and hooks can affect user-level agent configuration, memory, or startup behavior.

Mitigation: Avoid hard or global injection and hooks unless those changes are intentionally authorized and reviewed for the target platform.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zxc663/skills/shisan-xinuo-workflow)
- [Project Homepage](https://github.com/zxc663/shisan-xinuo-workflow)
- [Workflow Details](references/details.md)
- [Injection Core](references/injection-core.md)
- [Platform Adaptation](references/platform-adaptation.md)
- [Security and Rollback](references/security.md)
- [Skill Usage](references/skill-usage.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional code, shell commands, configuration snippets, and file templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to create or update workflow, memory, rules, and optional hook configuration files.]

## Skill Version(s):

1.0.19 (source: server release metadata; artifact metadata reports workflow content version 3.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
