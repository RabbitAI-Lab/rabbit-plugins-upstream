## Description: <br>
Use when managing a business's online review replies via the StarReview CLI: list unanswered reviews, draft replies in the owner's voice, submit them for owner approval, and report review KPIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fabsbags](https://clawhub.ai/user/fabsbags) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business owners, operators, and their agents use this skill to manage online review response workflows across supported providers. The agent can inspect unanswered reviews, request drafts, submit replies for owner approval, and report review KPIs while StarReview governs publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A StarReview API key can cover all businesses managed by the owner. <br>
Mitigation: Install only for intended business review workflows, keep the key revocable through StarReview, and rotate or revoke it if access should end. <br>
Risk: Drafted review replies may be inaccurate, off-brand, or inappropriate for the customer situation. <br>
Mitigation: Review submitted replies carefully and rely on the owner approval workflow before publication. <br>
Risk: Standing owner consent can allow some positive unedited drafts to be scheduled by StarReview. <br>
Mitigation: Check response fields such as autoScheduled, submitted, and awaitingManualPost before describing the outcome to the owner. <br>


## Reference(s): <br>
- [ClawHub StarReview skill page](https://clawhub.ai/fabsbags/skills/starreview) <br>
- [StarReview agent documentation](https://www.starreview.ch/agents/) <br>
- [StarReview MCP endpoint](https://mcp.starreview.ch/) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with shell commands and JSON CLI responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands emit one JSON document to stdout; authenticated commands require STARREVIEW_API_KEY.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
