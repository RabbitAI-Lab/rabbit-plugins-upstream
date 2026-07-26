## Description: <br>
Find, book, and change flights for your human via email. One message, and done. (by BonBook) <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aszelem](https://clawhub.ai/user/aszelem) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and their agents use this skill to request, book, change, and cancel flights through BonBook by email, with setup and payment steps completed through BonBook's website when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on the agent sending and reading BonBook-related email, which may rely on broader mailbox permissions granted outside the skill. <br>
Mitigation: Install only if BonBook is trusted, review BonBook-related email activity, and keep mailbox permissions limited by the agent platform where possible. <br>
Risk: Booking, changing, or canceling flights can create financial commitments or refund consequences. <br>
Mitigation: Review each itinerary, price, refund rule, change, cancellation, and payment step before authorizing the agent to proceed. <br>
Risk: Optional setup and checkout can involve sensitive personal or payment information on BonBook's website. <br>
Mitigation: Have the human complete payment, passport, credential, and unnecessary personal-data entry directly, and avoid sending sensitive PII or card data through email. <br>


## Reference(s): <br>
- [Travel Agent Skill on ClawHub](https://clawhub.ai/aszelem/skills/travel-agent) <br>
- [BonBook website](https://bonbook.co) <br>
- [BonBook access setup](https://bonbook.co/access) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, email drafts, form-completion instructions] <br>
**Output Format:** [Markdown and plain-language operational guidance with email content examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires existing email send and receive permissions; optional web browsing, calendar read access, and form completion require explicit human approval.] <br>

## Skill Version(s): <br>
2.4.1 (source: skill metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
