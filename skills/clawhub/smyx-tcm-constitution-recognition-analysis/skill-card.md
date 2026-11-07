## Description:

Determines nine TCM constitution types including Yin deficiency, Yang deficiency, Qi deficiency, phlegm-dampness, and blood stasis through facial features and physical signs, and provides personalized health preservation and conditioning suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

People seeking a traditional Chinese medicine constitution assessment can provide a face image or video to receive a report with constitution tendencies and general wellness suggestions. They can also request a list of their previous reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Different users may share a health-report account, which can associate users with the same report account.

Mitigation: Defer use with shared-user agents until sender isolation is fixed; require clear account-registration and upload controls.

Risk: The no-analysis option does not prevent facial media from being uploaded.

Mitigation: Defer use with real facial media until this is fixed, and make upload behavior clear before media is provided.

Risk: Backend authorization and provider retention or deletion practices are unverified; token storage also needs protection.

Mitigation: Confirm authorization and retention/deletion practices, and protect tokens before use with personal media.

Risk: Changing --api-url does not change the media recipient.

Mitigation: Do not rely on --api-url to redirect uploads; verify the recipient before sending media.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill introduction](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-tcm-constitution-recognition-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text, Markdown]

**Output Format:** [JSON or text analysis report; Markdown table for report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include constitution types, tendencies, scores, health-risk notes, and personalized wellness suggestions.]

## Skill Version(s):

1.0.17 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
