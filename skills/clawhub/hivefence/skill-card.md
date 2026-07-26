## Description: <br>
Collective immunity network for AI agents that detects prompt injection attacks, reports hashed threat patterns, and shares community-validated updates across connected agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seojoonkim](https://clawhub.ai/user/seojoonkim) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent builders use HiveFence to add prompt-injection detection, risk scoring, and community threat-intelligence updates to AI agents. The skill is intended for agents that can use network-backed threat sharing while preserving prompt privacy through hashed pattern reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Detected prompt-injection patterns may be automatically reported as SHA-256 hashes to a third-party threat-intelligence service. <br>
Mitigation: Use only when third-party hash reporting is acceptable, and ask the publisher for transmitted fields, retention policy, and reporting-disable controls before use in private, regulated, or strict local-only environments. <br>
Risk: Network-backed pattern updates and community voting can influence blocking behavior for connected agents. <br>
Mitigation: Review proposed integration behavior, monitor false positives, and keep a local allow/deny policy or fallback path for high-sensitivity workflows. <br>


## Reference(s): <br>
- [HiveFence ClawHub page](https://clawhub.ai/seojoonkim/skills/hivefence) <br>
- [HiveFence website](https://hivefence.com) <br>
- [HiveFence API docs](https://hivefence.com/docs) <br>
- [HiveFence GitHub repository](https://github.com/seojoonkim/hivefence) <br>
- [HiveFence API base URL](https://hivefence-api.seojoon-kim.workers.dev) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, API Calls, Configuration instructions] <br>
**Output Format:** [Markdown with JavaScript and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May involve network requests to HiveFence API endpoints for threat reporting, voting, latest patterns, and statistics.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
