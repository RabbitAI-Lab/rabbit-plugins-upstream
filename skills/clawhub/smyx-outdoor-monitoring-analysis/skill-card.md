## Description:

Analyzes outdoor images and videos to identify people, vehicles, non-motorized vehicles, and pets, and produces monitoring reports for areas such as courtyards, orchards, and farms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Outdoor property owners and operators use this skill to analyze surveillance images or videos for people, vehicles, and pets, assess possible intrusions, and review cloud-stored monitoring reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surveillance media and submitted URLs are sent to the LifeEmergence cloud without clear user-facing consent controls.

Mitigation: Obtain authorization before submitting media or URLs, and prefer non-sensitive inputs.

Risk: The skill silently creates or reuses a local identity, stores tokens locally, and can query cloud report history.

Mitigation: Review access to the workspace data directory and its identity and token state; add explicit consent and cleanup controls before sensitive use.

## Reference(s):

- [Outdoor monitoring API reference](references/api_doc.md)
- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-outdoor-monitoring-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Monitoring report or JSON; history listings as Markdown tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes detection results, risk observations, recommendations, and report links; can save results to a file.]

## Skill Version(s):

1.0.16 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
