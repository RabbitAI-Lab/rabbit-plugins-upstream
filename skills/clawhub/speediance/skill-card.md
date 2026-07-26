## Description: <br>
Reads completed Speediance Gym Monster workouts, exports exercise catalog data, and pushes custom training programs through the user's Speediance account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stozo04](https://clawhub.ai/user/stozo04) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agent developers with Speediance Gym Monster accounts use this skill to retrieve workout details, inspect the exercise catalog, and create custom training programs on their own account. <br>

### Deployment Geography for Use: <br>
Global, with Speediance API region configurable for Global or EU. <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Speediance email and password and may cache a session token locally. <br>
Mitigation: Use trusted, gitignored environment or config files, run from directories you control, and check the configured token cache path. <br>
Risk: Program creation can modify the user's Speediance account by adding training programs. <br>
Mitigation: Use dry-run mode and review generated program payloads before pushing them to the account. <br>
Risk: The integration is unofficial and depends on Speediance cloud API behavior that may change. <br>
Mitigation: Validate returned workout data before relying on it and re-check behavior after Speediance app or API changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/stozo04/skills/speediance) <br>
- [Source homepage](https://github.com/stozo04/speediance-cli) <br>
- [Release binaries](https://github.com/stozo04/speediance-cli/releases) <br>
- [Go package documentation](https://pkg.go.dev/github.com/stozo04/speediance-cli) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs Speediance workout, session, catalog, and program data; operations may read local credential/config files, cache a session token, write library/config files, and call the Speediance cloud API.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
