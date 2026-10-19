## Description:

Searches clinical-trial registries across regions and summarizes trial phase, status, sponsors, timelines, and competitors for planning and landscape analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Researchers, trial planners, and developers use this skill to compare public clinical-trial registrations, identify similar studies, benchmark study designs, and review competitor landscapes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public search terms and a stable machine-derived fingerprint are sent to the publisher's third-party endpoints.

Mitigation: Use only public queries; do not enter patient data, confidential study plans, proprietary strategy, or private tokens.

Risk: A recoverable shared bearer token is bundled with the skill.

Mitigation: Treat the token as public shared infrastructure, not a personal secret; review endpoint access before use.

Risk: CDE and anti-bot documentation may not match the retrieval behavior.

Mitigation: Review the documented source-access approach before relying on compliance claims or retrieved results.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/medstatstar/skills/ct-registry)
- [Project homepage (publisher metadata)](https://github.com/medstatstar/ct-registry)
- [Search procedure](references/search_procedure.md)
- [Normalized record schema](docs/registry_record_schema.md)

## Skill Output:

**Output Type(s):** [Text guidance, Markdown, JSON, Excel workbook, PNG chart]

**Output Format:** [Conversational text or Markdown; optional JSON, XLSX, and PNG files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [XLSX is the default final report; intermediate JSON and Markdown can be retained on request. Document downloads require explicit confirmation.]

## Skill Version(s):

0.14.3 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
