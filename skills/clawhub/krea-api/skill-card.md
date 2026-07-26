## Description: <br>
Generate images via Krea.ai API (Flux, Imagen, Ideogram, Seedream, etc.) <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fossilizedcarlos](https://clawhub.ai/user/fossilizedcarlos) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to generate images through Krea.ai models, inspect available models, list recent jobs, and configure Krea API credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Krea API secrets can be exposed if passed on the command line or stored with weak file permissions. <br>
Mitigation: Use the credential file at ~/.openclaw/credentials/krea.json with chmod 600 and prefer a dedicated or revocable Krea API key. <br>
Risk: Prompts are sent to Krea and image generation may consume account credits. <br>
Mitigation: Review prompts before generation and monitor usage through Krea account tooling. <br>


## Reference(s): <br>
- [Krea API keys and billing](https://docs.krea.ai/developers/api-keys-and-billing) <br>
- [Krea usage statistics](https://www.krea.ai/settings/usage-statistics) <br>
- [ClawHub skill page](https://clawhub.ai/fossilizedcarlos/skills/krea-api) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API Calls, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell and Python examples; command output is plain text with JSON-derived image URLs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Krea API credentials; generated prompts are sent to Krea and image generation may use account credits.] <br>

## Skill Version(s): <br>
0.2.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
