## Description: <br>
Generate AI-powered podcast-style audio narratives using Azure OpenAI's GPT Realtime Mini model via WebSocket. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thegovind](https://clawhub.ai/user/thegovind) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to add podcast-style text-to-speech workflows with Azure OpenAI Realtime API, including WebSocket streaming, voice selection, transcript handling, and PCM-to-WAV conversion for browser playback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Podcast prompts, scripts, transcripts, and generated-content context may be sent to Azure OpenAI. <br>
Mitigation: Use only approved Azure OpenAI configurations and avoid sending secrets, regulated data, or private material unless the organization has approved that provider and data flow. <br>
Risk: Realtime audio generation requires an Azure OpenAI API key. <br>
Mitigation: Store the API key in environment variables or an approved secrets manager, and avoid logging or committing credentials. <br>


## Reference(s): <br>
- [Architecture Reference](references/architecture.md) <br>
- [Code Examples](references/code-examples.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [PCM to WAV Helper](scripts/pcm_to_wav.py) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with Python, JavaScript, environment-variable, and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes WebSocket API integration guidance and PCM-to-WAV conversion patterns.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
