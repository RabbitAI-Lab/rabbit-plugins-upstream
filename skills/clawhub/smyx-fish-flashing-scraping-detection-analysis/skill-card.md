## Description:

Analyzes fixed aquarium camera video to detect fish flashing or scraping behavior, count abnormal friction events, and produce an ectoparasite risk warning report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and aquarium operators use this skill to analyze aquarium, quarantine tank, or aquaculture video for flashing and scraping patterns that may indicate ectoparasite risk. It returns risk-oriented observations and recommended next steps, not a veterinary diagnosis or medication plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium videos, video URLs, report history requests, and identity-linked metadata may be sent to the configured cloud service.

Mitigation: Use only non-sensitive, authorized footage and review the configured service endpoints, identity behavior, and retention expectations before deployment.

Risk: The skill may create or reuse local account and token state in the workspace data directory.

Mitigation: Avoid shared workspaces for sensitive use, and clear or isolate the workspace data directory when changing users or deployment contexts.

Risk: Behavioral warnings can be mistaken for veterinary diagnosis or treatment guidance.

Mitigation: Treat outputs as risk signals only; confirm ectoparasites through appropriate observation or veterinary microscopy and avoid medication, dose, or equipment changes unless confirmed by qualified personnel.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-flashing-scraping-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured JSON-like analysis text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud analysis status, event counts, alert level, recommended observation actions, and historical report listings.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
