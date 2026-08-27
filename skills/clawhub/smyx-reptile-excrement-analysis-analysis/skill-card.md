## Description:

Analyzes reptile enclosure images or video frames to identify urate size, color, and texture alongside feces color and morphology, then returns structured health-oriented observations and suggested next actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile keepers, farm operators, and app or enclosure developers use this skill to submit reptile waste images or URLs, receive structured urate and feces observations, and review historical reports when available. The output is a visual assessment aid, not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence reports that uploaded reptile images, videos, URLs, report metadata, and an automatically selected identity may be sent to LifeEmergence cloud endpoints.

Mitigation: Review before installing, use only if cloud processing is acceptable, and prefer an isolated workspace with a disposable account or identity for testing.

Risk: Security evidence reports that tokens and profile data may be retained in a shared local SQLite database.

Mitigation: Use a dedicated workspace, avoid sharing the workspace between unrelated tasks or users, and clear local data when the skill is no longer needed.

Risk: Visual waste analysis can be mistaken for veterinary diagnosis or treatment advice.

Mitigation: Treat outputs as non-diagnostic screening guidance, avoid medication or procedure recommendations, and direct significant or repeated abnormalities to a qualified reptile veterinarian.

Risk: Poor image quality, missing scale references, substrate obstruction, or missing species and feeding context can make visual assessment unreliable.

Mitigation: Require clear top-down pre-cleaning images or frames, adequate lighting, a size reference where possible, and species, feeding, shedding, brumation, and recent diet-change context before relying on results.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Analysis API error and request format reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown text containing structured JSON-like analysis results and optional report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the returned analysis text to a requested output file; historical report queries return structured report lists.]

## Skill Version(s):

1.0.9 (source: server release evidence; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
