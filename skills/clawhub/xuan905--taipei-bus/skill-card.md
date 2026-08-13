## Description:

Provides Taipei bus real-time vehicle positions, sequence-based ETA estimates, route and stop information, map-oriented location data, and bus anomaly monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT-0

## Use Case:

Transit riders and agent users use this skill to ask about Taipei bus arrivals, vehicle locations, route stops, route summaries, and abnormal/off-duty buses. Developers can also use its JavaScript examples and helper modules to integrate Taipei bus lookups, maps, or scheduled reminders into an agent workflow.

### Deployment Geography for Use:

Taipei, Taiwan

## Known Risks and Mitigations:

Risk: The skill makes public transit API network calls and reads local cache files.

Mitigation: Use it for Taipei bus queries and review network access expectations and cache file placement before deployment.

Risk: Broad activation keywords can cause the skill to run for loosely related bus questions.

Mitigation: Confirm the user is asking about Taipei bus status, routes, stops, ETA, maps, or anomaly monitoring before invoking the skill.

Risk: Optional cron reminders can repeat unintentionally or announce results to an unexpected channel.

Mitigation: Review the schedule and delivery target, and set deleteAfterRun to true for one-time arrival alerts.

Risk: ETA and route matching depend on separate TstBusEvent and PTX ID systems plus static route and stop caches.

Mitigation: Present ETA as an estimate, bridge IDs through route or stop name search, and rebuild caches periodically.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xuan905/skills/taipei-bus)
- [README.en.md](README.en.md)
- [README.zh-TW.md](README.zh-TW.md)
- [Taipei City fixed-point vehicle OD API](https://tcgbusfs.blob.core.windows.net/blobbus/TstBusEvent.json)
- [PTX Taipei bus stops API](https://ptx.transportdata.tw/MOTC/v2/Bus/Stop/City/Taipei)
- [PTX Taipei bus routes API](https://ptx.transportdata.tw/MOTC/v2/Bus/Route/City/Taipei)
- [PTX Taipei bus stop-of-route API](https://ptx.transportdata.tw/MOTC/v2/Bus/StopOfRoute/City/Taipei)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text responses with JavaScript examples and JSON-like transit records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include real-time public transit API results, cached stop and route data, ETA estimates, anomaly summaries, and optional cron job configuration.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact SKILL.md labels internal content version 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
