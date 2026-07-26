## Description: <br>
Automates ChatGPT-based manuscript review through a logged-in Brave Browser session, sending review prompts and saving feedback on factual accuracy, logic, and AI-like writing patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mayf3](https://clawhub.ai/user/mayf3) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and content reviewers use this skill to get a secondary ChatGPT review of articles, podcast scripts, or video scripts, then compare the feedback with another primary review model. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reviewed article and prompt content are sent to ChatGPT/OpenAI through the user's logged-in Brave session. <br>
Mitigation: Avoid confidential, regulated, proprietary, or unpublished material unless the applicable rules allow ChatGPT use. <br>
Risk: Brave remote debugging enables local browser automation control. <br>
Mitigation: Keep remote debugging bound locally and use it only for the review workflow. <br>
Risk: The configured output path may overwrite an existing file. <br>
Mitigation: Choose output paths deliberately and review the destination before running the skill. <br>


## Reference(s): <br>
- [Gpt Review on ClawHub](https://clawhub.ai/mayf3/skills/gpt-review) <br>
- [Prompt Template](references/prompt-template.md) <br>
- [GPT Review Gotchas](references/gotchas.md) <br>
- [ChatGPT](https://chatgpt.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown review text with command-line status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes the ChatGPT response to a user-specified output file; prompt content is sent through the user's logged-in ChatGPT session.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
