## Description:

Analyzes close-up pet face images or video for visible eye abnormalities such as conjunctival redness, abnormal tearing or tear stains, and pupil or cornea opacity, then returns alerts, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners, boarding center operators, and veterinary staff use this skill to screen pet eye images or videos for visible signs of redness, tearing, opacity, and left-right asymmetry. The output supports daily health checks, routine inspections, triage, and senior pet monitoring, but it is not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images or videos, report metadata, and an automatically generated or reused identity may be sent to a remote service.

Mitigation: Use only media appropriate for service transmission, review retention and token handling before deployment, and avoid sensitive media when those controls are unacceptable.

Risk: The packaged endpoint configuration includes development HTTP addresses.

Mitigation: Review the endpoint configuration before use and replace it with approved production HTTPS endpoints for the deployment environment.

Risk: Authentication tokens may be persisted locally.

Mitigation: Run the skill in a controlled environment, inspect local token storage behavior, and clear or rotate credentials according to organizational policy.

Risk: Visual screening can be unreliable when images are blurry, backlit, poorly framed, or when breed-specific eye features affect appearance.

Mitigation: Use clear, well-lit close-up media with both eyes visible, treat outputs as screening guidance only, and refer suspected abnormalities to a veterinarian.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-eye-anomaly-detection-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report or JSON, depending on the selected detail and output options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include anomaly levels, health suggestions, historical report tables, and report links; results can optionally be saved to a file.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
