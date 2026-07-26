## Description: <br>
Thoroughly audit Tasks.md + Flatnotes for drift and accuracy; use GitHub (gh CLI) as source of truth to detect stale notes/cards and missing links. Produces a report and an optional fix plan. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[branexp](https://clawhub.ai/user/branexp) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and project maintainers use this skill to audit local Tasks.md boards and Flatnotes project notes against GitHub pull request state, then produce a drift report and optional fix plan. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The auditor reads local Tasks.md and Flatnotes directories and writes temporary reports that may contain task titles, project names, local paths, and pull request details. <br>
Mitigation: Confirm TASKS_ROOT and FLATNOTES_ROOT point only to intended audit directories and treat generated tmp reports as private. <br>
Risk: GitHub reconciliation depends on the GitHub account authenticated in the gh CLI. <br>
Mitigation: Check the active gh authentication context before running the audit so pull request results are scoped to the expected account and repositories. <br>
Risk: Some GitHub checks are skipped when gh is unavailable or unauthenticated, which can leave drift undetected. <br>
Mitigation: Review the report for SKIPPED_GITHUB or gh error entries and rerun after authenticating gh when GitHub truth reconciliation is required. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated Markdown or JSON audit reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Report generation depends on local Tasks.md and Flatnotes directories, optional TASKS_ROOT and FLATNOTES_ROOT environment overrides, and GitHub CLI authentication for PR reconciliation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
