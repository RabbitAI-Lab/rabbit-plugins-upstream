## Description: <br>
Helps an agent prepare and run spoken narration or voiceover generation with Gemini 3.1 Flash TTS through Replicate. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators use this skill to collect text, voice, style prompt, and language inputs, then guide a Replicate text-to-speech request for narration, documentary lines, explainer voiceover, or audio to pair with generated video. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A Replicate API token is required to generate audio. <br>
Mitigation: Keep REPLICATE_API_TOKEN in the local environment and do not include it in prompts, generated files, or shared logs. <br>
Risk: Optional related PrunaAI skills may broaden the installed skill set. <br>
Mitigation: Install only the companion skills needed for the workflow and review them before adding the full suite. <br>
Risk: Generated narration may not match the intended text, tone, voice, or language. <br>
Mitigation: Confirm text, voice, prompt, and language_code before generation, then review the downloaded audio before using it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/gemini-3-1-flash-tts) <br>
- [Replicate model readme](https://replicate.com/google/gemini-3.1-flash-tts/readme) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown guidance with bash and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REPLICATE_API_TOKEN; ffmpeg and ffprobe are needed for trimming, concatenating scene voiceover, or mixing with a music bed.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
