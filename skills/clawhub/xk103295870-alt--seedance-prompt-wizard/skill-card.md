## Description: <br>
Seedance Prompt Wizard guides users through a short dialogue to turn rough video ideas into precise Seedance 2.0 prompts without making API calls or using credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xk103295870-alt](https://clawhub.ai/user/xk103295870-alt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and creative teams use this skill to gather video intent, reference media details, style, camera movement, duration, aspect ratio, and audio preferences, then produce a ready-to-use Seedance 2.0 prompt with suggested parameters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad Chinese prompt-writing requests, which can make it respond when the user did not specifically intend to create a Seedance video prompt. <br>
Mitigation: Confirm the user wants Seedance video prompt generation before collecting video parameters or producing the final prompt. <br>
Risk: Generated output can reference third-party Seedance APIs or platforms where users may upload private prompts or media. <br>
Mitigation: Verify the third-party platform separately and avoid uploading sensitive media or prompts unless the destination is trusted for that data. <br>


## Reference(s): <br>
- [Seedance API documentation](https://seedance2api.app) <br>
- [ClawHub skill page](https://clawhub.ai/xk103295870-alt/seedance-prompt-wizard) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown text with a Chinese prompt, English prompt, suggested Seedance parameters, and usage notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No code execution, API calls, or credential handling; output may include suggested media references and third-party Seedance API parameters.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
