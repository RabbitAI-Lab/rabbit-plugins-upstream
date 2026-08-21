## Description:

Scrape Danish supermarket weekly tilbudsaviser (Lidl, Rema 1000, Netto, Meny, 365 discount) from the Tjek API and push filtered wow deals to ntfy.sh

This skill is ready for commercial/non-commercial use.

## Publisher:

[rune-philip](https://clawhub.ai/user/rune-philip)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure a weekly Danish grocery deal scraper that filters strong offers and sends concise shopping notifications plus a full deal list.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A public or guessable ntfy topic can expose shopping-interest notifications.

Mitigation: Use a random or authenticated ntfy topic, or self-host ntfy if shopping-interest privacy matters.

Risk: The weekly timer creates recurring automated notifications.

Mitigation: Enable the timer only when recurring weekly notifications are desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rune-philip/skills/danish-grocery-deals)
- [Tjek API endpoint](https://squid-api.tjek.com)
- [ntfy.sh](https://ntfy.sh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with Python scripts, JSON configuration, and systemd unit templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces weekly summaries, full text and JSON deal files, and optional ntfy notifications when configured.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
