## Description: <br>
Track a flight in real-time and notify when to leave for airport pickup based on distance to destination. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sundiraman](https://clawhub.ai/user/sundiraman) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to coordinate airport pickups by tracking a flight, estimating arrival timing, checking traffic-aware drive time, and deciding when to leave. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pickup origin and route details may be shared with Google Maps during drive-time checks. <br>
Mitigation: Confirm the pickup origin with the user before routing and avoid using saved home-address defaults without explicit approval. <br>
Risk: Scheduled monitoring can continue polling external services in the background. <br>
Mitigation: Use bounded schedules, document the polling interval, and stop monitoring after the flight lands or the pickup is cancelled. <br>
Risk: The artifact references a missing drive-time script and includes a placeholder flight-tracker script. <br>
Mitigation: Review and replace the packaged scripts before relying on automated pickup timing or notifications. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sundiraman/skills/flight-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses external flight-position and routing services; packaged scripts should be reviewed before use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
