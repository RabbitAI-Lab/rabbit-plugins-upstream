## Description: <br>
Research Idea launches background Clawdbot sessions that research business ideas, save a comprehensive Markdown analysis, and return a summary verdict to the active chat. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rqrqrqrq](https://clawhub.ai/user/rqrqrqrq) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to trigger business idea research from chat, including market, technical, go-to-market, risk, validation, and recommendation analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Business ideas may be sensitive and can be used in web searches or returned to the active chat. <br>
Mitigation: Use a private chat for confidential ideas and avoid submitting details that should not leave the local environment. <br>
Risk: Research sessions create persistent local Markdown output under ~/clawd/ideas/. <br>
Mitigation: Review and delete generated sessions or files when they are no longer needed. <br>
Risk: Generated market research and verdicts may be incomplete, outdated, or misleading. <br>
Mitigation: Verify important claims and sources before using the output for business decisions. <br>


## Reference(s): <br>
- [Research Idea ClawHub listing](https://clawhub.ai/rqrqrqrq/skills/research-idea) <br>
- [README](artifact/README.md) <br>
- [Idea Exploration Prompt Template](artifact/templates/idea-exploration-prompt.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown research report with a concise chat summary and verdict] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes research.md under ~/clawd/ideas/<slug>/ and returns results to the active chat.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
