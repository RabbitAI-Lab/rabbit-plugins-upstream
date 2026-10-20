## Description:

Searches patents and other public literature for prior art, compares technical features, and prepares a novelty assessment with a downloadable report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Inventors and R&D teams use the skill to check whether a technical proposal appears in prior art, compare relevant patent and public-literature disclosures, and prepare material for internal review or pre-filing assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpublished invention details are sent to PatentMax during a search.

Mitigation: Confirm PatentMax's confidentiality and retention terms before submitting sensitive material.

Risk: Service credentials and local cached credentials could be exposed.

Mitigation: Use a limited-scope key through the environment rather than chat, and protect locally cached credentials.

Risk: Paid searches incur charges, and report generation can take tens of minutes.

Mitigation: Confirm current pricing before starting; cancel if needed and allow time for report completion.

Risk: Search results are not an official or guaranteed patentability determination.

Mitigation: Verify cited documents and treat the assessment as technical reference; seek qualified review for formal conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ip930/skills/prior-art-search)
- [PatentMax API platform information](https://api.ip930.com/features/api-platform)
- [Solution writing guide](references/solution-guide.md)
- [Workflow guide](references/workflow.md)
- [Frequently asked questions](references/faq.md)

## Skill Output:

**Output Type(s):** [Analysis, Files, Guidance]

**Output Format:** [Markdown response and downloadable Word (.docx) report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides cited prior-art comparisons and an indicative assessment, not a guarantee of patentability.]

## Skill Version(s):

1.1.5 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
