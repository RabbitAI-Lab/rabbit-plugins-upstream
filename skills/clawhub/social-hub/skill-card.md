## Description: <br>
Social Hub is a personal relationship-matching agent that runs locally, converses with users through WeChat Work, builds local profile data, shares profile tag summaries for matching, and helps deliver match results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[freeai-io](https://clawhub.ai/user/freeai-io) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users run this local personal agent to have relationship-matching conversations, maintain profile information, receive proposed matches, and manage profile disclosure or deletion requests. Operators should also review the bundled Claw Club social-bot scripts before deployment because they can register bots, read feeds, and post or reply through an external API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security summary says the release describes a local relationship-matching assistant but also bundles under-disclosed Claw Club social-bot tooling. <br>
Mitigation: Install only when both behaviors are intended, and ask the publisher to document or remove the Claw Club scripts before operational use. <br>
Risk: Bundled scripts can store a Claw Club API key locally and use it to register accounts, read feeds, post messages, and reply through api.vrtlly.us. <br>
Mitigation: Review credential storage, posting authority, consent, data flows, deletion, and revocation steps before running the scripts with real accounts or user data. <br>
Risk: The skill handles personal profile and relationship-matching data. <br>
Mitigation: Confirm user consent, disclosure settings, local data deletion behavior, and what profile tags are shared before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/freeai-io/skills/social-hub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with conversational text, profile-management instructions, local file paths, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local ChromaDB profile storage, WeChat Work interactions, group-channel match messages, and Claw Club API credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
