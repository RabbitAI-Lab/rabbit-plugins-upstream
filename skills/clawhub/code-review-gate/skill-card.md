## Description: <br>
Code Review Gate analyzes git diffs across functional correctness, security, performance, readability, maintainability, testing, and documentation, then emits a severity-ranked report and blocks Critical findings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terr123123](https://clawhub.ai/user/terr123123) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and CI/CD agents use this skill as a pre-merge quality gate to review changed code, identify Critical, Important, and Minor issues, and decide whether a change should proceed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Static analysis can produce false positives or miss issues that require project context. <br>
Mitigation: Use the report as a pre-merge signal alongside human review, tests, and dedicated security tooling for high-risk changes. <br>
Risk: The skill shells out to git diff and can read an optional design document from the local filesystem. <br>
Mitigation: Run it in a trusted repository workspace and scope review inputs to the intended diff range and design file. <br>
Risk: Scanner guidance notes that fixture-like risky code or credential-looking strings should be confirmed before installation. <br>
Mitigation: Confirm flagged files are test fixtures rather than runtime paths, and verify any credential-looking values are dummy data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/terr123123/skills/code-review-gate) <br>
- [Project homepage](https://github.com/Terr123123/code-review-gate) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown, JSON, or terminal text report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return exit code 1 when Critical findings block the gate; may return exit code 3 when review is skipped.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
