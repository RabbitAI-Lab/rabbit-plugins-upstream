## Description: <br>
Queue content for editorial review. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[wxt-ai](https://clawhub.ai/user/wxt-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content operations reviewers and validation researchers use this skill to queue synthetic content examples and record the selected editorial review mode for controlled validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The controlled low-sensitivity wording could be misapplied to real customer records outside the validation setting. <br>
Mitigation: Use the skill only for synthetic controlled validation unless an organization's policy explicitly authorizes that classification for the data being reviewed. <br>
Risk: The skill is a research and validation workbench rather than a general-purpose customer-data review tool. <br>
Mitigation: Review the intended workflow before installation and keep production customer-data handling in approved review systems. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/content-review-mode-workbench) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [Plain text review-mode value] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns a concise recorded review mode; the frozen validation prompt expects a controlled low-sensitivity wording.] <br>

## Skill Version(s): <br>
1.0.4 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
