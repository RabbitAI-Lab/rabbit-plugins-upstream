## Description:

Analyzes fixed-camera home video of older adults living alone to detect behavior indicators such as dazing, sighing, and self-talking, then returns behavior statistics, an emotional-risk level, reminders, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Family members, caregivers, and community workers can use this skill to review uploaded home camera footage for behavior-based loneliness or depression-tendency indicators and receive structured risk summaries. The output should support care outreach and observation workflows, not medical diagnosis or treatment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles highly sensitive in-home video and mental-health-adjacent reports through a vendor cloud service.

Mitigation: Use it only with informed consent from the elder or legal guardian, and confirm retention, deletion, export-link security, and access-control terms with the publisher before using real household footage.

Risk: The skill automatically creates or reuses persistent identity records and stores authentication tokens.

Mitigation: Review token storage and access controls before installation; prefer isolated runtime credentials and clear or rotate stored tokens when access should end.

Risk: Behavior signals such as dazing, sighing, or self-talking may be confused with ordinary activities or may be misread as a medical diagnosis.

Mitigation: Treat outputs as behavior-based risk prompts only, require human review, and route clinical concerns to qualified medical or mental-health professionals.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-loneliness-depression-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown text with structured JSON-style analysis results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a file when an output path is provided; history queries are rendered for the agent as Markdown-style report listings.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
