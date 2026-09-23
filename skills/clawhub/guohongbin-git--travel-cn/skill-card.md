## Description:

Travel CN helps agents query and compare China travel information across flights, hotels, trains, attractions, and common providers such as Qunar, Ctrip, Fliggy, and 12306.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guohongbin-git](https://clawhub.ai/user/guohongbin-git)

### License/Terms of Use:


## Use Case:

External users and developers use this skill to plan China travel, compare fares and hotel options, query train availability, and monitor price changes. It is suited to business travel planning, trip planning, and travel price tracking workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned package installation examples may install unexpected dependency versions.

Mitigation: Use a virtual environment, pin package versions, and review dependencies before installation.

Risk: Scraping travel provider sites can trigger provider blocking or violate provider expectations.

Mitigation: Prefer official provider APIs where available and confirm that scraping is allowed before use.

Risk: Travel prices and availability can change in real time.

Mitigation: Treat returned prices and availability as provisional and verify them with the provider before booking.

Risk: Travel queries may involve personal travel details or credentials.

Mitigation: Do not enter credentials or personal travel details unless the provider and workflow are trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guohongbin-git/skills/travel-cn)
- [Publisher profile](https://clawhub.ai/user/guohongbin-git)
- [Ctrip flight search endpoint example](https://api.ctrip.com/flight/search?from=SHA&to=PEK&date=2026-02-20)
- [Qunar flight search](https://flight.qunar.com/)
- [Ctrip hotel search endpoint example](https://api.ctrip.com/hotel/search?city=上海&checkin=2026-02-20)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, API Calls, Configuration]

**Output Format:** [Markdown with inline bash and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include provider API examples, scraping examples, and travel query command examples.]

## Skill Version(s):

1.0.0 (source: release.version, package.json, artifact version text)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
