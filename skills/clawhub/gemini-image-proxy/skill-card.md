## Description: <br>
Generate and edit images with Gemini API using the OpenAI Python SDK. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yspcoder](https://clawhub.ai/user/yspcoder) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers use this skill to generate new images or edit existing images from a command-line workflow through a configured OpenAI-compatible Gemini image endpoint. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and optional source images are sent to the configured API endpoint, which may have its own logging, retention, and data-handling practices. <br>
Mitigation: Use the skill only with a trusted GOOGLE_PROXY_BASE_URL endpoint and avoid confidential prompts, private images, or regulated data unless those practices are acceptable. <br>
Risk: The configured API key could grant access beyond this skill's intended image generation and editing workflow. <br>
Mitigation: Use a limited API key where possible and provide it only through the GOOGLE_PROXY_API_KEY environment variable. <br>
Risk: The workflow depends on the OpenAI Python package and a user-configured API-compatible service. <br>
Mitigation: Install the package only from a trusted source and verify the endpoint before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yspcoder/skills/gemini-image-proxy) <br>
- [Publisher profile](https://clawhub.ai/user/yspcoder) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, code, files] <br>
**Output Format:** [Markdown guidance with inline shell commands and a Python script that saves image files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires GOOGLE_PROXY_API_KEY, GOOGLE_PROXY_BASE_URL, Python 3.10+, and the openai package.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
