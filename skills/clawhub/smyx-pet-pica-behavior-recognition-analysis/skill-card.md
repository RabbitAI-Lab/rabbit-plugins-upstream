## Description:

Analyzes indoor pet camera videos from local files or URLs by calling server-side APIs to detect sustained contact between a pet's mouth and non-food hazardous items such as electric wires, plastic, socks, tissues, and toy fragments, then returns a safety warning without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill for pet safety monitoring workflows that analyze indoor video, identify possible pica behavior around hazardous non-food objects, and produce warning-oriented reports or history tables. The output is for safety monitoring and intervention guidance, not veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indoor camera videos may be uploaded to provider-operated APIs for analysis.

Mitigation: Install and use the skill only where uploading that video content to the provider is acceptable.

Risk: The skill can create or reuse local/cloud identities and cache access tokens in the workspace data directory.

Mitigation: Run it in a separate workspace or account and clear stored tokens and reports when they should not persist.

Risk: Historical report queries can fetch prior cloud reports with limited user control.

Mitigation: Use accounts where reused report history is expected, and review cloud report access before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-pica-behavior-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet pica behavior API documentation](artifact/references/api_doc.md)
- [Common analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown report or JSON analysis result, with optional Markdown tables for history queries and shell commands for invoking the packaged script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk level, detected object categories, intervention suggestions, report links, and historical report listings.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
