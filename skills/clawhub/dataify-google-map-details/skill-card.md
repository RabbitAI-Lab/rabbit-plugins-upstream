## Description:

Collect structured Google Maps place or business details from a known map URL, CID, location input, or Place ID.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify Builder jobs for Google Maps place or business detail collection by URL, CID, location inputs, or Place ID, then monitor the task and return the collected JSON result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dataify receives Google Maps URLs, IDs, keywords, coordinates, and uses the user's Dataify API token and credits.

Mitigation: Use the skill only for approved collection targets, keep the token in DATAIFY_API_TOKEN, and never expose the token in chat or generated output.

Risk: Location mode can broaden collection into discovery-capable workflows despite the stated no-discovery language.

Mitigation: Confirm the intended location scope before submitting location-mode tasks, especially when keywords, coordinates, or multiple inputs could expand collection.

Risk: Implicit invocation and auto-run guidance can submit external collection tasks before the user notices a scope or cost issue.

Mitigation: Ask for explicit confirmation when inputs are ambiguous, high volume, multi-input, or likely to affect credit usage.

## Reference(s):

- [Modes and parameters](references/modes-and-parameters.md)
- [Google Country Options](references/google_countries.md)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-map-details)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON task or result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit an external Dataify Builder task and return either the final collected JSON result or a resumable task ID if waiting times out.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
