## Description:

Analyzes aquarium camera images or videos for fish gasping, rapid mouth movement, and increased gill-cover movement to produce an ammonia poisoning or hypoxia risk warning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium owners, aquaculture operators, public aquarium staff, and developers use this skill to analyze fixed-camera aquarium footage for visual warning signs of fish gasping, abnormal respiration, and possible water-quality emergencies. The output supports timely water testing, aeration, water-change decisions, and escalation to qualified aquatic health professionals without presenting a definitive disease diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium videos or URLs are sent to the publisher's remote service and resulting cloud reports may be associated with a generated or reused local identity.

Mitigation: Use only authorized aquarium media, avoid sensitive environments unless approved, and confirm the publisher's data handling terms before installation or use.

Risk: The package can create local workspace data and store service tokens in SQLite.

Mitigation: Run it in an isolated workspace, review local data storage before and after use, and remove or rotate stored credentials when the skill is no longer needed.

Risk: The release is configured to call development or private HTTP endpoints.

Mitigation: Review and replace endpoint configuration with approved production endpoints before using the skill in a normal deployment.

Risk: The security verdict is suspicious and requires review before installation.

Mitigation: Perform governance, security, and configuration review before deploying the skill or allowing it to process user media.

## Reference(s):

- [Skill page](https://clawhub.ai/18072937735/skills/smyx-fish-gasping-ammonia-warning-analysis)
- [Aquarium warning API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown text with structured JSON analysis content, warning guidance, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May optionally save the rendered analysis output to a user-specified file.]

## Skill Version(s):

1.0.12 (source: server release evidence; artifact frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
