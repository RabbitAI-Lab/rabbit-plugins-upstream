## Description: <br>
Analyzes self-hosted SonarQube projects, fetches issues, checks Quality Gates, and returns code-quality reports with suggested fixes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[felipeoff](https://clawhub.ai/user/felipeoff) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and CI/CD maintainers use this skill to query self-hosted SonarQube projects or pull requests, summarize issues and Quality Gate status, and produce suggested remediation steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Weak credential examples may lead users to reuse default or committed SonarQube tokens. <br>
Mitigation: Use a real least-privilege SonarQube token from environment variables or secret storage, and do not commit tokens. <br>
Risk: Auto-fix wording may cause users to over-trust suggested code changes or future versions that add source-file writes. <br>
Mitigation: Review suggested fixes before applying them, and carefully review any future release that adds real auto-fix behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/felipeoff/skills/sonarqube-analyzer) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact skill documentation](artifact/SKILL.md) <br>
- [Artifact changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance, Shell commands] <br>
**Output Format:** [JSON and Markdown reports with CLI text summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a SonarQube host URL, authentication token, project key, and optional pull request, severity, limit, action, and format parameters.] <br>

## Skill Version(s): <br>
0.1.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
