## Description: <br>
Safely validate, publish, and track a local SKILL.md directory across GitHub, Awesome Codex Plugins, HOL Registry, skills.sh, SkillsMP, LobeHub, ClawHub, and Cursor Directory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liuyewang](https://clawhub.ai/user/liuyewang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use this skill to preflight, publish, synchronize, and track one local agent skill across multiple public skill registries and marketplace-style directories. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-impact publishing actions can commit, push, publish, or create registry handoffs across selected platforms. <br>
Mitigation: Run preflight or dry-run first, review platform choices and git diffs, and reserve --yes for already-reviewed authenticated automation. <br>
Risk: The Awesome Codex Plugins workflow targets a hard-coded GitHub fork owner rather than clearly using the current user's account. <br>
Mitigation: Review the generated fork and pull request target before enabling that platform or running a non-dry-run sync. <br>
Risk: Broad implicit invocation and CLI output could affect automated decisions if used without review. <br>
Mitigation: Require explicit human review for publication decisions and sanitize CLI output before feeding it into downstream automation. <br>


## Reference(s): <br>
- [Platform Matrix](artifact/references/platform-matrix.md) <br>
- [Security Policy](artifact/references/security-policy.md) <br>
- [State Schema](artifact/references/state-schema.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/liuyewang/skills/skill-sync-publisher) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline CLI commands and optional JSON CLI reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce platform status, dry-run plans, manual handoff instructions, and local state updates.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
