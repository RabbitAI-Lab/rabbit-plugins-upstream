## Description: <br>
Diff two agent or skill manifests and report capability, permission, dependency, status, and version changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agent reviewers, and platform teams use this skill to compare manifest versions, surface capability and permission deltas, catch version changes, and produce JSON output suitable for CI review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional CI verification helper intentionally runs local Python tests and self-test commands. <br>
Mitigation: Run the CI helper only in trusted repositories or controlled CI environments; use the offline manifest diff command for normal manifest comparisons. <br>


## Reference(s): <br>
- [Manifest Diff on ClawHub](https://clawhub.ai/itspremkumar/skills/manifest-diff) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text or JSON CLI output, with Markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Offline Python 3.8+ CLI; optional CI verification helper executes local tests and self-tests.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata; artifact frontmatter says 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
