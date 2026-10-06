## Description:

Analyzes reptile enclosure video to summarize movement and time spent in basking and hiding zones.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile keepers and enclosure operators use this skill to review basking and hiding patterns, receive environmental guidance, and consult past reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enclosure media or URLs are sent to a configured cloud service.

Mitigation: Review the destination and obtain approval before sharing enclosure footage or links.

Risk: The skill silently creates or reuses a local identity database containing account tokens and history context.

Mitigation: Avoid shared workspaces unless access to the local identity and cloud report history is controlled.

Risk: Behavioral warnings may be mistaken for a veterinary diagnosis.

Mitigation: Check species-specific baselines and recording conditions; consult a reptile veterinarian for persistent or severe symptoms.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-reptile-thermoregulation-behavior-analysis)
- [Skill API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis text or JSON; Markdown tables for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes zone-use metrics, alerts, recommendations, and report links when available.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; bundled frontmatter lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
