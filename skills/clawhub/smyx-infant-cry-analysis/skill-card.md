## Description:

Detects baby cries with audio AI, analyzes likely causes, and returns structured guidance about needs such as hunger, tiredness, pain, discomfort, or irritability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and caregivers use this skill to submit infant cry audio or video for cloud-based analysis and receive structured reports, likely-cause classifications, suggestions, and report links. Developers and agents can also use it to query prior cloud reports when the user asks for analysis history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload sensitive infant audio, video, or media URLs to Life Emergence cloud services for analysis.

Mitigation: Use the skill only when cloud processing of sensitive family media is acceptable, and avoid submitting media that should remain local.

Risk: The skill may create or reuse a local identity and bind cloud report history to that identity.

Mitigation: Review identity behavior before installation and run it only in workspaces where persistent identity binding is acceptable.

Risk: The skill may store authentication tokens in a workspace SQLite database.

Mitigation: Restrict workspace access, protect generated data files, and clear local state according to the deployment's retention policy.

Risk: History-related prompts can retrieve prior cloud reports automatically.

Mitigation: Confirm that automatic history retrieval is appropriate for the user and environment before enabling the skill.

Risk: Infant cry classifications and suggestions are assistive and may be incorrect or incomplete.

Mitigation: Treat results as parenting support only and seek medical care when crying, pain, illness, or distress persists.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-cry-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Analysis API Error Codes](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [analysis, markdown, json, guidance, shell commands]

**Output Format:** [Markdown or JSON text with structured analysis results, suggestions, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write analysis output to a user-specified file path when requested.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter states 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
