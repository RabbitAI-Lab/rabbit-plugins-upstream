## Description: <br>
Chat with Grok models via xAI API, including text chat, vision, model listing, and real-time X search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mvanhorn](https://clawhub.ai/user/mvanhorn) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external users use this skill to ask Grok for text answers, analyze selected images, search X/Twitter with citations, and list available xAI models from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, X search queries, and selected image files are sent to xAI under the user's API key. <br>
Mitigation: Use a dedicated xAI API key, avoid submitting sensitive content unless approved for xAI processing, and monitor usage and billing. <br>
Risk: Bundled artifact metadata lists versions that differ from the server release version. <br>
Mitigation: Verify the intended ClawHub release version before deployment and prefer the server release metadata for this card. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mvanhorn/skills/xai) <br>
- [xAI API documentation](https://docs.x.ai/api) <br>
- [xAI documentation](https://docs.x.ai) <br>
- [xAI](https://x.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text or JSON responses, with shell command examples for setup and invocation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XAI_API_KEY; may send prompts, selected image files, and X search queries to xAI under the user's API key.] <br>

## Skill Version(s): <br>
1.3.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
