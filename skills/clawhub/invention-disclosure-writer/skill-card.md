## Description:

Turns R&D materials or an early technical idea into a patent invention-disclosure document in Word, with review notes and patent-reference comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Inventors, R&D teams, and developers use the skill to organize a technical proposal or project materials into an invention-disclosure document for review by a patent professional, or to explore possible invention directions. It does not produce a patent application or guarantee patentability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags API-key storage and redirect-handling weaknesses.

Mitigation: Before using paid credentials, restrict authenticated redirects to the intended HTTPS service, keep credential files owner-only, and provide keys through the documented environment variable rather than conversation.

Risk: Source materials are sent to the service for processing and may include sensitive, unfiled invention details.

Mitigation: Upload only materials you are authorized to share, and review the service's confidentiality and retention terms before submitting sensitive information.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/invention-disclosure-writer)
- [PatentMax service](https://api.ip930.com)
- [PatentMax API platform and account information](https://api.ip930.com/features/api-platform)

## Skill Output:

**Output Type(s):** [documents, text, guidance]

**Output Format:** [Microsoft Word (.docx) invention-disclosure and review-notes documents; idea-direction results are also provided as structured text.]

**Output Parameters:** [Based on supplied R&D files or an idea; may include invention points, technical description, diagrams, patent-reference comparisons, and items for inventor review.]

**Other Properties Related to Output:** [Materials are sent to the PatentMax service for generation. Users should avoid uploading confidential or unfiled invention details unless authorized and comfortable with the service's confidentiality and retention terms. Review inferred facts before sharing the document with a patent professional.]

## Skill Version(s):

1.1.8

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
