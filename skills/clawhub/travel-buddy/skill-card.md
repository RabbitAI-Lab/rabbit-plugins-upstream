## Description:

Discover, compare, and plan trips from incomplete traveler needs, then revise them when constraints change.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use Travel Buddy to turn incomplete travel needs into destination shortlists, verified itineraries, local travel profiles, and replans when constraints change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles private travel profile and trip-planning files and has helper scripts with local file and network access.

Mitigation: Review before installing, use OpenClaw or a pinned/tagged install path where possible, and keep the Travel Buddy workspace in a private local folder.

Risk: Validators and link checkers may access plan or HTML content supplied by someone else.

Mitigation: Avoid running validators or link checkers on plans or HTML from people you do not trust.

Risk: Named assistant handoff flags can start a detached planner task.

Mitigation: Do not enable --assistant codex or --assistant claude unless you intentionally want a detached planner task.

## Reference(s):

- [Travel Buddy skill definition](artifact/SKILL.md)
- [Travel Buddy README](artifact/README.md)
- [Initial intake reference](artifact/references/initial-intake.md)
- [Research budget reference](artifact/references/research-budget.md)
- [Decision and research reference](artifact/references/decision-and-research.md)
- [Regional service routing reference](artifact/references/regional-service-routing.md)
- [Booking HTML output reference](artifact/references/booking-html-output.md)
- [Profile and storage reference](artifact/references/profile-and-storage.md)
- [Verification reference](artifact/references/verification.md)
- [Replanning reference](artifact/references/replanning.md)
- [ClawHub skill page](https://clawhub.ai/dong845/skills/travel-buddy)
- [ClawHub publisher profile](https://clawhub.ai/user/dong845)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with local JSON, HTML, and calendar deliverables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local workspace files for trip intake, destination shortlists, verified plans, self-contained itinerary HTML, and calendar exports.]

## Skill Version(s):

2.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
