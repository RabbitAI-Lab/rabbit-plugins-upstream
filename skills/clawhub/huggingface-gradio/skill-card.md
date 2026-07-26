## Description: <br>
Build Gradio web UIs and demos in Python, including apps, components, event listeners, layouts, chatbots, and CLI interactions with Gradio Spaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huggingface](https://clawhub.ai/user/huggingface) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to create, edit, and reason about Gradio Python applications and demos. It is also useful for discovering and calling Gradio app endpoints when the user has confirmed the target Space, endpoint, payload, and any files or tokens involved. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes examples for calling remote Gradio Spaces, including predictions that may upload files or use tokens. <br>
Mitigation: Before running `gradio predict`, uploading files, or using `--token`, confirm the exact Space, endpoint, payload, files, and intended remote service with the user. <br>
Risk: Private files or secrets could be sent to a remote Gradio app if an agent follows CLI examples without review. <br>
Mitigation: Do not pass secrets, tokens, or private files unless the user explicitly intends to send them to that remote service. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huggingface/skills/huggingface-gradio) <br>
- [Gradio Quickstart](https://www.gradio.app/guides/quickstart) <br>
- [The Interface Class](https://www.gradio.app/guides/the-interface-class) <br>
- [Blocks and Event Listeners](https://www.gradio.app/guides/blocks-and-event-listeners) <br>
- [Controlling Layout](https://www.gradio.app/guides/controlling-layout) <br>
- [Custom HTML Components](https://www.gradio.app/guides/custom-HTML-components) <br>
- [Gradio End-to-End Examples](examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with Python and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Gradio component signatures, app patterns, event-listener examples, and CLI payload examples.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
