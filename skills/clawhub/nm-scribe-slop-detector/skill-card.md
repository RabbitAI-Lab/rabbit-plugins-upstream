## Description: <br>
Detects AI-generated writing patterns in prose. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, documentation maintainers, and release reviewers use this skill to scan prose, comments, READMEs, and public documentation for AI-writing markers, identity leaks, unsupported claims, hallucinated references, and cleanup candidates. It can also guide remediation and CI guardrails when reviewers want structured findings rather than a passive detector. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports a suspicious posture because the skill asks for broader repository cleanup, security review, and remediation authority than its short prose-detector summary suggests. <br>
Mitigation: Install it only when that broader repo-aware review is desired, run it on explicit target paths, and review its proposed changes before applying them. <br>
Risk: The workflow can inspect sensitive project surfaces such as secrets, agent configs, package registries, URLs, CI, and pre-commit hooks. <br>
Mitigation: Run it in a controlled workspace, avoid unnecessary secret exposure, and scope scans to files or directories that need review. <br>
Risk: Remediation output may include diffs or cleanup recommendations that could remove meaningful comments, change public API documentation, or overcorrect low-confidence findings. <br>
Mitigation: Keep auto-apply disabled unless a reviewer has approved the proposed diffs, and require human decisions for low-confidence findings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-slop-detector) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, structured finding records, JSON Lines for CI, and inline shell commands or configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings may include severity, confidence, evidence, rationale, suggested fixes, and diffs for high-confidence cases; default unattended behavior is report-only.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
