## Description:

Natal charts and transit forecasts from the third-party site grupovenus.com, with a saved people list. Use for Grupo Venus or carta astral readings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apresmoi](https://clawhub.ai/user/apresmoi)

### License/Terms of Use:

MIT-0

## Use Case:

People seeking natal charts or transit forecasts can use the skill to request chart images, review forecast data, and discuss astrological interpretations. It can keep a people list for later readings when the user consents to saving it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Birth details are sent to grupovenus.com, and city queries are sent to photon.komoot.io; third-party retention and live service behavior were not verified.

Mitigation: Explain these disclosures before the first request, suggest an alias, and obtain consent before saving a person.

Risk: Local deletion cannot retract information already sent to third parties, and temporary charts or exports outside managed storage may remain after forgetting a person.

Mitigation: Delete temporary charts after use and review saved charts and exports separately when removing personal data.

## Reference(s):

- [Grupo Venus](https://grupovenus.com)
- [Photon geocoding service](https://photon.komoot.io/api/)
- [Project homepage](https://github.com/apresmoi/grupo-venus)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Images]

**Output Format:** [Conversational readings, transit forecast JSON, and natal chart PNG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Birth details are used to request reports; saved people and chart data are stored locally only when the user opts in.]

## Skill Version(s):

0.2.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
