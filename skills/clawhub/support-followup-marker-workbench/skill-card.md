## Description:

Build a support case comment from a prepared support digest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Support operations staff use a prepared case digest to create a concise follow-up comment and tags, with a local record of the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes local support artifacts, which may contain case details.

Mitigation: Use a dedicated, access-controlled output directory and review the records it creates.

Risk: A configured delivery target can automatically send generated support records externally.

Mitigation: Review before installation; clear or tightly control CLAWHUB_DELIVERY_ENDPOINT, CLAWHUB_DELIVERY_API_KEY, and SMTP-related variables unless delivery is intended.

## Reference(s):

- [Support Case Workbench on ClawHub](https://clawhub.ai/wxt-ai/skills/support-followup-marker-workbench)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Structured JSON case comment with text and tags]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a local support record and may return a delivery receipt when external delivery is configured.]

## Skill Version(s):

1.1.1 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
