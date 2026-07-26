## Description: <br>
GitGuard helps agents audit local Git repositories for exposed secrets, repository health, commit quality, stale branches, dependency freshness, and GitHub backlog staleness. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[welove111](https://clawhub.ai/user/welove111) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to inspect repositories they own or are authorized to review, prioritizing secret cleanup, repo health work, stale branch cleanup, dependency updates, and PR or issue triage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads the repository paths supplied by the user, which may include private source files and local git metadata. <br>
Mitigation: Run it only against repositories you own or are authorized to audit, and avoid broad private directories unless you intend them to be scanned. <br>
Risk: Dependency freshness and GitHub triage checks can contact npm, PyPI, and GitHub and expose package or repository metadata to those services. <br>
Mitigation: Use offline-capable checks when privacy is required, and enable network-backed checks only when those external lookups are acceptable. <br>
Risk: GitHub triage can use a token from the environment, increasing the impact of accidental token exposure or overbroad permissions. <br>
Mitigation: Use a limited-scope GitHub token and avoid providing write-capable credentials for read-only triage. <br>
Risk: Audit reports may include file paths, line numbers, and redacted secret previews that are still sensitive in some organizations. <br>
Mitigation: Review generated reports before sharing them outside the team or system that owns the scanned repository. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/welove111/skills/gitguard-skill) <br>
- [Publisher profile](https://clawhub.ai/user/welove111) <br>
- [Publisher homepage](https://btc-vision.org) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Text, Guidance] <br>
**Output Format:** [Structured JSON reports with redacted findings, scores, rankings, and recommendations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Secret findings are intended to be redacted previews rather than raw credential values.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
