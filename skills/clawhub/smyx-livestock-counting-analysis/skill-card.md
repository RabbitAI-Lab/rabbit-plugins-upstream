## Description:

Detects and counts livestock or poultry in barn or passage camera images and videos, returning total headcount, confidence, structured results, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators and external users can use this skill to count pigs, chickens, sheep, or other livestock from images, videos, or URLs for inventory checks, batch transfer counts, and passage counting. The skill returns structured count results and can list prior cloud reports associated with the current internal identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barn or livestock media and report metadata may be sent to the configured Life Emergence service.

Mitigation: Use only media that is appropriate to share with that service and avoid submitting sensitive farm, personnel, or location information unless that transfer is intended.

Risk: The skill can automatically create or reuse an internal identity, query cloud report history, and store account tokens or profile data locally.

Mitigation: Run it in an isolated workspace and avoid placing sensitive identity files or API keys where the skill can read them unless that behavior is intended.

Risk: Livestock counts can be wrong in dense, occluded, unstable, underexposed, or overexposed footage.

Mitigation: Use stable camera views that cover the counting area and review results against existing farm inventory or transfer-count procedures before operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-counting-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface document](artifact/references/api_doc.md)
- [Analysis API interface document](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured text with optional report links and saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call a configured Life Emergence service for image/video analysis and cloud report-history queries.]

## Skill Version(s):

1.0.9 (source: server-resolved ClawHub release metadata; SKILL.md frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
