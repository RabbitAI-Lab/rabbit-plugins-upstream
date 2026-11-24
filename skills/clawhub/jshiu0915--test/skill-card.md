## Description:

Converts audio files to text using the Baidu Smart Cloud speech recognition API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jshiu0915](https://clawhub.ai/user/jshiu0915)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill to transcribe local audio files with Baidu Smart Cloud, including batch processing for Mandarin, English, Cantonese, and Sichuanese speech. It writes transcription text, API response JSON, and processing reports to the configured output directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected audio files are sent to Baidu Smart Cloud for transcription and may contain sensitive content.

Mitigation: Use non-sensitive test audio first and run the skill only when the selected audio is appropriate to share with Baidu Smart Cloud.

Risk: Baidu API credentials can be exposed through command history, committed config files, or shared logs.

Mitigation: Prefer environment variables or a secret manager, keep credentials out of committed files, and rotate exposed credentials promptly.

Risk: Python dependencies affect runtime security and reliability.

Mitigation: Install in a virtual environment and pin and review dependencies before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jshiu0915/skills/test)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, JSON, files]

**Output Format:** [Plain text transcription files, JSON API responses, JSON processing reports, and JSON console summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Baidu Smart Cloud API credentials and sends selected audio files to Baidu Smart Cloud for transcription.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
