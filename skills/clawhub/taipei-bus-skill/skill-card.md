## Description:

Provides Taipei bus position lookup, route and stop search, sequence-based ETA estimates, map-oriented outputs, and anomaly detection using Taipei City and PTX public transit data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT-0

## Use Case:

Transit riders, operators, and agent developers can use this skill to answer Taipei bus status questions, estimate arrivals, inspect route and stop information, and set up optional monitoring examples for recurring bus checks.

### Deployment Geography for Use:

Taipei, Taiwan

## Known Risks and Mitigations:

Risk: The skill makes public transit API calls and may create local cache files for Taipei bus stops and routes.

Mitigation: Run it in an environment where outbound public API calls and local cache creation are expected, and rebuild caches when current route or stop data matters.

Risk: Broad bus-related triggers can cause the skill to answer questions outside its Taipei bus data coverage.

Mitigation: Use explicit Taipei bus route, stop, ETA, or anomaly questions and disclose when a requested route, transfer, or region is unsupported.

Risk: Optional cron and push-notification examples can create recurring background checks.

Mitigation: Enable scheduled alerts only when the user intentionally requests recurring monitoring and review the schedule, timezone, and notification target.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xuan905/skills/taipei-bus-skill)
- [Publisher Profile](https://clawhub.ai/user/xuan905)
- [Taipei Bus Fixed-Point Vehicle API](https://tcgbusfs.blob.core.windows.net/blobbus/TstBusEvent.json)
- [PTX Taipei Bus Stops API](https://ptx.transportdata.tw/MOTC/v2/Bus/Stop/City/Taipei)
- [PTX Taipei Bus Routes API](https://ptx.transportdata.tw/MOTC/v2/Bus/Route/City/Taipei)
- [PTX Taipei StopOfRoute API](https://ptx.transportdata.tw/MOTC/v2/Bus/StopOfRoute/City/Taipei)
- [Artifact Documentation](artifact/docs/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text with optional JavaScript and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include public transit data, ETA estimates, route and stop lists, anomaly summaries, local cache instructions, and optional cron or map integration examples.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
