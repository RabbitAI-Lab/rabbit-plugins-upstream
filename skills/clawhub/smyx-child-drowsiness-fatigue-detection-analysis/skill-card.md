## Description:

Analyzes classroom or home-study child face videos to estimate visual drowsiness indicators such as PERCLOS, head-nodding frequency, eye-region changes, fatigue score, fatigue level, and rest reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers, parents, and developers can use this skill to submit child study-area video files or URLs for visual fatigue assessment and to query previously generated fatigue reports. It is an auxiliary monitoring aid and not a medical or sleep-disorder diagnostic tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child video data and report history may be handled by remote services.

Mitigation: Obtain guardian consent before use, verify the configured API endpoint, and confirm retention, deletion, and access-control practices before uploading classroom or home-study videos.

Risk: The skill silently reuses or creates cloud-linked identities and stores local token/report state.

Mitigation: Run the skill in an isolated workspace, restrict access to local data files, and review or clear locally stored identity and token state when changing users or environments.

Risk: Visual fatigue scores and reminders could be mistaken for medical or sleep-disorder diagnosis.

Mitigation: Present outputs as auxiliary rest-reminder guidance only and route persistent or severe drowsiness concerns to parents, teachers, or qualified medical professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-drowsiness-fatigue-detection-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Child drowsiness/fatigue API reference](references/api_doc.md)
- [Shared analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown report text with JSON-structured analysis content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fatigue metrics, drowsiness events, voice-prompt text, history-list records, and report export URLs.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
