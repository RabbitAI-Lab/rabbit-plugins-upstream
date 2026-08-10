## Description:

Analyzes pet full-body images or videos through server-side APIs to identify breed or body type and fur density, then returns a non-medical drying temperature and duration curve for grooming devices or pet-care workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External pet-care providers, grooming salons, smart dryer operators, and developers use this skill to submit pet images, videos, or URLs and receive structured drying-temperature recommendations plus report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media or URLs are sent to remote analysis services and may include people, private spaces, or sensitive metadata.

Mitigation: Use only media that is appropriate for remote processing, and avoid inputs that include people, private spaces, or sensitive metadata.

Risk: The skill silently creates or reuses an internal identity, queries report history, and stores authentication-related state locally.

Mitigation: Deploy only where that identity behavior and local token storage are acceptable; restrict local file access and clear stored state when it is no longer needed.

Risk: Drying recommendations are not medical advice, and unsuitable temperature settings can harm vulnerable pets.

Mitigation: Review recommendations before device use, stay within documented safety limits, and lower temperatures for young, older, or flat-faced pets as the artifact guidance states.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-adaptive-pet-drying-temperature-analysis)
- [Pet drying temperature API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown text with structured JSON results, temperature-duration recommendations, history lists, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a file when an output path is provided; history queries return structured report lists from the remote service.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
