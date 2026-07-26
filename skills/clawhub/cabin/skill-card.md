## Description: <br>
Search and book real flights across 500+ airlines with USDC payments on Base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kobuta23](https://clawhub.ai/user/kobuta23) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and their agents use this skill to search flight options, compare fares, create bookings, and guide USDC payment on Base after explicit user approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit passenger personal data to Cabin and downstream travel providers. <br>
Mitigation: Collect only required passenger details and confirm with the user before sending booking requests. <br>
Risk: The skill can guide an agent toward real flight bookings and USDC payments. <br>
Mitigation: Require explicit approval for each booking and each payment, including fare, Base network, USDC amount, deposit address, and checkout URL. <br>
Risk: Wallet-capable agents could send funds without enough user oversight. <br>
Mitigation: Do not grant unattended wallet authority; require the user to approve any wallet action before funds are sent. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/kobuta23/skills/cabin) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/kobuta23) <br>
- [Project homepage](https://github.com/yolo-maxi/cabin) <br>
- [Cabin API](https://api.cabin.team) <br>
- [Cabin website](https://cabin.team) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, API calls, guidance] <br>
**Output Format:** [Markdown guidance with curl examples, structured booking details, payment instructions, and links to rendered flight comparison images.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include passenger data requirements, booking references, USDC payment amounts, Base deposit addresses, checkout URLs, confirmation links, and check-in links.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
