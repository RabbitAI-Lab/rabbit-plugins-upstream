## Description: <br>
Enables grounded question answering by automatically executing the Google Search tool within Gemini models when information is recent or requires verifiable citation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[theoseo](https://clawhub.ai/user/theoseo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to answer questions that require current web information, recent events, prices, weather, statistics, or source-backed citations through Gemini's Google Search grounding tool. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search prompts and surrounding context are sent to Google/Gemini. <br>
Mitigation: Avoid submitting secrets or regulated data, and use the skill only for prompts appropriate for the Gemini service. <br>
Risk: Gemini API keys can be exposed or over-permissioned if handled casually. <br>
Mitigation: Use a restricted Gemini API key, keep it in the GEMINI_API_KEY environment variable, and monitor API usage and billing. <br>
Risk: Dependency versions may change if installed without local controls. <br>
Mitigation: Pin dependencies locally when reproducible builds are required. <br>


## Reference(s): <br>
- [Google Search Tool Reference](references/api_reference.md) <br>
- [Google AI Studio API Keys](https://aistudio.google.com/app/apikey) <br>
- [Google Web Search on ClawHub](https://clawhub.ai/theoseo/skills/google-web-search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Natural-language text or Markdown with citation links, plus Python and shell snippets for setup and integration.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires GEMINI_API_KEY and can optionally use GEMINI_MODEL to select the Gemini model.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
