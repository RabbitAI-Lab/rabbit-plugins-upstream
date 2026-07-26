## Description: <br>
Generate and edit images with the Gemini API using dependency-free Python standard library tooling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cluka-399](https://clawhub.ai/user/cluka-399) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to generate new images or edit existing images from prompts using Google's Gemini API when they need a dependency-free Python workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, selected input images, and related request data are sent to Google's Gemini API under the user's API key. <br>
Mitigation: Use a purpose-specific API key and avoid submitting confidential, regulated, or private images unless external processing is acceptable. <br>
Risk: Gemini API usage may consume quota or incur billing under the configured account. <br>
Mitigation: Monitor quota and billing for the API key used with this skill. <br>


## Reference(s): <br>
- [Gemini Image Simple on ClawHub](https://clawhub.ai/cluka-399/skills/gemini-image-simple) <br>
- [Google AI Studio API keys](https://aistudio.google.com/apikey) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration instructions] <br>
**Output Format:** [PNG image file saved to a local path, with terminal status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires GEMINI_API_KEY; an optional input image can be provided for edits.] <br>

## Skill Version(s): <br>
1.1.0 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
