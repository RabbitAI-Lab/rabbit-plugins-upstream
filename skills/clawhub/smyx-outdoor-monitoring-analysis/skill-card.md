## Description:

Detects targets such as people, vehicles, non-motorized vehicles, and pets within target areas; supports batch image analysis for outdoor surveillance scenarios such as courtyards, orchards, and farms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze outdoor monitoring images, videos, or URLs for people, vehicles, non-motorized vehicles, pets, and intrusion-risk reporting in courtyards, orchards, farms, and similar security contexts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted images, videos, or URLs may be sent to external analysis services.

Mitigation: Confirm the configured endpoints and publisher trust before use, and avoid sending sensitive media unless data handling is acceptable.

Risk: The skill may create or reuse a local identity and cache authentication tokens in a workspace SQLite database.

Mitigation: Run in a dedicated workspace, protect workspace data, and clear cached identity or token data when no longer needed.

Risk: Packaged configuration may point to development HTTP endpoints on a private IP.

Mitigation: Review configuration before installation and replace non-production or private endpoints with trusted production endpoints when appropriate.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-outdoor-monitoring-analysis)
- [Publisher Profile](https://clawhub.ai/user/18072937735)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration]

**Output Format:** [Markdown report or JSON returned from command-line analysis and history-query calls.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and an optional output file; accepts local media file paths or public media URLs.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
