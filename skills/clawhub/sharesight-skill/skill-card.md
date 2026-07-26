## Description: <br>
Manage Sharesight portfolios, holdings, and custom investments via the API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lextoumbourou](https://clawhub.ai/user/lextoumbourou) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, OpenClaw users, and finance operators use this skill to inspect Sharesight portfolios, analyze performance, manage holdings, and maintain custom investments through structured CLI/API workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify Sharesight records when write mode is enabled. <br>
Mitigation: Leave SHARESIGHT_ALLOW_WRITES unset for read-only use and enable it only for reviewed create, update, or delete operations. <br>
Risk: The skill uses Sharesight API credentials and caches access tokens locally. <br>
Mitigation: Install only when account access is intended, protect the configured credentials, and clear the cached token when the integration is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lextoumbourou/skills/sharesight-skill) <br>
- [Sharesight API getting started](https://portfolio.sharesight.com/api/) <br>
- [OpenClaw environment configuration](https://docs.openclaw.ai/environment) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [JSON command output with command-line guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Sharesight client credentials; create, update, and delete operations require SHARESIGHT_ALLOW_WRITES=true.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, pyproject.toml, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
