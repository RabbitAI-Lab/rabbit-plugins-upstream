## Description: <br>
Checks or fixes the reading measure of body text by estimating characters per line and recommending readable max-width values for desktop and mobile layouts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[monikazapisekstudio](https://clawhub.ai/user/monikazapisekstudio) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Designers, developers, and agents use this skill to judge whether body-copy containers are too wide or narrow and to propose readable CSS or Figma sizing fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Direct Figma resizing could change design files if the agent is asked to apply a fix. <br>
Mitigation: Review the proposed width first and only permit direct node resizing when that edit is intended. <br>
Risk: Line-length estimates can vary by font, content, and container behavior. <br>
Mitigation: Treat recommendations as typography guidance and verify the result in the actual layout before shipping. <br>


## Reference(s): <br>
- [Server-resolved source provenance](https://github.com/monikazapisekstudio/design-engineering-playbook/tree/main/skills/typesetting-engine-skillset/line-length-optimizer) <br>
- [ClawHub skill page](https://clawhub.ai/monikazapisekstudio/skills/line-length-optimizer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown with CSS snippets and concise reasoning] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include measured or estimated characters per line, desktop/mobile verdicts, and Figma sizing guidance.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
