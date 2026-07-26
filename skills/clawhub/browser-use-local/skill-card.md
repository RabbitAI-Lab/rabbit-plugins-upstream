## Description: <br>
Automates local browser workflows with browser-use CLI or Python, including opening pages, clicking and typing, taking screenshots, extracting HTML and links, debugging sessions, capturing QR codes, and running browser-use Agents with OpenAI-compatible LLMs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fengjiajie](https://clawhub.ai/user/fengjiajie) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation agents use this skill to control local browser sessions, inspect pages, capture screenshots or QR codes, and run browser-use Agents with OpenAI-compatible LLM endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local browser automation can expose sensitive page content, screenshots, HTML dumps, QR crops, extracted images, and persistent session data. <br>
Mitigation: Use only authorized pages, avoid private or logged-in sessions unless necessary, and clean up screenshots, HTML dumps, QR crops, extracted images, and persistent sessions after use. <br>
Risk: Agent runs require API keys and OpenAI-compatible LLM endpoints that may receive browser task context. <br>
Mitigation: Use trusted LLM endpoints, scoped API keys, and local environment configuration; do not commit or disclose API keys or session artifacts. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with bash and Python examples; helper scripts can print file paths and write PNG or JPEG image files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use persistent browser sessions, screenshots, HTML dumps, extracted images, and local environment variables for OpenAI-compatible LLM endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
