## Description:

Identifies bird species in images or videos of target areas, supports recognition of at least 500 common bird species, and can query cloud-hosted recognition report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecological monitoring teams use this skill to submit bird images, videos, or media URLs for species identification and structured recognition reports. It is suitable for nature observation, garden birdwatching, biodiversity surveys, and reviewing prior cloud report history tied to the user's resolved identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded images, videos, supplied URLs, and report queries are sent to the Life Emergence analysis service.

Mitigation: Install only when sending this media and report context to that service is acceptable for the intended workflow.

Risk: The skill creates or reuses a hidden local or cloud identity and ties report history to that identity.

Mitigation: Review identity and report-history behavior before deployment and require explicit user control where the deployment policy needs it.

Risk: The authoritative security evidence flags hidden identity reuse, local token storage, unsafe credential-handling paths, and dev HTTP defaults.

Mitigation: Before approval, remove dev HTTP defaults, restrict credentialed requests to approved HTTPS hosts, avoid plaintext token storage, and fix the dependency declaration noted by the scanner guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-bird-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Bird recognition API documentation](artifact/references/api_doc.md)
- [Analysis API error codes](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, API calls, files, guidance]

**Output Format:** [Markdown or JSON text with optional report export links and optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and json detail modes; local media input is limited to configured formats and a 10 MB maximum.]

## Skill Version(s):

1.0.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
