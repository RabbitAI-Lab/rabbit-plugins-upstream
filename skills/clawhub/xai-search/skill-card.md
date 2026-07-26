## Description: <br>
Search X/Twitter and the web in real-time using xAI's Grok API with agentic search tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aydencook03](https://clawhub.ai/user/aydencook03) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and other agents use this skill to run real-time xAI/Grok searches across the web and X/Twitter, either through documented curl examples or the bundled helper script. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms and related context are sent to xAI/Grok when the skill is used. <br>
Mitigation: Avoid secrets, credentials, regulated data, and confidential internal information in queries. <br>
Risk: The helper script depends on an xAI API key and the xai-sdk package. <br>
Mitigation: Keep XAI_API_KEY in the environment rather than source files, and use a virtual environment with a pinned xai-sdk version. <br>


## Reference(s): <br>
- [xAI Documentation](https://docs.x.ai/docs/) <br>
- [ClawHub skill page](https://clawhub.ai/aydencook03/skills/xai-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown and terminal text, with optional citation URLs returned by xAI/Grok responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XAI_API_KEY and xai-sdk; user search terms are sent to xAI/Grok.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
