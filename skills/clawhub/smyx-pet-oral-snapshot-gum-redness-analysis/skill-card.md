## Description:

Analyzes pet oral images or videos to describe gum color, redness, and tartar coverage, without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and developers of pet cameras or health platforms can assess oral snapshots for visible gum redness and tartar, review observations and recommendations, and retrieve prior reports. The observations are not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media and supplied URLs are sent to LifeEmergence cloud services.

Mitigation: Use only with appropriate consent; avoid sensitive household media and review cloud data handling before uploading.

Risk: The skill silently creates or reuses a local user identity and stores authentication tokens and report history in the workspace.

Mitigation: Run in an isolated workspace and confirm how to remove local data/smyx-common-claw.db and data/smyx-api-key.txt before using real user data.

Risk: History queries may access cloud reports without clear user-directed consent.

Mitigation: Confirm the user's intent and authorization before retrieving cloud report history.

## Reference(s):

- [Pet oral analysis API documentation](artifact/references/api_doc.md)
- [Skill usage introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured oral-health observations and report links; JSON reports or Markdown tables for history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include gum color, tartar estimates, risk prompts, and recommendations; results can be saved to a file.]

## Skill Version(s):

1.0.16 (source: server release metadata; artifact frontmatter says 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
