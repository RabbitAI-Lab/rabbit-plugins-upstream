## Description:

Qinghu Rednote Social helps agents research Xiaohongshu trends, notes, comments, and creator profiles through Qinghu APIs to build seeding topics, pain-point libraries, KOC/KOL shortlists, and posting plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, social media operators, and agents use this skill to research Xiaohongshu topics, analyze high-performing notes and comments, identify audience pain points, shortlist KOC/KOL creators, and prepare seeding plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a user-authorized Qinghu API token for Xiaohongshu research.

Mitigation: Request the token only when needed, prefer configured token environment variables when available, and avoid exposing the token in outputs or exported files.

Risk: Qinghu API calls may consume user credits.

Mitigation: Get user approval before API calls and report actual Qinghu credit usage from the API response when available.

Risk: Large result sets may be exported to local files that contain sensitive campaign, creator, or audience research.

Mitigation: Tell users where exports were written and recommend deleting sensitive exports when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-rednote-social)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown summaries with optional local exported files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include topic lists, note-structure templates, pain-point excerpts, creator shortlists, campaign pacing guidance, and Qinghu API credit usage notes.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
