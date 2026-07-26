## Description: <br>
Google-AI Mode Search lets agents query Google AI Mode for a single keyword and return the AI Overview as Markdown with source links for research and web-summary tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and commerce analysts use this skill to ask one Google AI Mode search question and summarize the returned AI Overview for market research, technical Q&A, product exploration, and consumer preference analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search prompts and related metadata are sent to the service provider. <br>
Mitigation: Avoid confidential, regulated, or secret-bearing queries unless provider terms and data handling have been approved. <br>
Risk: Full responses and cached results may be saved locally. <br>
Mitigation: Run the skill only in an appropriate workspace and clean retained response or cache files when prompts or results contain sensitive material. <br>
Risk: Feedback may be sent automatically when behavior or satisfaction signals are detected. <br>
Mitigation: Review or disable feedback behavior before using the skill in sensitive workflows. <br>
Risk: Google AI Overview output is live, variable, and may not be available for every keyword. <br>
Mitigation: Treat results as time-specific, preserve source links, and tell users when the response reports zero AI Overview blocks. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/linkfox-ai/skills/linkfox-ai-mode-google-search) <br>
- [API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown returned in stdout, with saved JSON response files and concise terminal summaries for large responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single-keyword requests only; responses may vary because Google AI Mode is fetched live.] <br>

## Skill Version(s): <br>
1.0.4 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
