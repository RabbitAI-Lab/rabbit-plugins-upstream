## Description:

Runs a Telegram-based body measurement workflow that validates adult consent and scan inputs, submits a video to an AnthroVision bridge, polls scan status, and returns structured body measurements and waist-to-hip ratio output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External Telegram users and agent operators use this skill to collect explicit consent, submit an adult single-person body scan video, monitor processing, and receive concise measurement results. It is not intended for medical diagnosis, minors, non-consensual videos, or multi-person scans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow handles highly sensitive body-video and body-measurement data with unclear storage and retention boundaries.

Mitigation: Use only after reviewing the AnthroVision bridge privacy policy, including what data is sent, where it is stored, retention and deletion terms, and access controls.

Risk: The skill declares broad read, write, and exec tool authority for a workflow that primarily needs controlled scan submission and status polling.

Mitigation: Install with the narrowest available tool permissions and remove unnecessary read, write, or exec authority before deployment.

Risk: Body scans can be misused if submitted for minors, non-consenting people, non-personal videos, or medical interpretation.

Mitigation: Require explicit adult consent, reject minors and non-consensual or multi-person videos, and present measurements without medical diagnosis or health advice.

Risk: Private or local file paths and URLs could expose local or internal resources.

Mitigation: Accept only uploaded video attachments or public HTTPS video URLs and reject local paths, localhost, loopback, and RFC1918 private network URLs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/anthrovision-telegram-body-scan)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown-style Telegram messages with structured fields such as scan_id, status, measurements, and waist-to-hip ratio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic status and measurement summaries; processing timeout prompt after about 3 minutes.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
