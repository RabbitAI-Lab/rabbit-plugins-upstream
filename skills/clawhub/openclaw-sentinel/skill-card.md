## Description: <br>
Openclaw Sentinel helps agents inspect and scan installed or downloaded agent skills for supply chain security risks such as obfuscated code, suspicious install behavior, dependency confusion, metadata inconsistencies, and known-bad signatures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atlaspa](https://clawhub.ai/user/atlaspa) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and security reviewers use this skill to inspect agent skills before installation, scan installed skills after installation, review threat database status, and understand local skill supply chain risk. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can manage other installed skills, including commands that may disable, move, or remove skill directories. <br>
Mitigation: Start with scan, inspect, threats, and status; pass an explicit --workspace path; keep backups; and use quarantine, reject, or protect only when you intentionally want those changes. <br>
Risk: Imported threat lists can affect scan results and decisions. <br>
Mitigation: Import threat lists only from trusted sources and review their contents before use. <br>
Risk: The release evidence reports a suspicious security verdict because some management capabilities are under-disclosed. <br>
Mitigation: Treat results as advisory until reviewed, and verify that the documented commands match the actions you intend to allow in the workspace. <br>


## Reference(s): <br>
- [Openclaw Sentinel on ClawHub](https://clawhub.ai/atlaspa/skills/openclaw-sentinel) <br>
- [AtlasPA publisher profile](https://clawhub.ai/user/atlaspa) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and local scan results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local security findings, risk scores, recommendations, threat database summaries, status output, and optional JSON evidence files.] <br>

## Skill Version(s): <br>
1.0.2 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
