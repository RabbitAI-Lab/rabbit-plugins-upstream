## Description:

Analyzes fish-egg images or videos to identify incubation stages and provide breeding-tank reports and suggested actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Fish breeders, hatchery staff, and developers use macro images or videos to monitor egg development, review incubation-stage reports, and plan hatchling care. Historical reports can be queried through the cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fish-egg images, videos, or URLs are sent to the LifeEmergence cloud service for analysis.

Mitigation: Use only media you are authorized to share, after checking the provider's handling and retention terms.

Risk: The skill automatically creates or reuses a local identity and stores authentication material in the workspace data directory.

Mitigation: Review the skill before installation and protect the workspace data directory as sensitive.

## Reference(s):

- [Fish Egg Incubation Stage Identification on ClawHub](https://clawhub.ai/18072937735/skills/smyx-fish-egg-incubation-stage-analysis)
- [Fish-egg analysis API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured incubation-stage report or Markdown history table, with optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include egg-color distribution, eye-spot detection, estimated hatching window, suggested actions, and report links.]

## Skill Version(s):

1.0.8 (source: server-resolved ClawHub release; artifact frontmatter lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
