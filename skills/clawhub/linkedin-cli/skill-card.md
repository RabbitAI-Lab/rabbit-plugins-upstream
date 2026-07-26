## Description: <br>
A LinkedIn CLI for searching profiles, checking messages, and summarizing a feed using LinkedIn session cookies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arun-8687](https://clawhub.ai/user/arun-8687) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators can use this skill to run LinkedIn account checks, people searches, profile lookups, feed summaries, and message previews from a terminal-backed agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires live LinkedIn session cookies that can grant account access. <br>
Mitigation: Install only when the publisher and dependency chain are trusted, store cookie values like passwords, and rotate or invalidate the session if exposure is suspected. <br>
Risk: The skill can print private LinkedIn messages and profile information to terminal output. <br>
Mitigation: Run it only in trusted environments and avoid capturing terminal output in shared logs or transcripts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/arun-8687/skills/linkedin-cli) <br>
- [Publisher profile](https://clawhub.ai/user/arun-8687) <br>
- [Project homepage listed in skill metadata](https://github.com/clawdbot/linkedin-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Text, Guidance] <br>
**Output Format:** [Terminal text and command-line guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, the linkedin-api package, and LINKEDIN_LI_AT and LINKEDIN_JSESSIONID environment variables.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
