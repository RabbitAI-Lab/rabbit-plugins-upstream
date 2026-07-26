## Description: <br>
Skill Factory helps agents create, evaluate, improve, benchmark, analyze, synthesize, package, and publish OpenClaw skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeremysommerfeld8910-cpu](https://clawhub.ai/user/jeremysommerfeld8910-cpu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and skill maintainers use this skill to scaffold new OpenClaw skills, run quality evaluations, iterate on skill versions, compare benchmark results, analyze patterns, and prepare skills for publication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create and modify persistent skill files and package archives. <br>
Mitigation: Use it in a dedicated draft workspace and review generated diffs before enabling or publishing a skill. <br>
Risk: Packaged or published skills may accidentally include secrets or unintended local files. <br>
Mitigation: Scan generated skill folders and archives for secrets and unnecessary files before packaging or publication. <br>
Risk: Sync or publish commands can share skills more broadly than intended. <br>
Mitigation: Run publish or sync steps only after confirming the target account, workspace, version, and changelog. <br>


## Reference(s): <br>
- [ClawHub Skill Factory release page](https://clawhub.ai/jeremysommerfeld8910-cpu/skill-factory) <br>
- [OpenClaw Skill Patterns](artifact/references/patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, generated skill files, evaluation reports, and packaged skill artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or modify persistent skill directories, metadata, evaluation history, and packaged archives when the agent follows the workflow.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
