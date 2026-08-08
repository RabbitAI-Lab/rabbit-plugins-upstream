## Description:

This skill analyzes turtle or snake egg images or videos to report eggshell color, vascular signs, embryo silhouette, fertilization status, development stage, and incubation progress.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile breeders, incubator operators, and hobbyist keepers use this skill to analyze turtle or snake egg media, monitor development by egg ID, produce structured incubation reports, and review historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Egg images, videos, identity data, and report history may be processed by the publisher's cloud service.

Mitigation: Use the skill only with media and report data that may leave the local environment, and avoid private URLs or sensitive media.

Risk: The local workspace data directory may contain a SQLite database with reusable service tokens.

Mitigation: Treat the workspace data directory as sensitive, restrict access to it, and remove stored credentials when the skill is no longer needed.

Risk: Incubation-stage classifications can affect breeding decisions if they are treated as definitive.

Mitigation: Use the report as visual analysis guidance, confirm important decisions with species incubation references and environmental logs, and escalate serious findings to an appropriate reptile breeding professional.

## Reference(s):

- [API Reference](artifact/references/api_doc.md)
- [Shared Analysis API Reference](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [analysis, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON structured incubation report with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include report date, incubator ID, egg ID, species, estimated incubation days, visual signals, composite scene, alert level, recommended actions, disclaimer, and report links.]

## Skill Version(s):

1.0.9 (source: server release evidence; SKILL.md frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
