## Description: <br>
Helps agents publish and version one skill across the ClawHub skill registry, ClawHub bundle-plugin packages, and Claude Code plugin marketplaces from a single source of truth. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[readysoon](https://clawhub.ai/user/readysoon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill maintainers use this guidance to prepare, sync, verify, and publish a skill release across ClawHub and Claude Code channels while keeping release metadata aligned. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publishing commands can expose unintended files or stale release metadata if followed without review. <br>
Mitigation: Review git status, diffs, selected upload folders, slugs, versions, and manifests before pushing or publishing. <br>
Risk: Version drift across the skill registry, bundle-plugin package, and Claude Code marketplace can cause failed or misleading releases. <br>
Mitigation: Use the skill's sync and version preflight guidance, then verify the live skill and package versions after publishing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/readysoon/skills/multi-channel-skill-publisher) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and manifest snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Human-reviewed publishing checklist; it does not execute commands automatically.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
