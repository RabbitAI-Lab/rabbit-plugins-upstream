## Description:

Assesses frog skin moisture from high-definition dorsal or lateral images or videos by analyzing glossiness, wrinkles, white film, and context signals to produce dehydration-risk reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External keepers, amphibian farms, animal hospitals, and developers use this skill to evaluate frog skin moisture from images, videos, or URLs and receive structured risk findings, suggested husbandry actions, and report links. It also supports cloud-backed history queries for previous moisture assessment reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Frog images, videos, or URLs are sent to the configured Life Emergence cloud service for analysis.

Mitigation: Install only when cloud processing is acceptable, and avoid submitting private or internal URLs.

Risk: The skill silently creates or reuses a local account identity and stores account tokens locally.

Mitigation: Review or clear the workspace data directory and local SQLite token store when account separation is required.

Risk: Moisture assessments may influence urgent animal care decisions.

Mitigation: Treat outputs as visual assessment guidance, keep the skill's veterinary and medication limits in place, and contact a qualified amphibian veterinarian for severe dehydration concerns.

## Reference(s):

- [API Interface Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-frog-skin-moisture-assessment-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown or JSON analysis report with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write results to a user-specified output file; history queries return a Markdown table.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
