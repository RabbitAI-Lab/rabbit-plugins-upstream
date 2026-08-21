## Description:

Fetch health and fitness data from Garmin Connect -- 40+ metrics including sleep, HRV, stress, body battery, SpO2, VO2 Max, training status, and activities. Stores data locally as JSON and SQLite.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dw1161](https://clawhub.ai/user/dw1161)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an AI agent fetch, cache, and query their Garmin Connect health and fitness data for personal trend review and workout analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill accesses a Garmin account and stores detailed health history locally.

Mitigation: Install only when comfortable granting that access, keep data and token directories private, and delete the cache when local retention is no longer wanted.

Risk: Passing the Garmin password as a command-line argument can expose it through shell history or process listings.

Mitigation: Prefer macOS Keychain or environment variables for credentials instead of the CLI password flag.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dw1161/skills/garmin-connect-health)
- [OpenClaw](https://github.com/openclaw/openclaw)
- [python-garminconnect](https://github.com/cyberjunky/python-garminconnect)

## Skill Output:

**Output Type(s):** [text, json, code, shell commands, configuration, guidance]

**Output Format:** [Terminal status text, JSON snapshots, and SQLite tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes daily snapshots, latest cached JSON, OAuth token cache, and a local SQLite database under user-configurable directories.]

## Skill Version(s):

1.1.0 (source: frontmatter, skill.json, changelog, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
