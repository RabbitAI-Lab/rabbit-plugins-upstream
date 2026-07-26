## Description: <br>
This skill lets an agent operate Adafruit IO through an OOMOL-connected account for reading feed/account data and creating feed data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users use this skill to operate Adafruit IO through an OOMOL-connected account, including account lookup, feed discovery, feed inspection, feed data retrieval, and confirmed creation of feed data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create new Adafruit IO feed data through the connected account. <br>
Mitigation: Confirm the feed, value, and expected effect with the user before approving write actions such as create_feed_data. <br>
Risk: The skill depends on a signed-in OOMOL account with an active Adafruit IO connection. <br>
Mitigation: Run setup or reconnection steps only after an action fails with an authentication, missing-scope, expired-credential, app, or billing error. <br>


## Reference(s): <br>
- [Adafruit IO](https://io.adafruit.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-adafruit-io) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector actions may return JSON data from Adafruit IO through the OOMOL oo CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
