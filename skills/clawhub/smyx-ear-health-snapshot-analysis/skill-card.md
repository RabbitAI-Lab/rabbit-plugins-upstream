## Description:

Analyzes pet ear images or head-shaking and scratching videos to produce visual ear-canal observations, abnormality alerts, and check-up or veterinary follow-up suggestions without making a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, boarding centers, and veterinary intake teams use this skill to screen pet ear media for visible redness, discharge-like material, earwax buildup, and related health-risk prompts. It returns observations and follow-up suggestions for human review, not a diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images or videos may reveal private household details when submitted for analysis.

Mitigation: Use only media the user is comfortable sending to the configured cloud service, and avoid submitting unnecessary private surroundings.

Risk: The skill creates or reuses a local identity and may persist service tokens in the workspace data directory.

Mitigation: Run it in a workspace with appropriate access controls, and clear local data when identity or token persistence is not desired.

Risk: Visual ear-health observations may be mistaken for a medical diagnosis.

Mitigation: Present outputs as visual observations and follow-up suggestions, and direct abnormal findings to owner review or veterinary care.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-ear-health-snapshot-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown and JSON-like structured analysis text with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save results to a caller-provided output path and can list cloud report history.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
