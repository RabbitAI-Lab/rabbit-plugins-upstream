## Description:

Guides agents through source verification, originality review, editorial planning, human approval gates, drafting, review, and evidence packaging for a single technology industry deep-dive article.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, writers, and editors can use this skill to turn a topic brief and source materials into a reviewed, publish-ready Markdown deep-dive for technology, AI, data, cloud, or enterprise-software audiences, with supporting evidence and review records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Originality searches may expose confidential source material to external search providers.

Mitigation: Review the confidentiality of the input and avoid sending sensitive source text in search queries.

Risk: The security scan was partial because some referenced paths could not be matched, so it does not establish that all relevant behavior was inspected.

Mitigation: Inspect the complete release contents, including referenced paths, before relying on the scan assessment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/industry-deep-dive-pipeline-skill)
- [Planning schema](references/planning-schema.md)
- [Evidence and originality](references/evidence-and-originality.md)
- [Replay evaluation](references/replay-evaluation.md)
- [Writing profile interface](references/writing-profile-interface.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance]

**Output Format:** [A reviewed Markdown article and evidence/review records, with JSON machine-gate results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one article per run; requires a topic brief or source materials and stops at the approved draft and evidence package.]

## Skill Version(s):

1.1.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
