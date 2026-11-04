## Description:

Analyzes images and video to detect cats, dogs, and birds and return structured pet detection results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Household pet owners can submit an image, video, or media URL to identify and count cats, dogs, and birds, and query previous detection reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automatically enrolls accounts and stores credentials; household media and URLs are sent to Life Emergence's cloud, where deletion and account isolation could not be verified from the client.

Mitigation: Require explicit account enrollment, use separate identities for each user, protect credentials, submit only intended media and URLs, and avoid shared workspaces or unrelated API secrets.

Risk: The advertised --export-env-only mode may still submit media.

Mitigation: Do not rely on this mode until the issue is fixed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-detection-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured JSON or formatted text; historical reports can be presented as Markdown tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Detection results can include species counts, confidence values, and report links.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
