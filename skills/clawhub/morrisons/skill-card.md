## Description:

Automated search and insertion of grocery items to your active Morrisons supermarket trolley, viewing basket contents, listing delivery slots, reserving slots, managing shopping lists, and viewing previous orders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[homostellaris](https://clawhub.ai/user/homostellaris)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to automate Morrisons grocery account workflows, including product search, trolley updates, delivery-slot review and reservation, shopping-list management, checkout follow-up, and order-history review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change Morrisons account state, including trolley contents, shopping lists, delivery-slot reservations, and checkout follow-up state.

Mitigation: Review command names and arguments before execution, run read-only commands first when practical, and use extra care with delete-list, list-to-cart, add, and book-slot.

Risk: The skill uses Morrisons session cookies or login credentials and can import cookies from a local file.

Mitigation: Store credentials and session files with local OS protections, import cookies only from trusted sources, and rotate account credentials if session data may have been exposed.

Risk: The skill can send WhatsApp checkout reminders and start a delayed background checkout-status check after slot booking.

Mitigation: Configure an explicit Morrisons-specific WhatsApp target before slot reminders and monitor delayed follow-up behavior after booking a slot.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/homostellaris/skills/morrisons)
- [Server-resolved GitHub provenance](https://github.com/homostellaris/dotfiles/tree/master/agents/skills/morrisons)
- [Bun runtime](https://bun.sh)
- [Playwright](https://playwright.dev)
- [Morrisons grocery basket](https://groceries.morrisons.com/webshop/basket.do)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration guidance]

**Output Format:** [Markdown guidance with shell commands and text or serialized JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read or change Morrisons account state when run with authenticated session data.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
