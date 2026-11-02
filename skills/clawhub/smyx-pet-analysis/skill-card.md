## Description:

Analyzes cat, dog, and bird videos through a remote service and returns a structured pet health report with potential concerns and care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caretakers can submit a local video or video URL for a cat, dog, or bird to receive a structured health report with potential concerns and care suggestions, and can request a list of prior reports. Results are for reference and do not replace a veterinarian's diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the skip-analysis option is ignored and that automatic account handling does not match the stated privacy assurances.

Mitigation: Ask the publisher to fix the option behavior and clearly disclose account creation and local token storage before installing.

Risk: Videos are sent to LifeEmergence for processing, and the supplied files cannot verify the claim that originals are deleted immediately afterward.

Mitigation: Treat deletion as unverified; send only media you are comfortable sharing, use an isolated workspace, and avoid supplying unrelated credentials.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-analysis)
- [Skill introduction demo](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Report links]

**Output Format:** [Structured text or JSON health reports; history can be presented as a Markdown table with report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include potential health concerns and care suggestions; they are not a veterinary diagnosis.]

## Skill Version(s):

999.999.1011 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
