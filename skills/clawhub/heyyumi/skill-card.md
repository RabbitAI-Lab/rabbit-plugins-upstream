## Description:

Find Korean restaurants, cafes and bars and send user-confirmed table reservation requests, with venue responses delivered in chat.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmp-dev](https://clawhub.ai/user/hmp-dev)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use HeyYumi to find Korean restaurants, cafes and bars by location and preferences. They can request a reservation in chat and follow the venue's response in their own language.

### Deployment Geography for Use:

South Korea (Seoul, Gyeonggi, Busan, Jeju, Incheon, Daejeon, Sejong, and North and South Chungcheong)

## Known Risks and Mitigations:

Risk: Reservation requests share the guest's name, phone number, optional email, and note with HeyYumi and the venue; identifiable booking details are retained for three years according to the privacy policy.

Mitigation: Explain what details will be shared and the stated retention period, then send a request only after the user confirms the complete booking details.

Risk: A reservation request may remain pending or be declined, so submitting it does not mean a table is booked.

Mitigation: Describe the request as pending until the venue returns a confirmed status, and relay declined or expired outcomes clearly.

## Reference(s):

- [HeyYumi website and service information](https://heyyumi.ai/mcp)
- [HeyYumi developer guide and REST API](https://heyyumi.ai/developers)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Conversational text with venue details and reservation updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Distinguishes a pending request from a confirmed reservation.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
