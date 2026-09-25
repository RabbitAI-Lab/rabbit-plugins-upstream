## Description:

Analyzes pet feeding videos to estimate eating speed and duration, provide slow-feeding recommendations, and retrieve past reports without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and developers of smart feeding products use this skill to analyze feeding videos, review eating-speed reports, and identify when a slow-feeding intervention may be appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos or video URLs are sent to an external analysis service.

Mitigation: Obtain consent before submitting media and avoid sharing unnecessary personal or location information.

Risk: The skill can silently create or reuse an account identity and store service tokens locally.

Mitigation: Require explicit consent before account creation and protect or remove stored credentials according to local policy.

Risk: History queries can retrieve reports associated with the account identity.

Mitigation: Request consent before history lookups and share retrieved reports only with the intended user.

## Reference(s):

- [Pet eating analysis API documentation](artifact/references/api_doc.md)
- [Analysis API errors and authentication](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown history table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes eating duration, speed estimates, recommendations, and report links; may be saved to a file. Device interventions are not performed by this skill.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; artifact frontmatter lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
