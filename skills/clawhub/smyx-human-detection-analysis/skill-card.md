## Description:

Detects personnel in target areas from images, videos, local files, or URLs using computer vision and returns structured monitoring reports for parks, offices, and restricted areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and security operations teams use this skill to analyze surveillance video or images for personnel presence, counts, frequency, and intrusion indicators in defined areas. Developers can invoke its bundled commands to run analysis or query cloud-stored report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surveillance media, video URLs, platform identity values, and generated reports may be sent to an external service and associated with a persistent account.

Mitigation: Review data handling before deployment, disclose cloud processing and retention expectations, and require explicit user control before media upload or cloud history queries.

Risk: Development HTTP defaults may expose media, identity data, or tokens over unencrypted endpoints.

Mitigation: Remove development endpoint defaults before release and enforce HTTPS for all service URLs.

Risk: Persistent local identity state may be created or reused without being obvious to the user.

Mitigation: Document account creation and identity reuse behavior, and provide a way to inspect, rotate, or clear stored identity state.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-human-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write analysis results to a user-specified output file.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
