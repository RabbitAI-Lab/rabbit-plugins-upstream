## Description: <br>
Provides templates and lifecycle patterns for storage and documentation systems. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation maintainers use this skill to organize markdown-backed knowledge stores with reusable templates, maturity stages, naming conventions, retention patterns, and backend selection guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger words may cause the skill to appear in unrelated template, storage, lifecycle, or organization discussions. <br>
Mitigation: Use it when the task is specifically about markdown-backed knowledge stores, documentation templates, or lifecycle management. <br>
Risk: Shell and Python snippets are examples that may inspect, move, or update files when adapted. <br>
Mitigation: Review paths, scopes, and retention behavior before running adapted commands or scripts. <br>
Risk: Some artifact text includes stale generic verification language. <br>
Mitigation: Treat verification notes as documentation artifacts and confirm actual commands or integrations in the target environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-storage-templates) <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [Lifecycle stages module](artifact/modules/lifecycle-stages.md) <br>
- [Storage patterns module](artifact/modules/storage-patterns.md) <br>
- [Template patterns module](artifact/modules/template-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with YAML frontmatter templates, shell examples, and Python snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only output; examples should be reviewed and adapted before use.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
