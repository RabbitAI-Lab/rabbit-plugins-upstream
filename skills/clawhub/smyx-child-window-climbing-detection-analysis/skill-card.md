## Description:

Analyzes fixed-camera video of windows or balconies to detect child climbing, leaning, gripping, or crossing behaviors and produce alert-oriented structured results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit local or URL-based child safety camera footage for cloud analysis and to retrieve structured alert reports for window or balcony climbing risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud processing may send minor-related home video or video URLs to lifeemergence.com services.

Mitigation: Use only when consent, retention, deletion, and cloud processing controls have been verified for the deployment.

Risk: The skill may create or reuse a cloud-linked identity and store access tokens locally.

Mitigation: Install only in controlled environments, restrict local data access, and clear local identities or tokens when they are no longer needed.

Risk: Cloud history retrieval may expose prior child-safety reports.

Mitigation: Limit who can trigger history queries and verify account-access boundaries before enabling the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-window-climbing-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, files]

**Output Format:** [Markdown or JSON structured analysis output, with optional saved result file and report link.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report links and history records; supports mp4, avi, and mov inputs up to 10 MB.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
