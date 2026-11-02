## Description:

Analyzes images and videos from smart feeder or IPC cameras to detect cats and dogs, recognize individual pets, enroll pets, and retrieve past reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and developers use this skill to analyze feeder or IPC camera media, distinguish cats and dogs and individual pets, enroll pets, and review cloud-hosted analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The no-analysis option may not prevent media from being analyzed.

Mitigation: Confirm this option's behavior before use and test with non-sensitive media.

Risk: Media is sent to a cloud service, and retention and account isolation are unverified.

Mitigation: Ask the publisher to explain uploads and retention; use non-sensitive test media with an isolated account or workspace.

Risk: Automatic account setup and credential handling lack clear safeguards.

Mitigation: Make account setup explicit, protect stored credentials, and restrict authenticated requests to approved HTTPS destinations.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-detection-feeder-analysis)
- [API interface reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured pet analysis results and report links, with JSON or Markdown output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include detection results, pet identity and enrollment details, suggestions, and historical report listings. Analysis is for feeding reference and requires human confirmation.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
