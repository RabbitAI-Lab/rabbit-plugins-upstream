## Description: <br>
Real Browser QA Ceki Main helps agents drive real Chrome browser sessions for authorized QA, end-to-end, accessibility, and security testing with realistic user interaction patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iwedmak](https://clawhub.ai/user/iwedmak) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, QA engineers, security testers, and support automation teams use this skill to test web applications they own or are explicitly authorized to assess through real browser sessions. It is intended for browser UI workflows such as form testing, rendering checks, accessibility review, synthetic monitoring, and vulnerability discovery where headless automation may miss real-world behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review says bundled profiles include third-party signup, CAPTCHA delegation, mailbox verification, and social engagement automation beyond owned-site testing. <br>
Mitigation: Install and use the skill only for clearly authorized QA or security testing; remove or ignore consumer-platform domain profiles and avoid account creation, CAPTCHA solving, mailbox verification, posting, liking, following, or payment-adjacent actions unless explicitly authorized with human approval for each action. <br>
Risk: Marketplace browser sessions can expose screen contents, navigation, keystrokes, chat, private content, or production credentials to a host. <br>
Mitigation: Prefer Self mode or a dedicated test browser profile, and do not use Marketplace mode with production credentials, payment data, or private content. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/iwedmak/skills/real-browser-qa-ceki-main) <br>
- [Ceki dashboard](https://ceki.me) <br>
- [Ceki extension install](https://browser.ceki.me/install) <br>
- [ceki-sdk on PyPI](https://pypi.org/project/ceki-sdk/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON configuration, and code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide an agent to use the ceki CLI or SDK to create and control authorized browser sessions.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
