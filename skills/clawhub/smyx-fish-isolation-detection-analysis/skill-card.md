## Description:

Analyzes aquarium or aquaculture video to identify fish schooling state, persistent isolation behavior, alert level, and recommended non-medication follow-up actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External aquarium keepers, aquaculture operators, and developers use this skill to analyze fixed-camera fish videos or video URLs for schooling, isolation, and historical report review. It supports monitoring workflows for home aquariums, public aquariums, aquaculture ponds, and quarantine tanks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium videos, video URLs, and report history are sent to or queried from the LifeEmergence cloud service.

Mitigation: Use the skill only with videos and report data that are approved for cloud processing, and review the service endpoint and data retention expectations before deployment.

Risk: The skill can create or reuse a local identity and store service tokens in the workspace data directory.

Mitigation: Review and protect the workspace data directory, rotate or remove stored tokens when access should end, and avoid shared workspaces for sensitive deployments.

Risk: Fish isolation alerts may be unreliable when tracking quality is poor, the view is obstructed, or the species naturally lives alone.

Mitigation: Require clear fixed-camera footage, validate species-specific baselines, and treat unreliable tracking states as a request to reshoot or adjust the camera rather than as a definitive alert.

Risk: Behavior analysis could be mistaken for veterinary diagnosis or treatment advice.

Mitigation: Use the output as monitoring guidance only; confirm health decisions with a qualified aquarium veterinarian or aquaculture professional and avoid medication or device-control actions without user confirmation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-isolation-detection-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, API calls, files, guidance]

**Output Format:** [Markdown text with structured JSON analysis content and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report export links, historical report lists, alert levels, recommended actions, and disclaimers.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
