## Description: <br>
Deep multi-source research via Parallel API for thorough research, comprehensive analysis, or investigation of a topic. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[normallygaussian](https://clawhub.ai/user/normallygaussian) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill when a user asks for deep research, competitive analysis, market research, due diligence, or other complex questions that need synthesis across many sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research prompts and uploaded query files may be processed by Parallel's external service. <br>
Mitigation: Avoid sending secrets, regulated data, or confidential business material unless that processing is acceptable for the user's environment. <br>
Risk: High-depth research runs can consume quota or incur billing impact on the authenticated Parallel account. <br>
Mitigation: Confirm parallel-cli is authenticated to the intended account and choose processor tiers deliberately for the depth required. <br>
Risk: The skill depends on a working official parallel-cli installation and authentication state. <br>
Mitigation: If parallel-cli is missing or authentication fails, stop and direct the user to the official Parallel CLI integration documentation. <br>


## Reference(s): <br>
- [Parallel](https://parallel.ai) <br>
- [Parallel API Docs](https://docs.parallel.ai) <br>
- [Parallel Research API Reference](https://docs.parallel.ai/api-reference/research) <br>
- [Parallel CLI Integration](https://docs.parallel.ai/integrations/cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples; Parallel research results may be saved as JSON and Markdown files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires installed and authenticated parallel-cli; research results can include task status, executive summary, findings, and source URLs.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
