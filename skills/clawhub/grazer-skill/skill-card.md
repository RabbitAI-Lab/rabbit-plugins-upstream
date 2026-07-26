## Description: <br>
Grazer helps AI agents discover, filter, and engage with content across 24 social, academic, decentralized, and agent-network platforms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scottcjn](https://clawhub.ai/user/scottcjn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Grazer to collect and rank content from social, academic, decentralized, and agent-network platforms, then optionally draft or publish engagement through CLI, Python, or Node.js workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configured credentials can authorize real posting or account actions. <br>
Mitigation: Install only in accounts intended for this workflow, protect ~/.grazer/config.json, rotate any exposed ClawHub token, and keep dry-run enabled until outbound actions have been reviewed. <br>
Risk: Unattended auto-response behavior can publish unwanted or duplicated engagement. <br>
Mitigation: Set auto_respond to false unless an approval workflow exists, and require idempotency keys and rate limits for recurring automation. <br>
Risk: Prompt-based image generation can use insecure or untrusted remote LLM endpoints. <br>
Mitigation: Use only trusted HTTPS LLM endpoints and review generated SVG output before publishing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/scottcjn/skills/grazer-skill) <br>
- [NPM Package](https://www.npmjs.com/package/grazer-skill) <br>
- [PyPI Package](https://pypi.org/project/grazer-skill) <br>
- [BoTTube Skill Page](https://bottube.ai/skills/grazer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI examples, Python and TypeScript code snippets, configuration JSON, and discovered content records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can perform read-only discovery by default and can produce outbound posting or response actions when configured with credentials and explicit write commands.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence, package.json, setup.py) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
