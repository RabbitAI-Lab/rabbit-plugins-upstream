## Description: <br>
Search Google Flights for prices, times, and airlines. No API key required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[awlevin](https://clawhub.ai/user/awlevin) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and agents use this skill to search Google Flights from the command line for flight prices, schedules, airlines, seat classes, passenger counts, and one-way or round-trip itineraries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote install scripts and package managers can change the local Python environment. <br>
Mitigation: Install a trusted release through uv, pipx, or pip, and review install commands before execution. <br>
Risk: The --upgrade option changes the installed flight-search package. <br>
Mitigation: Use --upgrade only when an intentional package update is desired. <br>
Risk: Flight search results depend on Google Flights scraping through the underlying fast-flights library and may fail or be blocked by network or anti-bot controls. <br>
Mitigation: Treat returned itineraries and prices as advisory, retry transient failures, and verify booking details with an authoritative travel provider before purchase. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/awlevin/skills/flight-search) <br>
- [PyPI Project](https://pypi.org/project/flight-search/) <br>
- [fast-flights Underlying Library](https://github.com/AWeirdDev/flights) <br>
- [Project Homepage](https://github.com/Olafs-World/flight-search) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Text, JSON] <br>
**Output Format:** [Markdown guidance with shell commands; CLI results are text or JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires uvx for one-off execution; the package can also be installed with uv, pipx, or pip.] <br>

## Skill Version(s): <br>
0.1.7 (source: CHANGELOG.md and pyproject.toml, released 2026-02-06) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
