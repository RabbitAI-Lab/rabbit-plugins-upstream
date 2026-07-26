## Description: <br>
Exhaustive Google Places search using grid-based scanning. Finds ALL places, not just what Google surfaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[foeken](https://clawhub.ai/user/foeken) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to run Google Places searches over locations or coordinates, filter results by rating, reviews, and open status, retrieve reviews, and export results as JSON, CSV, or an HTML map. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Google Places API setup requires a sensitive API key and may create billing exposure if the key is unrestricted. <br>
Mitigation: Use a dedicated, restricted Google Places API key with billing limits; avoid printing or hardcoding it. <br>
Risk: The documented secret path is specific to the publisher's setup and may not match a user's environment. <br>
Mitigation: Replace the documented 1Password path with the user's own secret-manager reference. <br>
Risk: Installation from an unpinned source can change behavior over time. <br>
Mitigation: Review the source repository and install a pinned release when possible. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/foeken/skills/spots) <br>
- [Artifact-declared source repository](https://github.com/foeken/spots) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The underlying CLI can produce JSON, CSV, or HTML map output.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
