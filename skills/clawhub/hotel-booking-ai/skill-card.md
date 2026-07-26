## Description: <br>
Book hotels with live prices and availability, including destination or hotel search, room-rate comparison, availability checks, reservations, booking lookup or cancellation, and WeChat Pay or Alipay payment initiation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tourmind](https://clawhub.ai/user/tourmind) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users use this skill when they explicitly want to search live hotel inventory, compare rates, create or manage a reservation, cancel a booking, or initiate payment. The agent should collect location, check-in date, check-out date, and guest count before making API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores and reuses a persistent user_key.txt while sending authentication and booking details to a plain HTTP API. <br>
Mitigation: Use only in a private environment, avoid shared machines, and delete user_key.txt when finished or when switching users. <br>
Risk: Live booking workflows or evals can create reservations, cancellations, or payment flows. <br>
Mitigation: Run booking actions only after explicit user intent and confirmation, and do not run evals against a live account unless real reservations are intended. <br>
Risk: Hotel prices, room availability, and cancellation fees can be wrong if stale or fabricated data is used. <br>
Mitigation: Use only live API responses, verify price and availability before booking, and report exact API errors rather than substituting recommendations from memory. <br>


## Reference(s): <br>
- [Hotel Booking AI Parameter Reference](references/parameter_guide.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/tourmind/skills/hotel-booking-ai) <br>
- [AgentAuth Dashboard](https://aauth-170125614655.asia-northeast1.run.app/dashboard) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API Calls, Guidance, Configuration] <br>
**Output Format:** [Markdown or plain text with JSON API request and response handling] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include hotel options, live prices, booking references, cancellation status, payment links, and exact API errors.] <br>

## Skill Version(s): <br>
0.2.4 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
