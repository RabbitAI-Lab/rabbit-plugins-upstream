## Description:

Analyzes fixed-camera reptile enclosure video to report basking, hiding, cool-zone dwell time, zone transitions, activity rhythm, thermal preference labels, alerts, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile keepers, breeders, and smart vivarium app developers use this skill to analyze enclosure videos or URLs for thermal-zone use, behavior rhythm, and environment-related warning signals. The skill is intended to provide behavior statistics and care guidance, not veterinary diagnosis or medication instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reptile enclosure videos and account-linked report history are sent to the configured cloud service.

Mitigation: Install only when that data sharing is acceptable, review endpoint configuration before use, and avoid submitting sensitive footage unless permitted.

Risk: The skill creates local identity and token state with limited user control.

Mitigation: Use an isolated workspace for shared machines, review identity handling before deployment, and remove local state when the skill is no longer needed.

Risk: The security scan verdict is suspicious because of cloud-backed analysis, silent identity handling, media upload, report-history access, and local token storage.

Mitigation: Perform deployment review before use and restrict operation to users who understand the cloud, identity, and report-history behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-thermoregulation-behavior-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON or Markdown report text with behavior metrics, recommended actions, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include thermal preference labels, alert levels, historical report tables, and exported report URLs.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
