## Description:

Provides Taipei bus live-position lookup, sequence-based ETA estimates, route and stop information, map-oriented output examples, and abnormal-service detection using Taipei City and PTX public transit data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to answer Taipei bus questions, estimate arrivals, inspect route and stop details, and monitor public-transit anomalies. It is most useful for Taipei-focused transit assistance rather than general route planning.

### Deployment Geography for Use:

Taipei, Taiwan

## Known Risks and Mitigations:

Risk: Ordinary bus-related prompts may activate this Taipei-specific skill and make live public-transit API requests.

Mitigation: Use the skill when the user intent is clearly Taipei bus lookup or ask a clarifying question before making live transit requests.

Risk: Optional cron examples can poll transit data on a schedule and repeatedly post results.

Mitigation: Enable scheduled monitoring only for explicit user requests, set bounded intervals, and remove one-shot jobs when they are no longer needed.

Risk: Optional map integration can involve a third-party map API key and external map service.

Mitigation: Use map rendering only when the user asks for it and keep API keys outside shared prompts, logs, and generated examples.

Risk: ETA and route answers can be incomplete or stale because the skill combines live vehicle data with static PTX route and stop caches.

Mitigation: Label ETAs as estimates, surface missing-data conditions, and rebuild PTX caches on the documented schedule before relying on route or stop coverage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xuan905/skills/taipei-bus-skill)
- [Publisher profile](https://clawhub.ai/user/xuan905)
- [Taipei fixed-point vehicle OD API](https://tcgbusfs.blob.core.windows.net/blobbus/TstBusEvent.json)
- [PTX Taipei bus stops API](https://ptx.transportdata.tw/MOTC/v2/Bus/Stop/City/Taipei)
- [PTX Taipei bus routes API](https://ptx.transportdata.tw/MOTC/v2/Bus/Route/City/Taipei)
- [PTX Taipei bus stop-of-route API](https://ptx.transportdata.tw/MOTC/v2/Bus/StopOfRoute/City/Taipei)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown or plain text with JavaScript and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live transit API results, route and stop IDs, ETA estimates, anomaly summaries, cron payload examples, or map HTML examples.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact documentation references 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
