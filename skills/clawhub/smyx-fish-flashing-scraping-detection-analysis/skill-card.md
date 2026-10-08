## Description:

Analyzes aquarium camera footage for fish flashing and scraping, counts abnormal contacts, and provides ectoparasite risk warnings and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers, aquaculture operators, and developers use the skill to review fish behavior footage for frequent rubbing against tank surfaces and receive early warnings, suggested checks, and historical reports. Warnings are not a parasite diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium media or URLs are sent to a cloud-backed analysis service.

Mitigation: Use only media you are comfortable uploading, and obtain appropriate authorization before submitting shared aquarium footage.

Risk: The skill silently creates or reuses a cloud-linked identity and stores authentication tokens locally.

Mitigation: Review this behavior before installation, run in a separate workspace, and remove local data files when you stop using the skill.

Risk: Visual behavior warnings can be unreliable or mistaken for a confirmed parasite diagnosis.

Mitigation: Check camera visibility and lighting, treat warnings as prompts for further inspection, and seek a qualified aquatic veterinarian for diagnosis.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-fish-flashing-scraping-detection-analysis)
- [Fish flashing and scraping API reference](references/api_doc.md)
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Reports]

**Output Format:** [Markdown summaries and structured JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Warnings may include event frequency, duration, affected fish, recommended actions, and report links; historical reports can be listed.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
