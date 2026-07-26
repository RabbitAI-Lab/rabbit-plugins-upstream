## Description: <br>
GoSquared (gosquared.com) skill for searching and reading analytics data through the OOMOL oo CLI instead of direct API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect GoSquared project analytics, authorization metadata, realtime visitor activity, and Trends aggregates through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on OOMOL as an intermediary for the connected GoSquared account. <br>
Mitigation: Install only when the user trusts OOMOL for this connection and understands that analytics and authorization metadata may be read from the connected project. <br>
Risk: A future version could add write or destructive GoSquared actions. <br>
Mitigation: Review future releases before deployment and require explicit user confirmation before running any action marked write or destructive. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-gosquared) <br>
- [GoSquared Homepage](https://www.gosquared.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses OOMOL server-side credentials and returns connector data with execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
