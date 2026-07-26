## Description: <br>
Skill Kit helps Claude Code agents create, lint, merge, upgrade, route, convert, discover, graph, and publish-check multi-topic skills, including trigger and hook registration guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent builders use Skill Kit to create, validate, refactor, discover, and publish-check Claude Code skills. It is also used to generate dependency graphs and manage trigger and hook workflows for skill ecosystems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent Claude Code hook or settings changes may be applied. <br>
Mitigation: Use dry-run and per-project modes first, and review settings.json plus generated hook scripts before applying changes. <br>
Risk: Global or unattended skill installs can affect more projects than intended. <br>
Mitigation: Avoid global -g -y installs for untrusted skills and prefer per-project installation when evaluating behavior. <br>
Risk: Converted, merged, or deduplicated skills may not behave as expected after file moves. <br>
Mitigation: Keep backups until the converted or merged skill has been reviewed, validated, and exercised in the target environment. <br>


## Reference(s): <br>
- [Skill Kit on ClawHub](https://clawhub.ai/drumrobot/skills/skill-kit) <br>
- [Publisher profile](https://clawhub.ai/user/drumrobot) <br>
- [README](README.md) <br>
- [Skill definition](SKILL.md) <br>
- [Skills CLI ecosystem](https://skills.sh/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with code fences, command examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose skill files, hook scripts, settings changes, dependency graphs, and validation reports.] <br>

## Skill Version(s): <br>
0.5.0 (source: ClawHub release metadata and CHANGELOG, released 2026-07-23) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
