## Description: <br>
GitGuard audits local Git repositories for exposed secrets, composite health, commit quality, stale branches, dependency freshness, and optional GitHub PR or issue triage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[welove111](https://clawhub.ai/user/welove111) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to audit repositories they own for exposed credentials, repo health, commit hygiene, stale branches, dependency freshness, and stale GitHub PRs or issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads source files and git metadata for repository paths provided by the user. <br>
Mitigation: Use it only on repositories you intend to audit and review the target path before running scans. <br>
Risk: Optional dependency freshness and GitHub triage features perform read-only network requests and may use a GitHub token for higher rate limits. <br>
Mitigation: Run offline-capable checks when network access is not needed, and provide a GitHub token only when higher-rate triage is required. <br>
Risk: The security scan identifies ordinary dependency hygiene as the main caution. <br>
Mitigation: Pin or constrain the requests dependency according to the deployment environment's package management policy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/welove111/skills/gitguard) <br>
- [Project homepage](https://btc-vision.org) <br>
- [GitGuard repository link from artifact metadata](https://github.com/welove111/gitguard-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Guidance] <br>
**Output Format:** [JSON-compatible structured results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Secret findings use redacted previews; dependency and GitHub triage checks may use read-only network requests.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
