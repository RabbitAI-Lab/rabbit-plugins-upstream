## Description: <br>
Automates Gemini Web conversations by sending prompts, continuing conversations, handling image or file uploads, returning Gemini replies, and routing login or page-state recovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lainxxx](https://clawhub.ai/user/lainxxx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill when they need Gemini Web to answer a prompt, inspect an uploaded image or file, continue an existing conversation, or recover a Gemini browser session after login or page-state issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, images, and uploaded files may be sent to Gemini/Google through a browser session. <br>
Mitigation: Do not provide confidential or sensitive content unless sharing it with Gemini/Google is acceptable. <br>
Risk: The skill may create or reuse local browser session data and login state. <br>
Mitigation: Install and run it only when the user intentionally wants an agent to operate Gemini Web on their behalf. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/lainXXX/gemini-web-automation-skill) <br>
- [ClawHub skill page](https://clawhub.ai/lainxxx/skills/gemini-web-automation-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and structured JSON returned by the runtime scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Gemini replies, error codes, next actions, and instructions for login, proxy, Chrome path, or environment setup.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
