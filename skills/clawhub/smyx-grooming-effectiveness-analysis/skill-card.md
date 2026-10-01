## Description:

Analyzes pet grooming images or videos to estimate coat matting, shed hair, and hairball risk and produce a care report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and care professionals can submit grooming images, videos, or URLs to assess coat condition and shed hair and review historical grooming reports. Results are grooming guidance, not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images, videos, or URLs are sent to a remote analysis service.

Mitigation: Use only with consent for remote processing; avoid submitting sensitive media or private URLs.

Risk: A shared workspace identity and locally stored tokens can expose one user's cloud report history to another user.

Mitigation: Avoid shared or multi-user workspaces unless identities, tokens, and report access are isolated per user.

Risk: Visual estimates of grooming and hairball risk may be mistaken for a medical diagnosis.

Mitigation: Treat the results as care guidance only and consult a veterinarian for health concerns.

## Reference(s):

- [Grooming analysis API documentation](artifact/references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-grooming-effectiveness-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown analysis report or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include risk level, grooming recommendations, report links, and a cloud report history table.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release metadata; bundled SKILL.md lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
