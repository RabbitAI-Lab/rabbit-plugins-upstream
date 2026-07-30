## Description: <br>
Extracts a user's writing voice from text samples via SICO comparative analysis <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and writing teams use this skill to collect writing samples, compare them against baseline model output, and create local voice profiles and registers for consistent style generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Writing samples and derived voice profiles may contain sensitive personal or proprietary text and are saved locally under ~/.claude/voice-profiles. <br>
Mitigation: Review and redact samples before use, limit inputs to material safe for local storage, and delete the profile directory when it is no longer needed. <br>
Risk: The directory-copy workflow may preserve identifying details even though the skill instructs users to anonymize samples. <br>
Mitigation: Confirm filenames, headers, dates, URLs, proper nouns, and other identifiers are removed before extraction. <br>
Risk: AI-detectability framing may be inappropriate in academic, compliance, or disclosure-sensitive contexts. <br>
Mitigation: Use the extracted style profile only where style adaptation is allowed and disclose or avoid use when policy requires it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-voice-extract) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash and JSON examples; produced profile artifacts are Markdown and JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates local voice profile files under ~/.claude/voice-profiles/{name}; user-provided writing samples may be copied into that profile directory.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
