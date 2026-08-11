## Description:

Automatically backs up new Plaud recordings to Google Drive, saves transcripts, classifies each recording, and logs links and metadata in Google Sheets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to keep Plaud recordings, transcripts, recording classifications, and tracking metadata synchronized into their own Google Drive and Google Sheets accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow syncs new Plaud recordings and transcripts into Google Drive and Google Sheets.

Mitigation: Review the connected Google accounts' sharing, retention, and compliance settings before using the skill for confidential, regulated, or third-party recordings.

Risk: When Plaud transcripts are unavailable, audio may be sent to the configured speech-to-text service.

Mitigation: Use the fallback only for recordings that are appropriate for the configured transcription provider and the user's data handling requirements.

Risk: A run that stops after claiming a spreadsheet row can leave that row unfinished.

Mitigation: Review rows with Status set to 'claimed' and rerun the workflow or resolve the row manually.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/plaud-recordings-to-google-drive-sync)
- [AgentPMT workflow homepage](https://www.agentpmt.com/agent-workflow-skills/plaud-recordings-to-google-drive-sync)
- [Google Sheets tool skill](https://clawhub.ai/agentpmt/google-sheets)
- [Google Drive tool skill](https://clawhub.ai/agentpmt/google-drive)
- [Plaud tool skill](https://clawhub.ai/agentpmt/plaud)
- [Speech to Text With Speakers tool skill](https://clawhub.ai/agentpmt/speech-to-text-with-speakers)

## Skill Output:

**Output Type(s):** [guidance, configuration, API calls, files, text]

**Output Format:** [Markdown instructions with JSON tool-call examples; runtime outputs are Google Drive files, Google Sheets rows, and a text run summary.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires connected Plaud, Google Drive, and Google Sheets accounts; may use a configured speech-to-text service when Plaud transcripts are unavailable.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
