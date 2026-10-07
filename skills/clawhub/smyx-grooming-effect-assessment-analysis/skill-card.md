## Description:

Assesses post-grooming pet images or videos for residual mats, dandruff, and coat smoothness, then provides a grooming score and follow-up care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and grooming professionals use post-grooming photos or videos to assess remaining mats, dandruff, and coat condition, and to decide whether another grooming pass is needed. The skill can also retrieve prior assessment reports from its cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images, videos, or supplied URLs are sent to a configured cloud service for assessment.

Mitigation: Submit only media and URLs approved for external processing; avoid sharing sensitive content.

Risk: The skill creates or reuses a local account identity and caches remote authentication tokens in a workspace SQLite database.

Mitigation: Run in a trusted workspace, restrict access to stored account data, and clear it when no longer needed.

Risk: History phrases can trigger retrieval of cloud reports associated with the local identity.

Mitigation: Confirm the user is authorized to view those reports before querying or sharing report links.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-grooming-effect-assessment-analysis)
- [Grooming assessment API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured assessment text or Markdown, with report links and optional JSON-formatted results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a 0–100 grooming score and follow-up suggestions; history queries produce a Markdown report list. Results are visual assessments, not medical diagnoses.]

## Skill Version(s):

1.0.12 (source: server-resolved release metadata; packaged frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
