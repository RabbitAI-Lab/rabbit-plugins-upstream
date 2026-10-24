## Description:

Retrieve source-attributed GoodRx medication and health information and cross-check safety-critical claims against official FDA or NIH sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Agents assisting people with general medication or condition research summarize GoodRx sources and check safety-critical claims against official drug information. The results are not personalized medical advice or treatment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup queries and the Crawlora API key are sent to a third-party service.

Mitigation: Use only if comfortable sharing queries and the API key with Crawlora; do not enter personal medical or prescription details.

Risk: Secondary or outdated content can lead to misleading medication safety claims.

Mitigation: Check safety-critical claims against matched FDA or NIH sources, retain source review dates, and label unverified claims.

Risk: General drug information could be mistaken for individual treatment advice.

Mitigation: Do not provide personalized diagnosis, dosing, or treatment decisions; refer those questions to a qualified clinician or pharmacist.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/medication-information-research)
- [Endpoint reference](reference/endpoints.md)
- [FDA: Find Information about a Drug](https://www.fda.gov/drugs/information-consumers-and-patients-drugs/find-information-about-drug)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Source-linked Markdown brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies the question and population, cites sources and review dates, and flags unsupported or conflicting claims.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
