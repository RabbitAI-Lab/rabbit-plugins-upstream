## Description: <br>
Query and act on Evite events, guest lists, RSVPs, and messages from a shell with curl and a cookie jar instead of running the evite-mcp server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to generate curl-based guidance for reading Evite event data and performing RSVP, messaging, invitation, and related actions through authenticated session cookies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Evite credentials and live session cookies that can expose account access and guest data. <br>
Mitigation: Use a restricted cookie jar, protect credentials, and avoid printing or storing guest emails and phone numbers unnecessarily. <br>
Risk: Generated write commands can mutate real Evite events, including RSVPs, invitations, cancellations, messages, and broadcasts. <br>
Mitigation: Require explicit user approval before writes and test send or broadcast flows only against throwaway events and non-deliverable guests. <br>
Risk: The skill relies on private Evite endpoints whose behavior may change without notice. <br>
Mitigation: Review generated commands before execution and revalidate endpoint behavior when authentication, CSRF handling, or request bodies fail. <br>
Risk: Photo upload guidance can move local files to live Evite destinations. <br>
Mitigation: Confirm exact local file paths and upload targets before running upload commands. <br>


## Reference(s): <br>
- [Evite endpoint reference](references/endpoints.md) <br>
- [Evite](https://www.evite.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell command blocks and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include curl commands that read or mutate live Evite account data when executed by a user or agent.] <br>

## Skill Version(s): <br>
0.5.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
