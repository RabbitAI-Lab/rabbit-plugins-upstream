## Description:

Analyzes fixed-camera pet sleep videos or URLs to estimate sleep and wake periods, sleep duration, roll-over or position-change counts, startle-awakening frequency, and a sleep-quality score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze pet bed or rest-area footage for sleep-quality indicators and historical sleep reports. It is intended for sleep-health reference and monitoring workflows, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill uploads or forwards pet videos or URLs to cloud services.

Mitigation: Use only media and URLs that are appropriate for cloud processing, and avoid sensitive household footage or private/internal URLs unless the publisher documents retention and URL-fetch protections.

Risk: The security evidence says the skill silently creates or reuses an internal identity and stores service tokens locally.

Mitigation: Run it in a controlled workspace, review local token handling before deployment, and avoid shared environments where account data could be exposed.

Risk: The skill reports sleep-health indicators that could be mistaken for medical conclusions.

Mitigation: Present outputs as visual sleep-monitoring reference only and direct users to a veterinarian for persistent abnormal findings.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-sleep-quality-analysis-analysis)
- [API Interface Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or JSON-style structured analysis report with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sleep metrics, risk prompts, recommendations, historical report links, and cloud-backed API results.]

## Skill Version(s):

1.0.11 (source: frontmatter; server release metadata reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
