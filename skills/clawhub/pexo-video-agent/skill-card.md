## Description: <br>
AI video generation skill with auto model selection across Seedance 2, Kling 3.0, HappyHorse, and 10+ models. Produces finished multi-shot videos (5-120s) from text, images, URLs, scripts, or audio, including AI music, lip sync, and multi-shot sequencing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pexo](https://clawhub.ai/user/pexo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and content teams use this skill to create finished short-form, product, brand, explainer, and marketing videos from text briefs, media files, URLs, scripts, or audio through Pexo projects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Video briefs, uploaded media, and generated outputs are sent to Pexo. <br>
Mitigation: Use the skill only for content approved for Pexo processing, and do not include secrets, confidential business data, regulated personal data, or untrusted remote files unless approved. <br>
Risk: The workflow can continue credit-gated video-generation work after explicit user approval. <br>
Mitigation: Review estimated credits and available balance before approval, and only run billing confirmation for work the user intends to pay for. <br>
Risk: Final delivery can include full signed download URLs for generated assets. <br>
Mitigation: Treat signed URLs as private until they expire and share them only with intended recipients. <br>
Risk: The skill requires a Pexo API key in local configuration. <br>
Mitigation: Store the key in an owner-only config file, keep it out of prompts and logs, and run the diagnostic script after setup or configuration errors. <br>


## Reference(s): <br>
- [Setup Checklist](references/SETUP-CHECKLIST.md) <br>
- [Troubleshooting](references/TROUBLESHOOTING.md) <br>
- [Pexo](https://pexo.ai) <br>
- [Pexo OpenClaw connection guide](https://pexo.ai/connect/openclaw) <br>
- [Pexo Video Agent on ClawHub](https://clawhub.ai/pexo/skills/pexo-video-agent) <br>
- [Pexo publisher profile on ClawHub](https://clawhub.ai/user/pexo) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Files] <br>
**Output Format:** [Markdown guidance with bash commands, JSON script outputs, project links, signed download URLs, and local video files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Final media outputs are 5-120 second videos with optional music, narration, subtitles, transitions, and aspect ratios 16:9, 9:16, or 1:1.] <br>

## Skill Version(s): <br>
0.3.12 (source: server release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
