## Description:

This skill guides agents through source verification, originality review, planning, gated drafting, review, revision, and evidence packaging for publish-ready technology industry deep-dive Markdown articles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and editorial teams use this skill to turn a technology, AI, data, cloud, or enterprise-software topic brief into an evidence-backed Markdown deep-dive article and review package.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research-heavy writing can inspect supplied local materials and create local draft and review files.

Mitigation: Use a dedicated case directory, provide only the writing profile fields needed for the article, and review the generated bundle before any downstream publishing workflow reads it.

Risk: Drafts can contain unverified high-risk facts, unregistered numbers, or wording that overstates originality.

Mitigation: Keep high-risk claims in the fact table, require first-hand or dual-source verification where appropriate, and rerun the deterministic draft and final validation gates after revisions.

Risk: Private writing profiles or local paths may leak into public-facing outputs if reviewed carelessly.

Mitigation: Load private profile fields only on demand, scan for credentials, UUIDs, personal paths, and publication metadata, and remove any hits before final handoff.

## Reference(s):

- [Planning Schema](references/planning-schema.md)
- [Evidence and Originality](references/evidence-and-originality.md)
- [Writing Profile Interface](references/writing-profile-interface.md)
- [Replay Evaluation](references/replay-evaluation.md)
- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/industry-deep-dive-pipeline-skill)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Case-directory bundle of Markdown files plus a JSON machine-gate report and inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stops at the approved article and evidence package; it does not generate publication layouts, social copy, CMS drafts, or publish actions.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
