## Description:

Analyzes aquarium fish videos for flashing and scraping behavior, counts abnormal contact events, and flags possible ectoparasite risk for follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarists and aquarium operators can use the skill to review fish footage for repeated scraping or flashing and receive a risk prompt and suggested follow-up. The output is a behavior warning and does not diagnose a specific disease.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The cloud analysis service may register an account, store access tokens, and upload video even when an export-only request is made.

Mitigation: Review the provider's upload, account, and billing terms before use; avoid sensitive footage and existing credentials until the behavior is resolved.

Risk: Documented video-retention limits are not enforced by the bundled client, and processing is not local-only.

Mitigation: Confirm the provider's retention and deletion terms before uploading footage, and do not rely on local processing or the documented retention period as a control.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-fish-flashing-scraping-detection-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API and behavior analysis reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report with event counts, risk prompts, suggested follow-up, and report links; JSON or Markdown presentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports observed flashing and scraping frequency and duration when available; recommendations are informational and do not establish a veterinary diagnosis.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata; artifact frontmatter states 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
