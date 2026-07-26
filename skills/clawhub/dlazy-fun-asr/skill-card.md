## Description: <br>
Alibaba Bailian Fun-ASR recording transcription supports Chinese, English and other languages, with auto language detection and speaker diarization for subtitles, transcription, and meeting notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent operators use this skill to send recording files to dLazy's hosted Fun-ASR service for multilingual transcription, speaker diarization, subtitle preparation, and meeting notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided audio, video, image, and parameters may be sent to dLazy as a third-party cloud processor. <br>
Mitigation: Use the skill only when that processing is acceptable for the data involved, avoid sensitive recordings unless policy permits it, and review dLazy service terms for retention and access practices. <br>
Risk: Authentication can store a dLazy API key in the local CLI configuration. <br>
Mitigation: Use the DLAZY_API_KEY environment variable for per-session credentials when a saved config key is not desired, and rotate or revoke keys from the dLazy dashboard when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy service homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Guidance] <br>
**Output Format:** [JSON responses and agent-facing command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return asynchronous task identifiers when invoked with no-wait behavior.] <br>

## Skill Version(s): <br>
1.3.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
