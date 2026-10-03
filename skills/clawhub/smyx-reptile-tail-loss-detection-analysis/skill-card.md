## Description:

Analyzes gecko and lizard tail images or videos for signs of tail loss, wounds, and regeneration, and returns event alerts and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile keepers and enclosure operators use the skill to review tail imagery for possible autotomy, track changes against prior observations, and view event alerts or historical reports. Visual findings are not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reptile media, URLs, and report-history requests are sent to a cloud service, and the skill may silently create or reuse a cloud-linked identity.

Mitigation: Obtain explicit consent before sending sensitive media, looking up history, or creating an account; review the cloud service before installation.

Risk: Service tokens may be stored in a local database under the workspace data directory.

Mitigation: Protect access to the workspace data directory and review local token storage before installation.

Risk: Poor-quality imagery or an existing regenerated tail can produce misleading alerts.

Mitigation: Check image quality and prior tail history, and have a reptile veterinarian assess concerning wounds or suspected infection.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-reptile-tail-loss-detection-analysis)
- [Tail-loss analysis API reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown history table; optional JSON file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include event alerts, suggested actions, and report links.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
