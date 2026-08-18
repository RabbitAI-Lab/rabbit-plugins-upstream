## Description:

Automatically detects smoking behavior in target areas based on computer vision; supports real-time detection of video streams, images, and video files; identifies violation smoking behavior and triggers violation alerts, assisting in smoking control safety management for parks/communities/units.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Facility managers, safety teams, and developers use this skill to analyze uploaded images, videos, or media URLs for smoking behavior and retrieve cloud-hosted detection reports for smoking-control workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded surveillance media, media URLs, and report queries may be processed by external services.

Mitigation: Use only approved media, confirm user consent and data handling requirements, and verify the configured backend endpoints before execution.

Risk: The skill may silently create or reuse account identities and store user tokens in the workspace.

Mitigation: Run it in an isolated workspace, review local credential storage before and after use, and clear stored tokens when they are no longer needed.

Risk: Packaged configuration includes dev or private HTTP endpoints.

Mitigation: Replace default endpoints with approved production HTTPS services before commercial deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-smoking-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands]

**Output Format:** [Markdown reports or JSON structured results with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write results to a user-specified output file; supports basic, standard, and json detail levels.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
