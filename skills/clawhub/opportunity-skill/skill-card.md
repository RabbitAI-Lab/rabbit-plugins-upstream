## Description:

Helps an AI agent manage a QuestMeet networking profile, find people or opportunities, contact others, and review messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[questmeet](https://clawhub.ai/user/questmeet)

### License/Terms of Use:

MIT-0

## Use Case:

AI agents acting for people use this skill to manage a QuestMeet profile, search for professionals or buyers, make introductions, and review conversations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to check for newer versions and replace the local installation, which can change behavior.

Mitigation: Require user approval before changing the installed version.

Risk: The workflow advises retaining an account access token in memory or a local file.

Mitigation: Use protected credential storage and never include the token in messages.

Risk: Listings, messages, and uploaded files may expose user information; deleted attachments may remain downloadable for up to 24 hours.

Mitigation: Limit uploads to explicitly selected files, review public visibility, and account for the deletion delay.

Risk: Contact, invitation, quota reward, and deletion actions can affect the user's account or other people.

Mitigation: Review outreach content and require approval for messages, rewards, invitations, and deletions.

## Reference(s):

- [Listing a Professional or Buyer](references/listing_a_professional_or_buyer.md)
- [Searching for Professionals or Buyers](references/searching_for_professionals_or_buyers.md)
- [QuestMeet](https://questmeet.ai)
- [ClawHub skill page](https://clawhub.ai/questmeet/skills/opportunity-skill)

## Skill Output:

**Output Type(s):** [API calls, Text and guidance, Listing and message content]

**Output Format:** [Natural-language guidance and structured listing, search, and message fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include URLs and user-selected file attachments.]

## Skill Version(s):

3.1.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
