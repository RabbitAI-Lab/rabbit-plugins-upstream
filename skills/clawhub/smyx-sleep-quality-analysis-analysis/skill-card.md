## Description:

This skill analyzes fixed-camera pet sleep videos to estimate sleep and awake states, total sleep duration, roll-over and startle-awakening counts, and a 0-100 sleep-quality score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, pet owners, veterinary staff, boarding centers, and developers use this skill to analyze pet rest-area video for sleep-duration, movement, awakening, and sleep-quality indicators. The results are sleep-health reference signals, not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet video, video URLs, and identity-linked report requests are processed by remote provider services.

Mitigation: Use only footage appropriate for provider-side processing, avoid sensitive home, clinic, or third-party footage, and confirm the provider's retention and deletion terms before use.

Risk: Report history is tied to an automatically selected or created persistent identity.

Mitigation: Run the skill in an isolated workspace when identity separation matters and avoid sharing workspaces across unrelated users or projects.

Risk: Tokens and user records may be stored in the workspace data directory.

Mitigation: Restrict workspace access, clean the data directory after testing when appropriate, and avoid running the skill from shared or untrusted workspaces.

Risk: Sleep-quality outputs are reference signals and may be mistaken for veterinary diagnosis.

Mitigation: Present results as observational sleep metrics and recommend professional veterinary review for persistent or severe abnormalities.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-sleep-quality-analysis-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet sleep quality analysis API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Analysis]

**Output Format:** [Markdown report text with optional JSON detail and optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a report link and history table when querying prior analyses.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter lists 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
