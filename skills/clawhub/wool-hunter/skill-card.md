## Description: <br>
A shopping-deals skill that searches coupons and compares prices across Chinese e-commerce platforms, queries deal benefits, and routes Meituan/local-life requests to a companion skill through Coze Bot APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guipi888](https://clawhub.ai/user/guipi888) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users use this skill to find coupons, compare prices, and query shopping or local-life deals across supported platforms. Agent operators use it when they are comfortable routing deal searches and configured tokens to Coze API endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product searches and deal requests are sent to external Coze API endpoints. <br>
Mitigation: Install only when external Coze processing is acceptable for the intended queries, and avoid sending sensitive shopping or personal information. <br>
Risk: Bearer tokens are used with configurable Coze endpoint URLs. <br>
Mitigation: Treat Coze tokens as secrets, restrict who can edit COZE_BASE_URL or coze_api_url values, and avoid untrusted endpoint configuration. <br>
Risk: Normal and error responses can include promotional or contact text. <br>
Mitigation: Review response formatting before deployment and decide whether the appended promotional/contact text is acceptable for the agent environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/guipi888/skills/wool-hunter) <br>
- [Project homepage](https://github.com/guipi888/wool-hunter) <br>
- [README](README.md) <br>
- [Skill definition](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown tables and plain text with shell command and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include externally generated Coze results and fixed promotional/contact text appended by the artifact scripts.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
