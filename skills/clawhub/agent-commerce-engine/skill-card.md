## Description: <br>
Agent Commerce Engine lets autonomous agents interact with compatible headless e-commerce backends through a standardized protocol for product discovery, cart operations, account flows, and order creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nowloady](https://clawhub.ai/user/nowloady) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to connect agent workflows to compatible commerce backends for product search, cart management, user profile actions, order creation, and payment handoff to the human user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can manage shopping carts, profile details, order creation, and locally stored store tokens. <br>
Mitigation: Use it only with trusted compatible stores, review order and profile details before submission, and run logout when the session is finished. <br>
Risk: Store APIs receive account credentials during login or registration and may receive personal shipping information during checkout preparation. <br>
Mitigation: Prefer trusted HTTPS store URLs and avoid providing passwords or fulfillment data unless the user intends to authenticate or create an order. <br>
Risk: Checkout creates a pending order but consumer payment still requires human authorization outside the agent. <br>
Mitigation: Hand any returned payment URL to the user and require the user to complete payment directly. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/nowloady/skills/agent-commerce-engine) <br>
- [Project Homepage](https://github.com/NowLoadY/agent-commerce-engine) <br>
- [Server-Side Implementation Specification](artifact/SERVER_SPEC.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON or text command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and the requests package; may use a store URL argument or optional COMMERCE_URL and COMMERCE_BRAND_ID environment variables.] <br>

## Skill Version(s): <br>
1.7.1 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
