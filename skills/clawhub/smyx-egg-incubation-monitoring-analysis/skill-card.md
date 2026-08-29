## Description:

Analyzes turtle or snake egg images or videos from incubator cameras to classify visible shell, vascular, embryo, mold, and signal-quality indicators and produce an incubation progress report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile breeders, breeding farms, and smart-incubator developers use this skill to review turtle or snake egg media, track egg-level incubation status, and surface non-invasive follow-up actions. It can also retrieve cloud-backed historical incubation reports for the associated user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media and history data are sent to backend services for analysis and report retrieval, with limited disclosure about upload handling or retention.

Mitigation: Use only non-sensitive egg images or videos, review the publisher's service terms before deployment, and require clear upload and retention disclosure before production use.

Risk: The skill can silently create or reuse a user identity and locally store service tokens.

Mitigation: Install only in an isolated workspace, review local token storage behavior before use, and require a user-visible way to manage or disable stored identity tokens.

Risk: Incorrect visual classifications could affect breeding decisions, especially for fertilization, blood-ring, mold, or pre-hatching status.

Mitigation: Treat results as decision support, verify important findings against species incubation records and breeder judgment, and avoid invasive actions or exact environmental adjustments based only on the skill output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-egg-incubation-monitoring-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown and JSON-formatted structured analysis text, with optional report export links and history listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include incubation stage labels, alert levels, recommended non-invasive actions, disclaimers, report image URLs, and cloud history query results.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
