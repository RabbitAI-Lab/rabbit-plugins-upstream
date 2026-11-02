## Description:

Analyzes gecko and lizard tail images or video for tail length changes, visible wounds or scabs, and possible tail-loss events, then returns a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile keepers can submit tail images or video for an assessment of possible tail loss and review prior reports. Treat visual findings as prompts for review; a reptile veterinarian should assess injuries and care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected footage and an account identifier to LifeEmergence; credential storage and remote media deletion need clearer user control.

Mitigation: Use only after accepting this data transfer, and ask the publisher how stored credentials and remote media can be deleted.

Risk: Export-only mode can still upload footage, and --api-url should not be relied on to change the destination.

Mitigation: Do not use export-only mode as a no-upload safeguard; confirm the service destination before submitting footage.

Risk: The bundled client does not verify the service's retention promises or establish that automatic camera monitoring works.

Mitigation: Do not assume footage retention limits or unattended monitoring are enforced; review results and confirm service behavior with the publisher.

## Reference(s):

- [Tail-loss analysis API guide](artifact/references/api_doc.md)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-reptile-tail-loss-detection-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured tail assessment with a Markdown summary and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include estimated tail measurements, shortening ratios, tail-tip observations, alert levels, and suggested follow-up.]

## Skill Version(s):

1.0.15 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
