## Description: <br>
Prioritize issues from a named GitHub repository or supplied issue set by ROI, solution sanity, architectural impact, and actionability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[glucksberg](https://clawhub.ai/user/glucksberg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use this skill to analyze open GitHub issues, exclude issues with existing PRs, rank remaining work by adjusted ROI, and identify quick wins or contributor-appropriate recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Fetched GitHub issue and PR content can be saved in local run-history files. <br>
Mitigation: Use the skill only for repositories whose issue content may be stored locally, and set a dedicated history directory when handling sensitive repositories. <br>
Risk: Resume, diff, retention, and cleanup behavior operates on local history paths. <br>
Mitigation: Review the configured history directory before use, avoid pointing resume or diff options at unrelated folders, and confirm retention cleanup is scoped to the skill's run-history area. <br>
Risk: Partial or fallback linked-PR detection can leave already-covered issues in the ranked recommendations. <br>
Mitigation: When the manifest reports partial, regex-only, skipped, or disabled linking, live-check final recommendations before acting on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/glucksberg/skills/issue-prioritizer) <br>
- [GitHub CLI](https://cli.github.com/) <br>
- [jq](https://jqlang.github.io/jq/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown issue-prioritization report with optional JSON or markdown table output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local run-history files containing fetched issue and PR content; default issue bodies are truncated for batch analysis.] <br>

## Skill Version(s): <br>
1.2.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
