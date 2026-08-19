## Description:

Analyzes aquarium camera images or video to estimate fish gill-cover opening and closing cycles, calculate respiratory rate, flag abnormal breathing patterns, and produce structured monitoring reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium owners, aquaculture operators, public aquarium staff, laboratory teams, and developers use this skill to analyze close-range fish video or image inputs, monitor respiratory rate trends, and receive non-diagnostic alerts and suggested next steps when visual breathing signals appear abnormal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium media and report history are processed through the publisher's cloud service.

Mitigation: Install only when this data flow is acceptable for the deployment, and obtain any required authorization for monitored aquariums.

Risk: The package can create or reuse a local identity and persist tokens in a workspace SQLite database.

Mitigation: Review local identity and token storage before installation, and restrict workspace access to users who should be able to view those credentials.

Risk: The inspected package defaults to private HTTP development endpoints rather than the documented public service.

Mitigation: Verify and update configuration endpoints before use, and avoid sending production media to untrusted or unintended services.

Risk: Visual respiratory monitoring may produce misleading alerts when footage is unclear, species context is missing, or water-temperature context is unavailable.

Mitigation: Use clear close-range footage, provide species and water-temperature context where possible, and treat outputs as non-diagnostic monitoring guidance rather than veterinary advice.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-respiratory-rate-monitor-analysis)
- [API Interface Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured text, with optional JSON-like report fields and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include respiratory rate, signal stability, alert level, suggested actions, report links, and history tables.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
