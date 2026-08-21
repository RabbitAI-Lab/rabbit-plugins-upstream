## Description:

Identifies weed species and coverage density from field top-view images, and outputs a weed distribution heatmap dataset to support precision weeding decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External farm-management users and agent operators use this skill to analyze field images or videos for weed species, coverage density, distribution areas, heatmap data, and historical weed-analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload farm images or videos to configured backend services that are under-disclosed in the release evidence.

Mitigation: Use the skill only with media approved for that backend, and confirm the publisher's production HTTPS endpoint and retention policy before installation.

Risk: The skill can use or create an internal account identity, query cloud history, and store authentication tokens in a local SQLite database.

Mitigation: Run the skill in an isolated workspace, restrict access to the local data directory, and verify identity scoping before enabling historical report queries.

Risk: The server security guidance reports stale pet/video and image-format mismatches that may confuse users about valid inputs.

Mitigation: Validate accepted file formats and parameter defaults in a staging environment before relying on results for field operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-farmland-weed-identification-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown report or JSON analysis output, with optional saved result files and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include weed species lists, coverage-density ratings, distribution areas, heatmap data, analysis timestamps, and links to generated reports.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
