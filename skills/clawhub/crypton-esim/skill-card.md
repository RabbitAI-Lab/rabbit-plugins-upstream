## Description: <br>
Purchase anonymous eSIMs with BTC/XMR/card - no account required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ajarmoszuk](https://clawhub.ai/user/ajarmoszuk) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users use this skill to browse eSIM plans, create Crypton.sh guest checkout sessions, and check eSIM order status from chat without creating an account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends plan lookup, checkout, payment, and order retrieval requests to Crypton.sh. <br>
Mitigation: Install and use it only when Crypton.sh is an acceptable third-party service for the user's eSIM purchase workflow. <br>
Risk: Order UUIDs, payment links or wallet addresses, ICCIDs, QR codes, and activation codes can grant access to purchase or eSIM activation details. <br>
Mitigation: Handle these values as sensitive credentials and avoid sharing them outside the intended user session. <br>
Risk: The skill depends on runtime HTTP requests through the Python requests package. <br>
Mitigation: Run it in an environment that resolves dependencies to current patched versions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ajarmoszuk/skills/crypton-esim) <br>
- [Crypton guest eSIM API documentation](https://crypton.sh/esim/guest) <br>
- [Crypton website](https://crypton.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, guidance] <br>
**Output Format:** [Markdown-like chat responses with plan listings, checkout details, payment instructions, order status, ICCIDs, and activation codes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the Crypton.sh guest eSIM API; no API key is required by the skill.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence, created 2026-02-04T17:03:52Z) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
