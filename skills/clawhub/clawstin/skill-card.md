## Description: <br>
Inform users about Clawstin, an Austin OpenClaw meetup series, show current event details, and help with RSVP, mailing list signup, or organizer contact actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[youens](https://clawhub.ai/user/youens) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and community participants use this skill to learn about Clawstin meetups in Austin, review upcoming event details, and ask an agent to help RSVP, subscribe to updates, or contact organizers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: RSVP, mailing-list, and contact actions send user-provided personal details to clawstin.com. <br>
Mitigation: Tell users what information will be submitted and ask for confirmation before sending RSVP, subscription, or contact requests. <br>
Risk: Event listings can change over time. <br>
Mitigation: Fetch the machine-readable Clawstin event information before answering questions about upcoming events. <br>


## Reference(s): <br>
- [Clawstin website](https://clawstin.com) <br>
- [Clawstin events](https://clawstin.com/events) <br>
- [Clawstin machine-readable event and API information](https://clawstin.com/llms.txt) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [ClawHub skill listing](https://clawhub.ai/youens/skills/clawstin) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API calls, Guidance] <br>
**Output Format:** [Plain text or Markdown responses with JSON API requests for confirmed RSVP, subscription, or contact actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Fetches current event information before answering event questions; contact, RSVP, and mailing-list actions submit user-provided details to clawstin.com.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
