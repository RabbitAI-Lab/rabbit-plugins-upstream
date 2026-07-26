## Description: <br>
Location awareness via privacy-friendly GPS tracking (Home Assistant, OwnTracks, GPS Logger). Set location-based reminders and ask about movement history, travel time, and nearby POIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hegghammer](https://clawhub.ai/user/hegghammer) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and administrators use this skill to connect an agent to configured location providers, answer location-aware questions, manage geofences and reminders, and retrieve travel-time, movement-history, and nearby-place information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access precise location, saved places, and movement history. <br>
Mitigation: Install only for users who accept that exposure, configure the minimum needed provider, and avoid storing unnecessary historical or place data. <br>
Risk: Provider tokens and location endpoints can grant access to sensitive location data. <br>
Mitigation: Use dedicated minimal tokens, prefer environment variables for secrets, and avoid putting unrelated secrets in ~/.openclaw/.env. <br>
Risk: ETA, address lookup, nearby search, map links, and notification workflows can reveal location data to external services or channels. <br>
Mitigation: Enable only the commands and channels needed for the deployment, review configured endpoints, and disclose external sharing to users before use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/hegghammer/skills/location-awareness) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text or JSON returned by shell commands, with setup guidance in Markdown.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include precise coordinates, place names, map links, reminders, ETA estimates, location history, and nearby POI lists.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
