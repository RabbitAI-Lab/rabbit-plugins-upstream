## Description: <br>
Automatically generates complete project structures with README, requirements, tests, and asset manifests, then runs validation before delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xincen0725](https://clawhub.ai/user/xincen0725) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use Code Factory to turn natural-language project requests into a standardized Python project with source files, tests, documentation, run scripts, and manifests. It is intended for local project generation workflows where generated assets are reviewed and verified before handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can write and mutate project files, install packages, and execute generated tests on the local host. <br>
Mitigation: Run it in a disposable workspace or container, review generated files before execution, and avoid running it in directories that contain sensitive material. <br>
Risk: Generated tests and dependency installation may execute code or packages that were produced from a user prompt. <br>
Mitigation: Inspect generated requirements, scripts, and tests before running them, and use an isolated Python environment with minimal privileges. <br>
Risk: Failure learning data may retain prompts, paths, test output, or other local execution details. <br>
Mitigation: Review and clean up .learnings data after use, especially when prompts or output may contain sensitive information. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Generated project files plus Markdown summaries, JSON manifests, TOML configuration, and shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a project path, README preview, ASSET_MANIFEST summary, manifest.json summary, and test result summary.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; pyproject.toml reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
