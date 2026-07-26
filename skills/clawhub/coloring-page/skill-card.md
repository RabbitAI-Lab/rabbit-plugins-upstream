## Description: <br>
Turn an uploaded photo into a printable black-and-white coloring page. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[borahm](https://clawhub.ai/user/borahm) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents use this skill to turn an end user's uploaded jpg, png, or webp photo into a printable black-and-white coloring-page PNG. It is intended for conversational requests such as creating a coloring page from an attached image. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a bundled local command and requires a Gemini API key. <br>
Mitigation: Install it only when comfortable running the local tool, and store the Gemini API key securely with access limited to the agent environment that needs it. <br>
Risk: Uploaded photos may be processed through the configured Gemini service. <br>
Mitigation: Use non-sensitive images unless the user is comfortable with that image content being processed by the configured service. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/borahm/skills/coloring-page) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Guidance] <br>
**Output Format:** [PNG image file with command-oriented usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts jpg, png, and webp inputs with optional 1K, 2K, or 4K output resolution.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
