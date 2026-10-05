## Description:

Helps agents coordinate AdsTurbo image, video, and digital-human creation and editing across multi-step creative workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to guide an agent through multi-step AdsTurbo workflows, such as creating an ad, replacing a spokesperson, and translating the resulting video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploading private or sensitive photos, voices, or videos may expose them via public asset URLs.

Mitigation: Use only authorized media and obtain consent; avoid sensitive uploads unless public URL exposure is acceptable.

Risk: Submitting generation or editing jobs can charge credits, and resubmission after a timeout can charge twice.

Mitigation: Confirm with the user before paid submissions; check existing job status instead of resubmitting on timeout.

Risk: Deleting a digital-human persona may be irreversible.

Mitigation: Require explicit user confirmation before persona deletion.

## Reference(s):

- [AdsTurbo skill on ClawHub](https://clawhub.ai/adsturbo/skills/adsturbo)
- [AdsTurbo API key setup](https://adsturbo.ai/iris/api)
- [AdsTurbo plans](https://adsturbo.ai/pricing)
- [Media upload guidance](references/upload.md)
- [Async task guidance](references/work.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Text or Markdown with result links and optional commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media creation tasks may run asynchronously; results are shared as links.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
