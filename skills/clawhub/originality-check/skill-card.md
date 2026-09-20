## Description:

originality-check is a zero-dependency CLI that compares a contest submission fingerprint against known hashes and returns advisory JSON originality signals under UIBC contest rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Contest organizers and reviewers use this skill to triage originality checks by comparing a submitted work fingerprint with known historical or public fingerprints. Its output is decision support and requires human review before any final contest ruling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The checker uses a simple illustrative hash-similarity algorithm and may not be sufficient for final originality decisions.

Mitigation: Treat results as advisory triage only and require contest organizers or reviewers to complete the final originality determination.

Risk: Users who do not read Chinese-language documentation may miss the tool's limitations and review requirements.

Mitigation: Confirm the documentation fits the deployment audience and provide reviewer-facing guidance before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/originality-check)
- [LGD theory reference](https://medxpert.cn/theory)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [JSON IR from the CLI, with Markdown usage guidance in the skill documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes rc status codes, duplicate-match indicators, warnings, notes, and an AIGC metadata marker.]

## Skill Version(s):

1.0.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
