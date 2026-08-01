## Description: <br>
Recommend hotel rooms and complete a real booking end to end — reserve an OpenTravel direct property with a payment link (bank QR, card, or PayPal), check payment status, resend an expired link, or cancel a booking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cotghw](https://clawhub.ai/user/cotghw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to find hotel rooms, compare direct and OTA options, create OpenTravel direct bookings, manage payment links, check booking status, and cancel reservations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create real hotel reservations and payment links. <br>
Mitigation: Confirm the hotel, dates, total price, guest name, email address, phone number, and payment method before creating a booking. <br>
Risk: Creating a second booking for the same stay can duplicate the reservation and confirmation email. <br>
Mitigation: Use the payment-link recreation flow for expired links instead of creating a new booking. <br>
Risk: OTA-only hotels cannot be reserved through this skill. <br>
Mitigation: Use only OTA URLs returned by the tools and present those options as external comparison or booking links. <br>


## Reference(s): <br>
- [Booking Assistant Tool Reference](artifact/reference.md) <br>
- [PriceWin Skills Hub](https://github.com/Price-Win/pricewin-skills-hub) <br>
- [ClawHub Skill Page](https://clawhub.ai/cotghw/skills/pricewin-booking-assistant) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, guidance] <br>
**Output Format:** [Markdown hotel recommendations with booking, payment, status, and cancellation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include returned payment links, confirmation codes, OTA links, room details, prices, cancellation terms, and status updates.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
