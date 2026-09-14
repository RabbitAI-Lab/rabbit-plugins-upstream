## Description:

Identifies bird species in images or videos of target areas, supports recognition for at least 500 common bird species, and can support customized model training for ecological observation, garden birdwatching, and related scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to identify bird species in uploaded images, videos, or public media URLs and to retrieve structured bird recognition reports. It is intended for nature observation, birdwatching, biodiversity surveys, and ecological monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says this cloud-based skill can send user media, identity values, and authentication tokens over plaintext HTTP despite claiming HTTPS/TLS.

Mitigation: Review before installing, avoid sensitive media, and use only if the publisher enforces HTTPS, documents account and token handling, and avoids plaintext token storage.

## Reference(s):

- [Bird Recognition API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Structured text or JSON-like report content, Markdown report listings, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include species recognition results, confidence information, recommendations, historical report records, and report links.]

## Skill Version(s):

1.0.20 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
