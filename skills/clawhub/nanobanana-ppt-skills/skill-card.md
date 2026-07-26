## Description: <br>
NanoBanana PPT Skills helps agents analyze source documents, plan presentation structure, and generate styled slide images with optional transition videos and interactive playback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itrocker](https://clawhub.ai/user/itrocker) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, presentation authors, and agents use this skill to turn markdown documents or pasted content into slide plans, generated presentation images, optional transition videos, and HTML playback pages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Source documents, prompts, generated slide images, and video materials may be sent to third-party AI providers during generation. <br>
Mitigation: Use only approved providers and avoid confidential, regulated, or customer-sensitive material unless those providers are approved for that data. <br>
Risk: API keys can be exposed if pasted into chat, written into prompts, or committed with local configuration files. <br>
Mitigation: Configure keys locally in a protected .env file or secret manager, use limited-scope keys, and rotate any key that may have been shared. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [Architecture](ARCHITECTURE.md) <br>
- [Quickstart](QUICKSTART.md) <br>
- [API Management](API_MANAGEMENT.md) <br>
- [Security](SECURITY.md) <br>
- [Video Examples](README_VIDEO_EXAMPLES.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON slide plans, generated image files, HTML viewers, and optional MP4 videos.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create slides_plan.json, prompts.json, PNG slide images, HTML viewer files, transition prompt JSON, and optional video outputs under an outputs directory.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
