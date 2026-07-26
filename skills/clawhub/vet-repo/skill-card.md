## Description: <br>
Scan repository agent configuration files for known malicious patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itsnishi](https://clawhub.ai/user/itsnishi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security reviewers use this skill to scan unfamiliar or changed repositories for risky agent configuration patterns before trusting local agent behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional registry verification can send package names to public npm or PyPI registry endpoints if invoked separately. <br>
Mitigation: Use the documented local scan workflow for private repositories unless public registry lookups are acceptable. <br>
Risk: The advisory hook behavior described by the artifact warns about risky commands but does not block execution. <br>
Mitigation: Treat hook warnings as supplementary signals and rely on scanner findings plus human review for enforcement decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/itsnishi/skills/vet-repo) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, shell commands, guidance] <br>
**Output Format:** [Structured text report grouped by severity with actionable recommendations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports findings as CRITICAL, HIGH, MEDIUM, LOW, or INFO.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
